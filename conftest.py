import base64
import json
import os
import socket
import subprocess
import time
import urllib.error
import urllib.request
from datetime import datetime

import pytest

from utils.driver_factory import create_android_driver
from utils.StoreToMySQL import store_transaction_result


APP_PACKAGE = "calculator.currencyconverter.tipcalculator.unitconverter"

# Target device/emulator. Set ANDROID_SERIAL (or UDID) when more than one
# device is attached, e.g. ANDROID_SERIAL=emulator-5554
DEVICE_SERIAL = os.getenv("ANDROID_SERIAL") or os.getenv("UDID")

ARTIFACTS_DIR = os.getenv("ARTIFACTS_DIR", "artifacts")
BOOT_TIMEOUT_SEC = int(os.getenv("BOOT_TIMEOUT_SEC", "180"))

# Post-boot "settle" phase: sys.boot_completed=1 does not mean the system has
# stopped starting services, and tests started in that window hit boot-time ANRs.
SETTLE_STEP_TIMEOUT_SEC = int(os.getenv("SETTLE_STEP_TIMEOUT_SEC", "90"))
SETTLE_PAUSE_SEC = int(os.getenv("SETTLE_PAUSE_SEC", "15"))
# 1-minute load average must drop below this; default is 75% of the device cores
SETTLE_LOAD_THRESHOLD = os.getenv("SETTLE_LOAD_THRESHOLD")

# ---- Email alerting via Resend (all via environment variables; keep secrets out of the repo)
# Alerts are skipped (with a console note) if RESEND_API_KEY, ALERT_FROM or
# ALERT_TO is missing, so local runs without credentials are unaffected.
RESEND_API_KEY = os.getenv("RESEND_API_KEY")
RESEND_API_URL = os.getenv("RESEND_API_URL", "https://api.resend.com/emails")
# Must be on a domain verified in Resend, e.g. "QA Alerts <alerts@yourdomain.com>".
# (onboarding@resend.dev works for testing, but only delivers to your own Resend account email.)
ALERT_FROM = os.getenv("ALERT_FROM")
ALERT_TO = [a.strip() for a in os.getenv("ALERT_TO", "").split(",") if a.strip()]
ALERT_LABEL = os.getenv("ALERT_LABEL", "APPIUM ANDROID")  # shown in the subject as [LABEL]
ALERT_MAX_ATTACHMENTS = int(os.getenv("ALERT_MAX_ATTACHMENTS", "10"))
ALERT_MAX_ATTACHMENT_MB = float(os.getenv("ALERT_MAX_ATTACHMENT_MB", "5"))
# Resend caps a message at 40 MB after base64 encoding; stay well under that
ALERT_MAX_TOTAL_MB = float(os.getenv("ALERT_MAX_TOTAL_MB", "20"))

# Collected during the run, summarised in one email from pytest_sessionfinish
_failures = []
_abort_reason = None
_alert_sent = False  # only the FIRST failure of a run triggers an email


# ============================================================================
# ADB HELPERS
# ============================================================================

def _adb(*args, timeout=15):
    """Run an adb command against DEVICE_SERIAL (if set)."""
    cmd = ["adb"]
    if DEVICE_SERIAL:
        cmd += ["-s", DEVICE_SERIAL]
    cmd += list(args)
    return subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)


def _shell(*args, timeout=15):
    return _adb("shell", *args, timeout=timeout).stdout.strip()


def _wait_until(description, predicate, timeout, interval=2):
    """Poll predicate() until it returns True or the timeout expires. Never raises."""
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        try:
            if predicate():
                print(f"  [ok] {description}")
                return True
        except Exception:
            pass
        time.sleep(interval)
    print(f"  [timeout] {description} (continuing anyway)")
    return False


def _activity_resumed():
    out = _shell("dumpsys", "activity", "activities", timeout=30)
    return any(
        ("topResumedActivity" in line or "mResumedActivity" in line) and "ActivityRecord" in line
        for line in out.splitlines()
    )


def _load_is_low(threshold):
    return float(_shell("cat", "/proc/loadavg").split()[0]) < threshold


