import logging
import os
import shutil
import subprocess
import time
import urllib.error
import urllib.request

from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.common.exceptions import WebDriverException
from urllib3.exceptions import HTTPError as Urllib3Error

log = logging.getLogger(__name__)

# =============================================================================
# CONFIG (everything overridable from the Jenkins job via env vars)
#
# Jenkins runs on Ubuntu, the Android emulator runs on Windows. Linux ADB
# connects straight to the Windows-side emulator over TCP, so do NOT use
# emulator-5554 or 127.0.0.1:5555 (those are the Windows-local transport).
# =============================================================================
APPIUM_URL = os.getenv("APPIUM_URL", "http://127.0.0.1:4723")
ANDROID_SERIAL = os.getenv("ANDROID_SERIAL", "192.168.150.1:5555")
DEVICE_NAME = os.getenv("DEVICE_NAME", "Tunneled-Pixel10")

APP_PACKAGE = "calculator.currencyconverter.tipcalculator.unitconverter"
APP_ACTIVITY = f"{APP_PACKAGE}.ui.splash.SplashActivity"

# UiAutomator2 waits for the UI to go "idle" before each command (default 10s).
# Ad-heavy apps with constant animation can burn that whole wait on every call.
# 0 disables it; the page objects use explicit waits instead.
WAIT_FOR_IDLE_MS = int(os.getenv("WAIT_FOR_IDLE_MS", "0"))

APPIUM_PACKAGES = (
    "io.appium.settings",
    "io.appium.uiautomator2.server",
    "io.appium.uiautomator2.server.test",
)


# =============================================================================
# ADB HELPERS
# =============================================================================
def _adb_path():
    """The jenkins user often has a different PATH than your shell."""
    found = shutil.which("adb")
    if found:
        return found
    sdk = os.getenv("ANDROID_HOME") or os.getenv("ANDROID_SDK_ROOT")
    if sdk:
        candidate = os.path.join(sdk, "platform-tools", "adb")
        if os.path.exists(candidate):
            return candidate
    return "adb"


def _adb(serial, *args, timeout=30):
    """Run an adb command. Returns CompletedProcess, or None if it timed out."""
    cmd = [_adb_path()]
    if serial:
        cmd += ["-s", serial]
    cmd += list(args)
    try:
        return subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
    except subprocess.TimeoutExpired:
        log.warning("adb %s timed out after %ss", " ".join(args), timeout)
        return None


def _reconnect_device(serial):
    """A tunnelled ADB-over-TCP device commonly drops to 'offline'; re-establish the link."""
    if ":" not in serial:
        return  # not a TCP device
    _adb(None, "disconnect", serial, timeout=15)
    result = _adb(None, "connect", serial, timeout=30)
    if result:
        log.info("adb connect %s: %s", serial, (result.stdout or result.stderr).strip())


def _wait_for_device_ready(serial, timeout=180):
    """
    Block until the device is genuinely usable: adb state is 'device', boot has
    completed, and the package manager answers. (sys.boot_completed alone can
    report 1 before the package manager is responsive.)
    """
    deadline = time.monotonic() + timeout
    last_reconnect = 0.0
    while time.monotonic() < deadline:
        state = _adb(serial, "get-state", timeout=10)
        if state and state.stdout.strip() == "device":
            boot = _adb(serial, "shell", "getprop", "sys.boot_completed", timeout=10)
            if boot and boot.stdout.strip() == "1":
                pm = _adb(serial, "shell", "pm", "path", "android", timeout=20)
                if pm and pm.returncode == 0 and "package:" in pm.stdout:
                    log.info("Device %s is ready", serial)
                    return
        elif time.monotonic() - last_reconnect > 15:
            _reconnect_device(serial)
            last_reconnect = time.monotonic()
        time.sleep(2)
    raise RuntimeError(f"Device {serial} was not ready after {timeout}s")


def _prepare_device(serial):
    """Per-run device prep: no animations, app starts from a fresh process, log memory headroom."""
    for key in ("window_animation_scale", "transition_animation_scale", "animator_duration_scale"):
        _adb(serial, "shell", "settings", "put", "global", key, "0", timeout=15)

    # Start each session from a fresh app process (data is kept because noReset=True)
    _adb(serial, "shell", "am", "force-stop", APP_PACKAGE, timeout=15)

    # Useful when io.appium.settings gets low-memory killed: see how much headroom the device had
    mem = _adb(serial, "shell", "grep", "MemAvailable", "/proc/meminfo", timeout=15)
    if mem and mem.stdout.strip():
        log.info("Device memory: %s", mem.stdout.strip())


