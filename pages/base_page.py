import inspect
import logging
import os
import time
from functools import wraps

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    ElementNotInteractableException,
    NoSuchElementException,
    StaleElementReferenceException,
    TimeoutException,
    WebDriverException,
)
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

log = logging.getLogger(__name__)

# Scaling short waits under CI environments
CI_FACTOR = 2 if os.getenv("JENKINS_URL") else 1
DEFAULT_TIMEOUT = int(os.getenv("DEFAULT_TIMEOUT", "45"))

# Implicit wait restored after ANR checks (0 = explicit waits only).
# Set IMPLICIT_WAIT if your driver_factory configures a non-zero value.
IMPLICIT_WAIT = int(os.getenv("IMPLICIT_WAIT", "0"))

# How often (seconds) long waits pause to look for an ANR dialog
ANR_CHECK_INTERVAL = int(os.getenv("ANR_CHECK_INTERVAL", "5"))

# After this many consecutive "Wait" clicks on the same dialog, click "Close app"
MAX_WAIT_CLICKS = int(os.getenv("ANR_MAX_WAIT_CLICKS", "3"))

# Transient errors safe for retry after UI recovery
TRANSIENT_ERRORS = (
    StaleElementReferenceException,
    ElementClickInterceptedException,
    ElementNotInteractableException,
)
NOT_FOUND_ERRORS = (TimeoutException, NoSuchElementException)

# ANR dialog locators. Verify the IDs on your API level with Appium Inspector.
ANR_WAIT_BTN = (AppiumBy.ID, "android:id/aerr_wait")
ANR_CLOSE_BTN = (AppiumBy.ID, "android:id/aerr_close")
ANR_TITLE = (
    AppiumBy.ANDROID_UIAUTOMATOR,
    'new UiSelector().resourceId("android:id/alertTitle").textContains("responding")',
)
# Text-based fallbacks, only used once the dialog title has been confirmed
ANR_WAIT_BTN_TEXT = (
    AppiumBy.ANDROID_UIAUTOMATOR,
    'new UiSelector().className("android.widget.Button").text("Wait")',
)
ANR_CLOSE_BTN_TEXT = (
    AppiumBy.ANDROID_UIAUTOMATOR,
    'new UiSelector().className("android.widget.Button").textMatches("(?i)Close app")',
)


def handle_anr_recovery(func):
    """
    Retries a BasePage action on transient UI errors after trying to dismiss
    any System UI / ANR dialog. Honors the wrapped method's own `retries`
    default (e.g. click(..., retries=2)) as well as a caller-supplied value.

    Timeouts are NOT retried here: BasePage._wait already checks for ANR
    dialogs while waiting, so retrying would only multiply the wait time.
    """
    sig = inspect.signature(func)

    @wraps(func)
    def wrapper(self, *args, **kwargs):
        bound = sig.bind(self, *args, **kwargs)
        bound.apply_defaults()
        retries = bound.arguments.get("retries", 1)

        for attempt in range(retries + 1):
            try:
                return func(self, *args, **kwargs)
            except TRANSIENT_ERRORS as exc:
                log.warning(
                    "%s() hit %s on attempt %d/%d - checking for System UI / ANR popups...",
                    func.__name__,
                    type(exc).__name__,
                    attempt + 1,
                    retries + 1,
                )
                if self.handle_system_anr():
                    time.sleep(0.5)  # let the UI hierarchy stabilize

                if attempt == retries:
                    raise
                time.sleep(0.5 * (attempt + 1))

    return wrapper