def wait_until_settled():
    """
    Wait for the system to finish its post-boot work before tests start:
      1. boot animation stopped
      2. package manager answering
      3. keyguard dismissed and an activity (launcher/home) resumed
      4. CPU load average back down
      5. a short fixed pause as a final margin
    Each step has its own timeout and never aborts the run.
    """
    print("Waiting for the device to settle after boot...")

    _wait_until(
        "boot animation stopped",
        lambda: _shell("getprop", "init.svc.bootanim") == "stopped",
        SETTLE_STEP_TIMEOUT_SEC,
    )
    _wait_until(
        "package manager responding",
        lambda: _shell("pm", "path", "android").startswith("package:"),
        SETTLE_STEP_TIMEOUT_SEC,
    )

    # Dismiss the lock screen if present (no-ops on an already-unlocked device)
    _adb("shell", "wm", "dismiss-keyguard")
    _adb("shell", "input", "keyevent", "82")  # KEYCODE_MENU

    _wait_until("an activity is resumed (launcher/home)", _activity_resumed, SETTLE_STEP_TIMEOUT_SEC)

    try:
        cores = int(_shell("nproc") or "2")
    except ValueError:
        cores = 2
    threshold = float(SETTLE_LOAD_THRESHOLD) if SETTLE_LOAD_THRESHOLD else max(1.0, cores * 0.75)
    _wait_until(
        f"load average below {threshold:.1f}",
        lambda: _load_is_low(threshold),
        SETTLE_STEP_TIMEOUT_SEC,
        interval=3,
    )

    time.sleep(SETTLE_PAUSE_SEC)


def reset_anr_baseline():
    """
    Report ANRs that happened during boot, then clear the events log so any
    am_anr evidence collected after a test failure only covers the test period.
    """
    try:
        events = _adb("logcat", "-b", "events", "-d").stdout
        boot_anrs = [line for line in events.splitlines() if "am_anr" in line]
        print(f"Boot-time ANR events before tests: {len(boot_anrs)}")
        for line in boot_anrs[-3:]:
            print(f"  {line}")
        _adb("logcat", "-b", "events", "-c")
    except Exception as e:
        print(f"Could not reset ANR baseline: {e}")


def prepare_device():
    """
    Pre-session device setup using plain adb (no Appium server flags needed):
      - wait for the device and for a full boot
      - wait for the system to settle (boot animation, package manager,
        launcher resumed, CPU load) so tests don't start during boot-time ANRs
      - disable animations
      - hide crash/ANR dialogs (a mitigation, not a guarantee; the BasePage
        ANR handler remains the safety net)
    """
    print("\n============================================================")
    print("PREPARING DEVICE")
    print("============================================================")

    try:
        _adb("wait-for-device", timeout=BOOT_TIMEOUT_SEC)

        deadline = time.monotonic() + BOOT_TIMEOUT_SEC
        while time.monotonic() < deadline:
            booted = _adb("shell", "getprop", "sys.boot_completed").stdout.strip()
            if booted == "1":
                break
            time.sleep(2)
        else:
            print(f"Device not fully booted after {BOOT_TIMEOUT_SEC}s; continuing anyway.")

        wait_until_settled()

        for key in (
            "window_animation_scale",
            "transition_animation_scale",
            "animator_duration_scale",
        ):
            _adb("shell", "settings", "put", "global", key, "0")

        result = _adb("shell", "settings", "put", "global", "hide_error_dialogs", "1")
        if result.returncode != 0:
            print(f"Could not set hide_error_dialogs: {result.stderr.strip()}")
        else:
            print("Animations disabled, error dialogs hidden.")

        reset_anr_baseline()

    except Exception as e:
        print(f"Device preparation failed (continuing): {e}")


def force_stop_app():
    print("\n============================================================")
    print("ADB APP CLEANUP")
    print("============================================================")

    try:
        result = _adb("devices")
        print("ADB devices:")
        print(result.stdout)

        if result.returncode != 0:
            print(f"ADB devices failed: {result.stderr}")
            return

        print(f"Force-stopping: {APP_PACKAGE}")
        result = _adb("shell", "am", "force-stop", APP_PACKAGE)

        if result.returncode == 0:
            print("ADB force-stop completed successfully.")
        else:
            print(f"ADB force-stop FAILED (return code {result.returncode})")
            if result.stderr:
                print(f"ADB error: {result.stderr}")

    except Exception as e:
        print(f"ADB cleanup exception: {e}")


# ============================================================================
# FAILURE EVIDENCE (ANR diagnostics)
# ============================================================================