def _clean_appium_packages(serial):
    """
    Remove stale/crashed io.appium.settings and UiAutomator2 server installs so a
    retry gets fresh ones (avoids 'Appium Settings app is not running after 5000ms').
    Only called after a failed attempt so the happy path pays no uninstall cost.
    """
    for pkg in APPIUM_PACKAGES:
        _adb(serial, "uninstall", pkg, timeout=30)


def _recover_device(serial):
    """Everything worth doing between a failed session attempt and the next one."""
    _reconnect_device(serial)
    _adb(serial, "shell", "am", "force-stop", APP_PACKAGE, timeout=15)
    _clean_appium_packages(serial)
    _wait_for_device_ready(serial, timeout=90)


# =============================================================================
# APPIUM SERVER
# =============================================================================
def _wait_for_appium_server(url, timeout=60):
    """Fail fast with a clear message if Appium isn't up, instead of a cryptic session error."""
    status_url = url.rstrip("/") + "/status"
    # Bypass any http(s)_proxy set in the Jenkins environment: this is a localhost call
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        try:
            with opener.open(status_url, timeout=5) as resp:
                if resp.status == 200:
                    log.info("Appium server is up at %s", url)
                    return
        except (urllib.error.URLError, OSError):
            pass
        time.sleep(1)
    raise RuntimeError(f"Appium server not responding at {status_url} after {timeout}s")


# =============================================================================
# CAPABILITIES
# =============================================================================
def _build_options(serial):
    options = UiAutomator2Options()

    # --- Platform / automation ------------------------------------------------
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.set_capability("appium:udid", serial)
    options.set_capability("appium:deviceName", DEVICE_NAME)

    # --- Application -----------------------------------------------------------
    options.app_package = APP_PACKAGE
    options.app_activity = APP_ACTIVITY
    # Allow the app to move from SplashActivity to whatever activity comes next
    options.set_capability("appium:appWaitActivity", "*")
    # NOTE: with this False, the session starts before the app is guaranteed to be
    # past the splash screen. Tests must therefore wait for a real landing-page
    # element (HomePage.load_landing_page) rather than assuming it is there.
    options.set_capability("appium:appWaitForLaunch", False)

    # --- State / permissions ---------------------------------------------------
    options.auto_grant_permissions = True
    options.no_reset = True  # app is already installed on the device

    # --- Jenkins / slow-emulator timeouts (ms unless noted) ---------------------
    # NOTE: "appium:appiumSettingsStartupTimeout" is not a recognised UiAutomator2
    # capability (Appium ignores unknown caps silently), so it is intentionally
    # absent. The 5000ms Settings-app check is hard-coded in the driver; the
    # retry + cleanup logic below is the real mitigation.
    options.set_capability("appium:adbExecTimeout", 300000)
    options.set_capability("appium:appWaitDuration", 120000)
    options.set_capability("appium:uiautomator2ServerLaunchTimeout", 300000)
    options.set_capability("appium:uiautomator2ServerInstallTimeout", 300000)
    options.set_capability("appium:androidInstallTimeout", 300000)
    options.set_capability("appium:newCommandTimeout", 300)  # seconds

    # --- Performance / stability -------------------------------------------------
    options.set_capability("appium:disableWindowAnimation", True)
    options.set_capability("appium:ignoreHiddenApiPolicyError", True)
    options.set_capability("appium:settings[waitForIdleTimeout]", WAIT_FOR_IDLE_MS)

    return options


# =============================================================================
# SESSION CREATION
# =============================================================================
def create_android_driver(retries: int = 2, backoff_seconds: int = 5):
    log.info(
        "Driver config: udid=%s name=%s package=%s server=%s waitForIdle=%sms",
        ANDROID_SERIAL, DEVICE_NAME, APP_PACKAGE, APPIUM_URL, WAIT_FOR_IDLE_MS,
    )

    # Pre-flight: make sure the stack is actually ready before asking Appium for a session
    _wait_for_appium_server(APPIUM_URL)
    _wait_for_device_ready(ANDROID_SERIAL)
    _prepare_device(ANDROID_SERIAL)

    options = _build_options(ANDROID_SERIAL)

    last_exc = None
    for attempt in range(1, retries + 2):
        try:
            return webdriver.Remote(command_executor=APPIUM_URL, options=options)
        except (WebDriverException, Urllib3Error, ConnectionError) as exc:
            last_exc = exc
            log.warning(
                "Session creation failed (attempt %d/%d): %s",
                attempt, retries + 1, str(exc).splitlines()[0] if str(exc) else type(exc).__name__,
            )
            if attempt <= retries:
                _recover_device(ANDROID_SERIAL)
                time.sleep(backoff_seconds * attempt)  # linear backoff

    raise last_exc