class BasePage:
    def __init__(self, driver, timeout=DEFAULT_TIMEOUT):
        self.driver = driver
        self.timeout = timeout
        self.wait = self._waiter(timeout)
        self._anr_wait_clicks = 0

    # ------------------------------------------------------------------
    # Scroll to Text
    # ------------------------------------------------------------------
    def scroll_to_text(self, text):
        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("{text}"))'
        )

    # ------------------------------------------------------------------
    # System Alert Handling
    # ------------------------------------------------------------------
    def _first_displayed(self, locator):
        """Return the first displayed element for locator, or None."""
        for el in self.driver.find_elements(*locator):
            try:
                if el.is_displayed():
                    return el
            except StaleElementReferenceException:
                continue
        return None

    def _anr_dialog_present(self) -> bool:
        return bool(
            self.driver.find_elements(*ANR_WAIT_BTN)
            or self.driver.find_elements(*ANR_CLOSE_BTN)
            or self.driver.find_elements(*ANR_TITLE)
        )

    def handle_system_anr(self) -> bool:
        """
        Dismisses an ANR dialog ("System UI isn't responding", "<app> isn't responding").

        Strategy:
          1. Click "Wait" (safe: keeps SystemUI / the app alive).
          2. If the same dialog keeps coming back (MAX_WAIT_CLICKS in a row),
             click "Close app" so the run can make progress.
          3. If the buttons can't be found but the title is visible, send BACK
             and only report success if the dialog is actually gone.

        Returns True only if a dialog was present and has been dismissed.
        """
        dismissed = False
        original_context = None

        try:
            # Switch to NATIVE_APP if currently inside a webview context
            current = self.driver.current_context
            if current != "NATIVE_APP":
                original_context = current
                self.driver.switch_to.context("NATIVE_APP")

            self.driver.implicitly_wait(0)

            if not self._anr_dialog_present():
                self._anr_wait_clicks = 0
                return False

            use_close = self._anr_wait_clicks >= MAX_WAIT_CLICKS
            if use_close:
                targets = (ANR_CLOSE_BTN, ANR_CLOSE_BTN_TEXT)
            else:
                targets = (ANR_WAIT_BTN, ANR_WAIT_BTN_TEXT)

            for locator in targets:
                btn = self._first_displayed(locator)
                if btn is not None:
                    log.warning(
                        "ANR dialog detected. Clicking '%s'%s...",
                        "Close app" if use_close else "Wait",
                        f" (after {self._anr_wait_clicks} 'Wait' clicks)" if use_close else "",
                    )
                    btn.click()
                    self._anr_wait_clicks = 0 if use_close else self._anr_wait_clicks + 1
                    dismissed = True
                    time.sleep(1)
                    break

            # Fallback: buttons not clickable but dialog is there -> BACK key
            if not dismissed:
                log.warning("ANR dialog found but buttons not clickable, sending BACK key...")
                self.driver.press_keycode(4)  # KEYCODE_BACK
                time.sleep(1)
                dismissed = not self._anr_dialog_present()
                if not dismissed:
                    log.error("BACK key did not dismiss the ANR dialog.")

        except Exception as exc:
            log.debug("Exception during ANR dismissal: %s", exc)
        finally:
            if original_context:
                try:
                    self.driver.switch_to.context(original_context)
                except Exception:
                    pass
            try:
                self.driver.implicitly_wait(IMPLICIT_WAIT)
            except Exception:
                pass

        return dismissed

    # ------------------------------------------------------------------
    # Internals
    # ------------------------------------------------------------------
    def _waiter(self, timeout=None, poll=0.5):
        return WebDriverWait(
            self.driver,
            timeout or self.timeout,
            poll_frequency=poll,
            ignored_exceptions=(StaleElementReferenceException,),
        )

    def _wait(self, condition, timeout=None, slice_=ANR_CHECK_INTERVAL):
        """
        Like WebDriverWait.until(), but pauses between short slices to look for
        (and dismiss) an ANR dialog, so a popup is handled within seconds rather
        than after the full timeout. If a dialog is dismissed right at the
        deadline, one extra slice is granted.
        """
        total = timeout or self.timeout
        deadline = time.monotonic() + total
        extended = False

        while True:
            remaining = deadline - time.monotonic()
            try:
                return self._waiter(max(1, min(slice_, remaining))).until(condition)
            except TimeoutException:
                dismissed = self.handle_system_anr()
                if time.monotonic() >= deadline:
                    if dismissed and not extended:
                        deadline = time.monotonic() + slice_
                        extended = True
                        continue
                    raise

    def _bool_wait(self, condition, timeout):
        """Boolean wrapper used by exists/wait_for/visible."""
        try:
            self._wait(condition, timeout * CI_FACTOR)
            return True
        except NOT_FOUND_ERRORS:
            return False

    # ------------------------------------------------------------------
    # Finding
    # ------------------------------------------------------------------
    @handle_anr_recovery
    def find(self, locator, timeout=None, retries=1):
        return self._wait(EC.presence_of_element_located(locator), timeout)

    @handle_anr_recovery
    def find_visible(self, locator, timeout=None, retries=1):
        return self._wait(EC.visibility_of_element_located(locator), timeout)

    # ------------------------------------------------------------------
    # Actions
    # ------------------------------------------------------------------
    @handle_anr_recovery
    def click(self, locator, timeout=None, retries=2):
        try:
            self._wait(EC.element_to_be_clickable(locator), timeout).click()
        except ElementClickInterceptedException:
            # Fallback coordinate tap if System UI or a transparent overlay blocks the click
            element = self._wait(EC.visibility_of_element_located(locator), 3)
            x = element.location["x"] + element.size["width"] // 2
            y = element.location["y"] + element.size["height"] // 2
            # driver.tap() was removed in newer Appium-Python-Client versions
            self.driver.execute_script("mobile: clickGesture", {"x": x, "y": y})

    @handle_anr_recovery
    def type(self, locator, text, clear=True, timeout=None, retries=2):
        element = self._wait(EC.visibility_of_element_located(locator), timeout)
        if clear:
            element.clear()
        element.send_keys(text)

    @handle_anr_recovery
    def get_text(self, locator, timeout=None, retries=2):
        return self._wait(EC.visibility_of_element_located(locator), timeout).text

    def hide_keyboard_if_shown(self):
        try:
            if self.driver.is_keyboard_shown():
                self.driver.hide_keyboard()
        except WebDriverException:
            pass

    # ------------------------------------------------------------------
    # Boolean Checks
    # ------------------------------------------------------------------
    def exists(self, locator, timeout=3):
        return self._bool_wait(EC.presence_of_element_located(locator), timeout)

    def wait_for(self, locator, timeout=30):
        return self._bool_wait(EC.presence_of_element_located(locator), timeout)

    def visible(self, locator, timeout=10):
        return self._bool_wait(EC.visibility_of_element_located(locator), timeout)

    def safe_click(self, locator, timeout=20):
        # click() already runs ANR recovery and retries
        try:
            self.click(locator, timeout=timeout * CI_FACTOR)
            return True
        except (*NOT_FOUND_ERRORS, *TRANSIENT_ERRORS):
            return False

    # ------------------------------------------------------------------
    # Asserting Waits
    # ------------------------------------------------------------------
    def wait_visible(self, locator, timeout=None):
        return self.find_visible(locator, timeout)

    def wait_invisible(self, locator, timeout=None):
        return self._wait(EC.invisibility_of_element_located(locator), timeout)

    @handle_anr_recovery
    def wait_for_text_contains(self, locator, expected, timeout=None, retries=1):
        def _check(driver):
            return expected in driver.find_element(*locator).text

        return self._wait(_check, timeout)

    @handle_anr_recovery
    def wait_for_any(self, locators, timeout=None, retries=1):
        def _check(driver):
            for loc in locators:
                try:
                    if driver.find_element(*loc).is_displayed():
                        return loc
                except (NoSuchElementException, StaleElementReferenceException):
                    pass
            return False

        return self._wait(_check, timeout)