def _collect_failure_evidence(item, when):
    """
    On failure: save ANR entries from the events log, a screenshot and the page source.
    Returns (list of saved file paths, number of am_anr events) so the email alert
    can attach the files and mention ANRs.
    """
    saved = []
    anr_count = 0
    try:
        os.makedirs(ARTIFACTS_DIR, exist_ok=True)
        stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        base = os.path.join(ARTIFACTS_DIR, f"{item.name}_{when}_{stamp}")

        # am_anr events show which process hung and when
        try:
            events = _adb("logcat", "-b", "events", "-d", "-t", "1000").stdout
            anr_lines = [line for line in events.splitlines() if "am_anr" in line]
            if anr_lines:
                anr_count = len(anr_lines)
                with open(f"{base}_anr.log", "w") as f:
                    f.write("\n".join(anr_lines))
                saved.append(f"{base}_anr.log")
                print(f"\n[ANR] {len(anr_lines)} am_anr event(s) found, saved to {base}_anr.log")
                print("\n".join(anr_lines[-3:]))
        except Exception as e:
            print(f"Could not collect logcat events: {e}")

        driver = item.funcargs.get("driver") if hasattr(item, "funcargs") else None
        if driver is not None:
            try:
                driver.save_screenshot(f"{base}.png")
                saved.append(f"{base}.png")
            except Exception as e:
                print(f"Could not save screenshot: {e}")
            try:
                with open(f"{base}_source.xml", "w", encoding="utf-8") as f:
                    f.write(driver.page_source)
                saved.append(f"{base}_source.xml")
            except Exception as e:
                print(f"Could not save page source: {e}")

    except Exception as e:
        print(f"Failure evidence collection error: {e}")

    return saved, anr_count


# ============================================================================
# EMAIL ALERTS
# ============================================================================

def _record_failure(item, report, evidence=None, anr_count=0):
    """Remember a failure; the first one of the run triggers the email alert immediately."""
    failure = {
        "file": os.path.basename(item.nodeid.split("::")[0]),
        "test": item.name,
        "name": item.nodeid,
        "phase": report.when,
        "error": (report.longreprtext or "")[-1500:],  # trim very long tracebacks
        "files": list(evidence or []),
        "anr_count": anr_count,
    }
    _failures.append(failure)

    if not _alert_sent:
        prefix = f"❌ [{ALERT_LABEL}]"
        headline = f"{prefix} {failure['file']} - First Test Failure: {failure['test']}"
        _send_alert(headline, failure=failure)


def _build_attachments(paths):
    """
    Base64-encode evidence files for the Resend API, skipping missing/oversized
    ones and respecting the per-file, count and total-size limits.
    """
    max_file = int(ALERT_MAX_ATTACHMENT_MB * 1024 * 1024)
    max_total = int(ALERT_MAX_TOTAL_MB * 1024 * 1024)
    total = 0
    attachments = []
    for path in paths:
        if len(attachments) >= ALERT_MAX_ATTACHMENTS:
            break
        try:
            if not os.path.isfile(path):
                continue
            size = os.path.getsize(path)
            if size > max_file or total + size > max_total:
                continue
            with open(path, "rb") as f:
                content = base64.b64encode(f.read()).decode("ascii")
            attachments.append({"filename": os.path.basename(path), "content": content})
            total += size
        except Exception as e:
            print(f"Could not attach {path}: {e}")
    return attachments


