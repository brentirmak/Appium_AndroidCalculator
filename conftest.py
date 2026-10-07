import os
import subprocess
import time
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


def prepare_device():
    """
    Pre-session device setup using plain adb (no Appium server flags needed):
      - wait for the device and for a full boot
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
    """On failure: save ANR entries from the events log, a screenshot and the page source."""
    try:
        os.makedirs(ARTIFACTS_DIR, exist_ok=True)
        stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        base = os.path.join(ARTIFACTS_DIR, f"{item.name}_{when}_{stamp}")

        # am_anr events show which process hung and when
        try:
            events = _adb("logcat", "-b", "events", "-d", "-t", "1000").stdout
            anr_lines = [line for line in events.splitlines() if "am_anr" in line]
            if anr_lines:
                with open(f"{base}_anr.log", "w") as f:
                    f.write("\n".join(anr_lines))
                print(f"\n[ANR] {len(anr_lines)} am_anr event(s) found, saved to {base}_anr.log")
                print("\n".join(anr_lines[-3:]))
        except Exception as e:
            print(f"Could not collect logcat events: {e}")

        driver = item.funcargs.get("driver") if hasattr(item, "funcargs") else None
        if driver is not None:
            try:
                driver.save_screenshot(f"{base}.png")
            except Exception as e:
                print(f"Could not save screenshot: {e}")
            try:
                with open(f"{base}_source.xml", "w", encoding="utf-8") as f:
                    f.write(driver.page_source)
            except Exception as e:
                print(f"Could not save page source: {e}")

    except Exception as e:
        print(f"Failure evidence collection error: {e}")


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
        _collect_failure_evidence(item, "setup")
        _store(test_name, "N/A", "FAIL", "N/A", current_timestamp)

    elif report.when == "call":
        if report.failed:
            _collect_failure_evidence(item, "call")

        if report.passed:
            status = "PASS"
        elif report.skipped:
            status = "SKIP"
        else:
            status = "FAIL"

        duration = f"{report.duration:.2f}s"
        transaction = getattr(item, "transaction_name", "Execution")

        _store(test_name, transaction, status, duration, current_timestamp)


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
    try:
        driver.current_activity  # cheap call; raises if the session is dead
    except Exception:
        pytest.exit(
            "Appium session is dead (likely ANR / UiAutomator2 crash). "
            "Check the saved am_anr log in the artifacts directory.",
            returncode=3,
        )