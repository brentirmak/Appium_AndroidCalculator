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

# Transient errors safe for retry after UI recovery
TRANSIENT_ERRORS = (
    StaleElementReferenceException,
    ElementClickInterceptedException,
    ElementNotInteractableException,
)
NOT_FOUND_ERRORS = (TimeoutException, NoSuchElementException)

# Highly efficient UIAutomator selector matching standard Android System UI / ANR dialog buttons
ANR_BUTTON_LOCATOR = (
    AppiumBy.ANDROID_UIAUTOMATOR,
    'new UiSelector().textMatches("(?i)Close app|Wait|OK|Process system|Close")'
)


def handle_anr_recovery(func):
    """
    Decorator that intercepts transient errors / timeouts on BasePage methods,
    attempts to dismiss any System UI / ANR dialogs, and retries the operation.
    """

    @wraps(func)
    def wrapper(self, *args, **kwargs):
        retries = kwargs.get("retries", 1)
        last_exc = None
        for attempt in range(retries + 1):
            try:
                return func(self, *args, **kwargs)
            except (*TRANSIENT_ERRORS, TimeoutException) as exc:
                last_exc = exc
                log.warning(
                    "%s() hit %s on attempt %d/%d - checking for System UI / ANR popups...",
                    func.__name__,
                    type(exc).__name__,
                    attempt + 1,
                    retries + 1,
                )

                # Check and clear System UI dialog
                if self.handle_system_anr():
                    time.sleep(0.5)  # Pause to let Appium UI hierarchy stabilize

                if attempt == retries:
                    raise last_exc
                time.sleep(0.5 * (attempt + 1))

    return wrapper


class BasePage:
    def __init__(self, driver, timeout=DEFAULT_TIMEOUT):
        self.driver = driver
        self.timeout = timeout
        self.wait = self._waiter(timeout)

    # ------------------------------------------------------------------
    # System Alert Handling
    # ------------------------------------------------------------------
    def handle_system_anr(self) -> bool:
        """
        Best-effort check to dismiss 'System UI isn't responding' / ANR pop-ups.
        Returns True if a dialog was detected and dismissed, False otherwise.
        """
        dismissed = False
        try:
            # Drop implicit wait to 0 to avoid blocking when no dialog exists
            self.driver.implicitly_wait(0)
            elements = self.driver.find_elements(*ANR_BUTTON_LOCATOR)

            for element in elements:
                if element.is_displayed():
                    log.warning("System UI / ANR dialog detected. Dismissing pop-up...")
                    element.click()
                    dismissed = True
                    time.sleep(0.8)
                    break
        except WebDriverException as exc:
            log.debug("Failed during ANR dialog check: %s", exc)
        finally:
            self.driver.implicitly_wait(0)  # Maintain explicit-wait paradigm

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

    # ------------------------------------------------------------------
    # Finding
    # ------------------------------------------------------------------
    @handle_anr_recovery
    def find(self, locator, timeout=None, retries=1):
        return self._waiter(timeout).until(EC.presence_of_element_located(locator))

    @handle_anr_recovery
    def find_visible(self, locator, timeout=None, retries=1):
        return self._waiter(timeout).until(EC.visibility_of_element_located(locator))

    # ------------------------------------------------------------------
    # Actions
    # ------------------------------------------------------------------
    @handle_anr_recovery
    def click(self, locator, timeout=None, retries=2):
        try:
            self._waiter(timeout).until(EC.element_to_be_clickable(locator)).click()
        except ElementClickInterceptedException:
            # Fallback coordinate tap if System UI or transparent overlay blocks standard click
            element = self.find_visible(locator, timeout=3)
            self.driver.tap([(element.location['x'] + element.size['width'] // 2,
                              element.location['y'] + element.size['height'] // 2)])

    @handle_anr_recovery
    def type(self, locator, text, clear=True, timeout=None, retries=2):
        element = self.find_visible(locator, timeout)
        if clear:
            element.clear()
        element.send_keys(text)

    @handle_anr_recovery
    def get_text(self, locator, timeout=None, retries=2):
        return self.find_visible(locator, timeout).text

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
        try:
            self._waiter(timeout * CI_FACTOR).until(EC.presence_of_element_located(locator))
            return True
        except NOT_FOUND_ERRORS:
            self.handle_system_anr()
            return False

    def wait_for(self, locator, timeout=30):
        try:
            self._waiter(timeout * CI_FACTOR).until(EC.presence_of_element_located(locator))
            return True
        except NOT_FOUND_ERRORS:
            self.handle_system_anr()
            return False

    def visible(self, locator, timeout=10):
        try:
            self._waiter(timeout * CI_FACTOR).until(EC.visibility_of_element_located(locator))
            return True
        except NOT_FOUND_ERRORS:
            self.handle_system_anr()
            return False

    def safe_click(self, locator, timeout=20):
        try:
            self.click(locator, timeout=timeout * CI_FACTOR)
            return True
        except (*NOT_FOUND_ERRORS, *TRANSIENT_ERRORS):
            self.handle_system_anr()
            return False

    # ------------------------------------------------------------------
    # Asserting Waits
    # ------------------------------------------------------------------
    def wait_visible(self, locator, timeout=None):
        return self.find_visible(locator, timeout)

    def wait_invisible(self, locator, timeout=None):
        return self._waiter(timeout).until(EC.invisibility_of_element_located(locator))

    @handle_anr_recovery
    def wait_for_text_contains(self, locator, expected, timeout=None, retries=1):
        def _check(driver):
            return expected in driver.find_element(*locator).text

        return self._waiter(timeout).until(_check)

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

        return self._waiter(timeout).until(_check)