def _send_email(subject, body, attachments=()):
    """Send via Resend's HTTP API (https://resend.com/docs/api-reference/emails/send-email)."""
    payload = {
        "from": ALERT_FROM,
        "to": ALERT_TO,
        "subject": subject,
        "text": body,
    }
    files = _build_attachments(attachments)
    if files:
        payload["attachments"] = files

    req = urllib.request.Request(
        RESEND_API_URL,
        data=json.dumps(payload).encode("utf-8"),
        method="POST",
        headers={
            "Authorization": f"Bearer {RESEND_API_KEY}",
            "Content-Type": "application/json",
            # Resend sits behind Cloudflare, which can reject urllib's default User-Agent
            "User-Agent": "pytest-appium-alerts/1.0",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8") or "{}")
    except urllib.error.HTTPError as e:
        # Surface Resend's error message (bad API key, unverified domain, etc.)
        detail = e.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Resend API returned HTTP {e.code}: {detail}") from e


def _send_alert(headline, failure=None, abort_reason=None, exitstatus=None):
    """Send the one alert email for this run. Never raises, never changes the test result."""
    global _alert_sent

    if not (RESEND_API_KEY and ALERT_FROM and ALERT_TO):
        print("Email alert skipped: RESEND_API_KEY / ALERT_FROM / ALERT_TO not set")
        return

    _alert_sent = True  # set before sending: a failed send is not retried for later failures

    job = os.getenv("JOB_NAME", "local run")
    build_number = os.getenv("BUILD_NUMBER")
    build_url = os.getenv("BUILD_URL", "n/a")  # set by Jenkins

    lines = [
        headline,
        "",
        f"Job:      {job}",
        f"Build:    {f'#{build_number} ' if build_number else ''}{build_url}",
        f"Host:     {socket.gethostname()}",
        f"Device:   {DEVICE_SERIAL or 'default'}",
        f"App:      {APP_PACKAGE}",
        f"Time:     {datetime.now():%Y-%m-%d %H:%M:%S}",
    ]
    if exitstatus is not None:
        lines.append(f"Exit:     {int(exitstatus)}")
    if failure and failure["anr_count"]:
        lines.append(f"ANRs:     {failure['anr_count']} am_anr event(s) seen at failure time (see attached logs)")
    if abort_reason:
        lines += ["", f"Run aborted: {abort_reason}"]
    lines.append("")

    attachments = []
    if failure:
        lines += [f"FAILED ({failure['phase']}): {failure['name']}", failure["error"], "-" * 60]
        lines += ["", "Note: only the first failure of a run triggers an alert; later failures are not emailed."]
        attachments = failure["files"]

    try:
        _send_email(subject=headline, body="\n".join(lines), attachments=attachments)
        print(f"Alert email sent to: {', '.join(ALERT_TO)}")
    except Exception as e:
        print(f"Failed to send alert email: {e}")


def pytest_sessionfinish(session, exitstatus):
    """
    Safety net: if the run ended abnormally (session died, collection error, etc.)
    without any test failure having already triggered an alert, send one now.
    """
    # With pytest-xdist, only the controller should send, not every worker
    if hasattr(session.config, "workerinput"):
        return
    if _alert_sent:
        return

    abnormal_exit = int(exitstatus) not in (0, 1)  # 1 = tests failed (alert already sent)
    if not (_abort_reason or abnormal_exit):
        return

    prefix = f"❌ [{ALERT_LABEL}]"
    if _abort_reason:
        headline = f"{prefix} Run Aborted - {_abort_reason}"
    else:
        headline = f"{prefix} Run Ended Abnormally (exit code {int(exitstatus)})"
    _send_alert(headline, abort_reason=_abort_reason, exitstatus=exitstatus)


# ============================================================================
# REPORTING HOOK
# ============================================================================

def _store(test_name, transaction, status, duration, timestamp):
    """Never let a DB problem fail the test run."""
    try:
        store_transaction_result(
            test_name=test_name,
            transaction=transaction,
            status=status,
            duration=duration,
            timestamp=timestamp,
        )
    except Exception as e:
        print(f"Could not store result for {test_name}: {e}")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    current_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    test_name = item.name

    if report.when == "setup" and report.failed:
        evidence, anrs = _collect_failure_evidence(item, "setup")
        _record_failure(item, report, evidence, anrs)
        _store(test_name, "N/A", "FAIL", "N/A", current_timestamp)

    elif report.when == "call":
        if report.failed:
            evidence, anrs = _collect_failure_evidence(item, "call")
            _record_failure(item, report, evidence, anrs)

        if report.passed:
            status = "PASS"
        elif report.skipped:
            status = "SKIP"
        else:
            status = "FAIL"

        duration = f"{report.duration:.2f}s"
        transaction = getattr(item, "transaction_name", "Execution")

        _store(test_name, transaction, status, duration, current_timestamp)

    elif report.when == "teardown" and report.failed:
        # e.g. the session-scoped driver fixture failing during final cleanup
        _record_failure(item, report)


# ============================================================================
# APPIUM DRIVER
# ============================================================================

@pytest.fixture(scope="session")
def driver():
    driver = None

    try:
        prepare_device()

        print("\n============================================================")
        print("STARTING APPIUM DRIVER")
        print("============================================================")

        driver = create_android_driver()

        print("Appium driver started.")

        yield driver

    finally:
        print("\n============================================================")
        print("STARTING TEST CLEANUP")
        print("============================================================")

        # 1. Try Appium terminate_app(); fall back to direct adb force-stop
        terminated = False
        if driver is not None:
            try:
                print("Attempting Appium terminate_app()...")
                driver.terminate_app(APP_PACKAGE)
                terminated = True
                print("Appium terminate_app() completed.")
            except Exception as e:
                print(f"Appium terminate_app() failed: {e}")

        if not terminated:
            force_stop_app()

        # 2. Quit Appium
        if driver is not None:
            try:
                print("Closing Appium session...")
                driver.quit()
                print("Appium session closed successfully.")
            except Exception as e:
                print(f"Appium driver.quit() failed: {e}")

        print("\n============================================================")
        print("TEST CLEANUP COMPLETED")
        print("============================================================")


@pytest.fixture(autouse=True)
def session_health(driver):
    """
    Fail fast if the shared session died (e.g. UiAutomator2 crashed after an ANR)
    instead of burning through the remaining tests with confusing errors.
    """
    global _abort_reason
    try:
        driver.current_activity  # cheap call; raises if the session is dead
    except Exception:
        # Recorded so the end-of-session email explains why the run stopped early
        _abort_reason = "Appium session died (likely ANR / UiAutomator2 crash)"
        pytest.exit(
            "Appium session is dead (likely ANR / UiAutomator2 crash). "
            "Check the saved am_anr log in the artifacts directory.",
            returncode=3,
        )