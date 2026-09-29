import logging
import os
import time

from selenium.common.exceptions import (
    ElementClickInterceptedException,
    ElementNotInteractableException,
    NoSuchElementException,
    StaleElementReferenceException,
    TimeoutException,
    WebDriverException,
)
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

log = logging.getLogger(__name__)

# Short "is it there?" waits double automatically under Jenkins.
# The main wait (DEFAULT_TIMEOUT) is already generous, so it is not scaled.
CI_FACTOR = 2 if os.getenv("JENKINS_URL") else 1
DEFAULT_TIMEOUT = int(os.getenv("DEFAULT_TIMEOUT", "45"))

# Errors that usually mean "the UI moved under us" - safe to re-find and retry.
TRANSIENT_ERRORS = (
    StaleElementReferenceException,
    ElementClickInterceptedException,
    ElementNotInteractableException,
)
# "Not found / not in time" outcomes for the boolean helpers.
NOT_FOUND_ERRORS = (TimeoutException, NoSuchElementException)

# Locators for system dialogs/ANRs
ANR_BUTTON_LOCATOR = (
    By.XPATH,
    "//*[@text='Wait' or @text='WAIT' or @text='Close app' or @text='CLOSE APP' or @text='Process system']",
)


class BasePage:
    def __init__(self, driver, timeout=DEFAULT_TIMEOUT):
        self.driver = driver
        self.timeout = timeout
        # Kept for backward compatibility with page objects that use self.wait directly
        self.wait = self._waiter(timeout)

    # ------------------------------------------------------------------
    # System Alert Handling
    # ------------------------------------------------------------------
    def handle_system_anr(self):
        """Best-effort check to dismiss 'System UI isn't responding' / ANR pop-ups."""
        try:
            # Temporarily drop implicit wait to 0 so we don't stall if the dialog isn't present
            self.driver.implicitly_wait(0)
            elements = self.driver.find_elements(*ANR_BUTTON_LOCATOR)
            if elements:
                log.warning("System UI / ANR dialog detected. Dismissing pop-up...")
                elements[0].click()
                time.sleep(1)  # Brief pause to let system UI stabilize
        except WebDriverException as exc:
            log.debug("Failed to check/dismiss ANR dialog: %s", exc)

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
    def find(self, locator, timeout=None):
        try:
            return self._waiter(timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            self.handle_system_anr()
            return self._waiter(timeout).until(EC.presence_of_element_located(locator))

    def find_visible(self, locator, timeout=None):
        try:
            return self._waiter(timeout).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            self.handle_system_anr()
            return self._waiter(timeout).until(EC.visibility_of_element_located(locator))

    # ------------------------------------------------------------------
    # Actions (re-find on every attempt, retry only on transient errors)
    # ------------------------------------------------------------------
    def click(self, locator, timeout=None, retries=2):
        last_exc = None
        for attempt in range(retries + 1):
            try:
                self._waiter(timeout).until(EC.element_to_be_clickable(locator)).click()
                return
            except (*TRANSIENT_ERRORS, TimeoutException) as exc:
                last_exc = exc
                log.warning(
                    "click(%s) attempt %d hit %s - checking for ANR dialog...",
                    locator,
                    attempt + 1,
                    type(exc).__name__,
                )
                self.handle_system_anr()
                time.sleep(0.5 * (attempt + 1))
        raise last_exc

    def type(self, locator, text, clear=True, timeout=None, retries=2):
        last_exc = None
        for attempt in range(retries + 1):
            try:
                element = self.find_visible(locator, timeout)
                if clear:
                    element.clear()
                element.send_keys(text)
                return
            except (*TRANSIENT_ERRORS, TimeoutException) as exc:
                last_exc = exc
                log.warning(
                    "type(%s) attempt %d hit %s - checking for ANR dialog...",
                    locator,
                    attempt + 1,
                    type(exc).__name__,
                )
                self.handle_system_anr()
                time.sleep(0.5 * (attempt + 1))
        raise last_exc

    def get_text(self, locator, timeout=None, retries=2):
        """Read text without tripping over an element that goes stale between find and read."""
        last_exc = None
        for attempt in range(retries + 1):
            try:
                return self.find_visible(locator, timeout).text
            except (StaleElementReferenceException, TimeoutException) as exc:
                last_exc = exc
                self.handle_system_anr()
                time.sleep(0.3)
        raise last_exc

    def hide_keyboard_if_shown(self):
        try:
            if self.driver.is_keyboard_shown():
                self.driver.hide_keyboard()
        except WebDriverException:
            pass  # best-effort only

    # ------------------------------------------------------------------
    # Boolean checks (never raise for "not found"; DO raise for real problems
    # such as a dead session, so failures are not silently turned into False)
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
        """Returns True/False. NOTE: this does not fail a test by itself - use assert or wait_visible."""
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
    # Asserting waits (raise TimeoutException with the locator in the message)
    # ------------------------------------------------------------------
    def wait_visible(self, locator, timeout=None):
        return self.find_visible(locator, timeout)

    def wait_invisible(self, locator, timeout=None):
        return self._waiter(timeout).until(EC.invisibility_of_element_located(locator))

    def wait_for_text_contains(self, locator, expected, timeout=None):
        def _check(driver):
            return expected in driver.find_element(*locator).text
        return self._waiter(timeout).until(_check)

    def wait_for_any(self, locators, timeout=None):
        """Wait until any one locator is displayed; returns the locator that matched."""
        def _check(driver):
            for loc in locators:
                try:
                    if driver.find_element(*loc).is_displayed():
                        return loc
                except (NoSuchElementException, StaleElementReferenceException):
                    pass
            return False
        return self._waiter(timeout).until(_check)