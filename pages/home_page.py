import os
import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import (
    NoSuchElementException,
    TimeoutException,
    StaleElementReferenceException,
    WebDriverException,
)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class HomePage(BasePage):
    """
    Page Object for the Android Calculator application's Home screen.

    This implementation is intentionally defensive because the application
    is running on a remote Android emulator accessed through:

        Linux Jenkins
            |
            +--> Windows host
                    |
                    +--> Android emulator
                            |
                            +--> Appium / UiAutomator2

    The Home screen is considered loaded when one or more reliable home-screen
    indicators can be located.
    """

    # ------------------------------------------------------------------
    # Timeouts
    # ------------------------------------------------------------------

    DEFAULT_TIMEOUT = 20
    SHORT_TIMEOUT = 5
    LONG_TIMEOUT = 30

    # ------------------------------------------------------------------
    # Common locators
    #
    # Keep these broad enough to tolerate Android/application UI changes.
    # The calculator application may expose text/content descriptions
    # differently depending on Android/Appium versions.
    # ------------------------------------------------------------------

    HOME_TEXT_LOCATORS = [
        (AppiumBy.ACCESSIBILITY_ID, "Calculator"),
        (AppiumBy.ACCESSIBILITY_ID, "Basic Calculator"),
        (AppiumBy.ACCESSIBILITY_ID, "Home"),
        (AppiumBy.XPATH, "//*[@text='Calculator']"),
        (AppiumBy.XPATH, "//*[@text='Basic Calculator']"),
        (AppiumBy.XPATH, "//*[@text='Home']"),
    ]

    MENU_BUTTON_LOCATORS = [
        (AppiumBy.ACCESSIBILITY_ID, "Open navigation drawer"),
        (AppiumBy.ACCESSIBILITY_ID, "Open menu"),
        (AppiumBy.ACCESSIBILITY_ID, "Menu"),
        (
            AppiumBy.XPATH,
            "//android.widget.ImageButton[contains(@content-desc,'navigation')]",
        ),
        (
            AppiumBy.XPATH,
            "//android.widget.ImageButton[contains(@content-desc,'menu')]",
        ),
    ]

    CALCULATOR_INDICATORS = [
        (
            AppiumBy.XPATH,
            "//*[contains(@text,'Calculator')]",
        ),
        (
            AppiumBy.XPATH,
            "//*[contains(@content-desc,'Calculator')]",
        ),
        (
            AppiumBy.XPATH,
            "//*[contains(@resource-id,'calculator')]",
        ),
    ]

    # ------------------------------------------------------------------
    # Constructor
    # ------------------------------------------------------------------

    def __init__(self, driver):
        super().__init__(driver)

        self.driver = driver

        # Allow Jenkins to override the timeout without changing code.
        try:
            self.timeout = int(
                os.getenv("APPIUM_HOME_PAGE_TIMEOUT", self.DEFAULT_TIMEOUT)
            )
        except (TypeError, ValueError):
            self.timeout = self.DEFAULT_TIMEOUT

        print(
            f"[HomePage] Initialized "
            f"(timeout={self.timeout}s)"
        )

    # ------------------------------------------------------------------
    # Logging helpers
    # ------------------------------------------------------------------

    @staticmethod
    def _describe_locator(locator):
        """
        Return a safe human-readable representation of a locator.
        """
        try:
            by, value = locator
            return f"{by}={value}"
        except Exception:
            return str(locator)

    def _log(self, message):
        """
        Consistent logging for Jenkins output.
        """
        print(f"[HomePage] {message}")

    # ------------------------------------------------------------------
    # Driver/session health
    # ------------------------------------------------------------------

    def _driver_is_alive(self):
        """
        Determine whether the Appium session is still usable.

        Returns:
            bool: True when the driver appears operational.
        """
        try:
            _ = self.driver.current_package
            return True
        except Exception as exc:
            self._log(
                f"Driver health check failed: "
                f"{type(exc).__name__}: {exc}"
            )
            return False

    # ------------------------------------------------------------------
    # Safe element lookup
    # ------------------------------------------------------------------

    def _find_element(self, locator, timeout=None):
        """
        Wait for and return an element.

        This method deliberately avoids allowing transient Appium/Selenium
        errors to immediately terminate the entire Home verification flow.
        """

        wait_time = timeout if timeout is not None else self.timeout

        try:
            return WebDriverWait(
                self.driver,
                wait_time,
                poll_frequency=0.5,
                ignored_exceptions=(
                    NoSuchElementException,
                    StaleElementReferenceException,
                ),
            ).until(
                EC.presence_of_element_located(locator)
            )

        except TimeoutException:
            return None

        except (
            StaleElementReferenceException,
            NoSuchElementException,
        ):
            return None

        except WebDriverException as exc:
            self._log(
                f"WebDriverException locating "
                f"{self._describe_locator(locator)}: {exc}"
            )
            return None

        except Exception as exc:
            self._log(
                f"Unexpected error locating "
                f"{self._describe_locator(locator)}: "
                f"{type(exc).__name__}: {exc}"
            )
            return None

    def _find_visible_element(self, locator, timeout=None):
        """
        Wait for and return a visible element.
        """

        wait_time = timeout if timeout is not None else self.timeout

        try:
            return WebDriverWait(
                self.driver,
                wait_time,
                poll_frequency=0.5,
                ignored_exceptions=(
                    NoSuchElementException,
                    StaleElementReferenceException,
                ),
            ).until(
                EC.visibility_of_element_located(locator)
            )

        except (
            TimeoutException,
            StaleElementReferenceException,
            NoSuchElementException,
        ):
            return None

        except WebDriverException as exc:
            self._log(
                f"WebDriverException locating visible element "
                f"{self._describe_locator(locator)}: {exc}"
            )
            return None

        except Exception as exc:
            self._log(
                f"Unexpected visible-element error: "
                f"{type(exc).__name__}: {exc}"
            )
            return None

    def _element_exists(self, locator, timeout=None):
        """
        Return True when an element exists.
        """

        element = self._find_element(
            locator,
            timeout=timeout if timeout is not None else self.SHORT_TIMEOUT,
        )

        return element is not None

    # ------------------------------------------------------------------
    # Generic locator utilities
    # ------------------------------------------------------------------

    def _try_locators(self, locators, timeout=None):
        """
        Try multiple locators and return the first matching element.

        Returns:
            WebElement or None
        """

        for locator in locators:
            description = self._describe_locator(locator)

            self._log(f"Trying locator: {description}")

            element = self._find_element(
                locator,
                timeout=timeout if timeout is not None else self.SHORT_TIMEOUT,
            )

            if element is not None:
                self._log(
                    f"Element found using: {description}"
                )
                return element

        return None

    def _try_visible_locators(self, locators, timeout=None):
        """
        Try multiple locators for a visible element.
        """

        for locator in locators:
            description = self._describe_locator(locator)

            self._log(
                f"Trying visible locator: {description}"
            )

            element = self._find_visible_element(
                locator,
                timeout=timeout if timeout is not None else self.SHORT_TIMEOUT,
            )

            if element is not None:
                self._log(
                    f"Visible element found using: {description}"
                )
                return element

        return None

    # ------------------------------------------------------------------
    # App/package information
    # ------------------------------------------------------------------

    def get_current_package(self):
        """
        Return the current Android package.

        Returns:
            str or None
        """

        try:
            package = self.driver.current_package

            self._log(
                f"Current Android package: {package}"
            )

            return package

        except Exception as exc:
            self._log(
                f"Unable to determine current package: "
                f"{type(exc).__name__}: {exc}"
            )

            return None

    def get_current_activity(self):
        """
        Return the current Android activity.

        Returns:
            str or None
        """

        try:
            activity = self.driver.current_activity

            self._log(
                f"Current Android activity: {activity}"
            )

            return activity

        except Exception as exc:
            self._log(
                f"Unable to determine current activity: "
                f"{type(exc).__name__}: {exc}"
            )

            return None

    # ------------------------------------------------------------------
    # Page source diagnostics
    # ------------------------------------------------------------------

    def get_page_source(self):
        """
        Safely retrieve Android page source.

        Returns:
            str or None
        """

        try:
            source = self.driver.page_source

            if source:
                self._log(
                    f"Page source retrieved "
                    f"({len(source)} characters)."
                )

            return source

        except Exception as exc:
            self._log(
                f"Unable to retrieve page source: "
                f"{type(exc).__name__}: {exc}"
            )

            return None

    def dump_page_source(self, filename=None):
        """
        Save page source to disk for Jenkins diagnostics.

        Returns:
            str or None: Path to saved file.
        """

        if filename is None:
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            filename = f"home_page_source_{timestamp}.xml"

        try:
            source = self.driver.page_source

            if not source:
                self._log("Page source is empty.")
                return None

            directory = os.path.dirname(filename)

            if directory:
                os.makedirs(directory, exist_ok=True)

            with open(
                filename,
                "w",
                encoding="utf-8",
            ) as file:
                file.write(source)

            self._log(
                f"Page source saved to: {filename}"
            )

            return filename

        except Exception as exc:
            self._log(
                f"Unable to save page source: "
                f"{type(exc).__name__}: {exc}"
            )

            return None

    # ------------------------------------------------------------------
    # Home screen detection
    # ------------------------------------------------------------------

    def _calculator_indicator_present(self):
        """
        Look for calculator-specific indicators.

        Returns:
            bool
        """

        for locator in self.CALCULATOR_INDICATORS:
            element = self._find_element(
                locator,
                timeout=self.SHORT_TIMEOUT,
            )

            if element is not None:
                return True

        return False

    def _home_text_present(self):
        """
        Look for explicit Home/Calculator text.
        """

        for locator in self.HOME_TEXT_LOCATORS:
            element = self._find_element(
                locator,
                timeout=self.SHORT_TIMEOUT,
            )

            if element is not None:
                return True

        return False

    def _menu_button_present(self):
        """
        Look for the navigation/menu button.

        This is useful because the calculator home page may not expose a
        literal 'Home' text element.
        """

        for locator in self.MENU_BUTTON_LOCATORS:
            element = self._find_element(
                locator,
                timeout=self.SHORT_TIMEOUT,
            )

            if element is not None:
                return True

        return False

    # ------------------------------------------------------------------
    # Primary Home verification
    # ------------------------------------------------------------------

    def verify_home_loaded(self):
        """
        Verify that the Android Calculator Home screen is loaded.

        Strategy:

        1. Verify that the Appium session is alive.
        2. Allow a short stabilization period.
        3. Check explicit Home/Calculator identifiers.
        4. Check calculator-specific UI indicators.
        5. Check the navigation/menu button.
        6. If necessary, inspect page source for calculator indicators.
        7. Return True only when a reliable indicator is found.

        This avoids relying on one fragile XPath, which is especially
        important on the remote Jenkins Android emulator.
        """

        self._log("=" * 60)
        self._log("VERIFYING ANDROID CALCULATOR HOME SCREEN")
        self._log("=" * 60)

        if not self._driver_is_alive():
            self._log(
                "FAIL: Appium driver/session is not available."
            )
            return False

        # --------------------------------------------------------------
        # Give Android/Appium a moment to settle.
        # --------------------------------------------------------------

        self._log(
            "Allowing Android UI to stabilize..."
        )

        time.sleep(1)

        # --------------------------------------------------------------
        # Log diagnostic information.
        # --------------------------------------------------------------

        package = self.get_current_package()
        activity = self.get_current_activity()

        if package:
            self._log(
                f"Home verification package: {package}"
            )

        if activity:
            self._log(
                f"Home verification activity: {activity}"
            )

        # --------------------------------------------------------------
        # Strategy 1 - explicit Home/Calculator text
        # --------------------------------------------------------------

        self._log(
            "Checking explicit Home/Calculator indicators..."
        )

        if self._home_text_present():
            self._log(
                "PASS: Explicit Home/Calculator indicator found."
            )
            return True

        # --------------------------------------------------------------
        # Strategy 2 - calculator-specific identifiers
        # --------------------------------------------------------------

        self._log(
            "Checking calculator-specific indicators..."
        )

        if self._calculator_indicator_present():
            self._log(
                "PASS: Calculator-specific UI indicator found."
            )
            return True

        # --------------------------------------------------------------
        # Strategy 3 - navigation/menu button
        # --------------------------------------------------------------

        self._log(
            "Checking navigation/menu button..."
        )

        if self._menu_button_present():
            self._log(
                "PASS: Navigation/menu button found."
            )
            return True

        # --------------------------------------------------------------
        # Strategy 4 - page source fallback
        #
        # This is deliberately used only after direct element lookup
        # fails. It provides a useful fallback for Android UI timing
        # and accessibility differences.
        # --------------------------------------------------------------

        self._log(
            "Direct locators did not identify Home."
        )

        self._log(
            "Inspecting Android page source..."
        )

        source = self.get_page_source()

        if source:
            source_lower = source.lower()

            source_indicators = (
                "calculator",
                "basic calculator",
            )

            for indicator in source_indicators:
                if indicator in source_lower:
                    self._log(
                        "PASS: Calculator indicator found "
                        f"in page source: '{indicator}'"
                    )
                    return True

        # --------------------------------------------------------------
        # Failure
        # --------------------------------------------------------------

        self._log(
            "FAIL: No reliable Home screen indicator was found."
        )

        self._log(
            "Capturing page source for diagnostics..."
        )

        try:
            self.dump_page_source(
                filename=os.path.join(
                    "snapshots",
                    "home_failure_page_source.xml",
                )
            )
        except Exception as exc:
            self._log(
                f"Page-source diagnostic failed: "
                f"{type(exc).__name__}: {exc}"
            )

        return False

    # ------------------------------------------------------------------
    # Wait for Home
    # ------------------------------------------------------------------

    def wait_for_home(self, timeout=None):
        """
        Wait until the Home screen is detected.

        Returns:
            bool
        """

        wait_time = timeout if timeout is not None else self.LONG_TIMEOUT

        self._log(
            f"Waiting up to {wait_time}s for Home screen..."
        )

        start_time = time.monotonic()

        while (time.monotonic() - start_time) < wait_time:

            if not self._driver_is_alive():
                self._log(
                    "Driver became unavailable while waiting "
                    "for Home."
                )
                return False

            try:
                if self._home_text_present():
                    self._log(
                        "Home detected while waiting."
                    )
                    return True

                if self._calculator_indicator_present():
                    self._log(
                        "Calculator UI detected while waiting."
                    )
                    return True

                if self._menu_button_present():
                    self._log(
                        "Navigation menu detected while waiting."
                    )
                    return True

            except Exception as exc:
                self._log(
                    f"Transient Home detection error: "
                    f"{type(exc).__name__}: {exc}"
                )

            time.sleep(0.5)

        self._log(
            f"FAIL: Home screen was not detected within "
            f"{wait_time}s."
        )

        return False

    # ------------------------------------------------------------------
    # Menu interaction
    # ------------------------------------------------------------------

    def get_menu_button(self):
        """
        Return the navigation/menu button if available.
        """

        return self._try_visible_locators(
            self.MENU_BUTTON_LOCATORS,
            timeout=self.SHORT_TIMEOUT,
        )

    def is_menu_button_visible(self):
        """
        Determine whether the menu button is visible.
        """

        return self.get_menu_button() is not None

    def click_menu(self):
        """
        Click the Home screen navigation/menu button.

        Returns:
            bool
        """

        self._log(
            "Attempting to open navigation menu..."
        )

        element = self.get_menu_button()

        if element is None:
            self._log(
                "FAIL: Navigation/menu button was not found."
            )
            return False

        try:
            element.click()

            self._log(
                "Navigation/menu button clicked."
            )

            return True

        except (
            StaleElementReferenceException,
            WebDriverException,
        ) as exc:

            self._log(
                f"Menu click failed on first attempt: "
                f"{type(exc).__name__}: {exc}"
            )

            # Retry once using a freshly located element.
            try:
                time.sleep(0.5)

                element = self.get_menu_button()

                if element is None:
                    self._log(
                        "FAIL: Menu button disappeared during retry."
                    )
                    return False

                element.click()

                self._log(
                    "Navigation/menu button clicked on retry."
                )

                return True

            except Exception as retry_exc:
                self._log(
                    f"Menu click retry failed: "
                    f"{type(retry_exc).__name__}: {retry_exc}"
                )
                return False

        except Exception as exc:
            self._log(
                f"Unexpected menu click error: "
                f"{type(exc).__name__}: {exc}"
            )
            return False

    # ------------------------------------------------------------------
    # Generic text helpers
    # ------------------------------------------------------------------

    def find_text(self, text, timeout=None):
        """
        Find an Android element by exact text.

        Args:
            text: Text displayed by the Android element.
            timeout: Optional timeout.

        Returns:
            WebElement or None
        """

        if text is None:
            return None

        text = str(text).strip()

        if not text:
            return None

        locator = (
            AppiumBy.XPATH,
            f"//*[@text={self._xpath_literal(text)}]",
        )

        return self._find_element(
            locator,
            timeout=timeout if timeout is not None else self.SHORT_TIMEOUT,
        )

    def is_text_visible(self, text, timeout=None):
        """
        Determine whether exact text is visible.
        """

        if text is None:
            return False

        text = str(text).strip()

        if not text:
            return False

        locator = (
            AppiumBy.XPATH,
            f"//*[@text={self._xpath_literal(text)}]",
        )

        return (
            self._find_visible_element(
                locator,
                timeout=timeout if timeout is not None else self.SHORT_TIMEOUT,
            )
            is not None
        )

    @staticmethod
    def _xpath_literal(value):
        """
        Safely create an XPath string literal.

        Handles strings containing single quotes, double quotes, or both.
        """

        value = str(value)

        if "'" not in value:
            return f"'{value}'"

        if '"' not in value:
            return f'"{value}"'

        parts = value.split("'")

        xpath_parts = []

        for index, part in enumerate(parts):
            if part:
                xpath_parts.append(f"'{part}'")

            if index < len(parts) - 1:
                xpath_parts.append('"\'"')

        return "concat(" + ", ".join(xpath_parts) + ")"

    # ------------------------------------------------------------------
    # Generic click helper
    # ------------------------------------------------------------------

    def click_text(self, text, timeout=None):
        """
        Find an element by exact text and click it.

        Returns:
            bool
        """

        element = self.find_text(
            text,
            timeout=timeout,
        )

        if element is None:
            self._log(
                f"FAIL: Text element not found: {text!r}"
            )
            return False

        try:
            element.click()

            self._log(
                f"Clicked text element: {text!r}"
            )

            return True

        except StaleElementReferenceException:
            self._log(
                f"Element became stale while clicking: {text!r}"
            )

            # Retry with a newly located element.
            try:
                element = self.find_text(
                    text,
                    timeout=self.SHORT_TIMEOUT,
                )

                if element is None:
                    return False

                element.click()

                self._log(
                    f"Clicked text element on retry: {text!r}"
                )

                return True

            except Exception as exc:
                self._log(
                    f"Retry click failed for {text!r}: "
                    f"{type(exc).__name__}: {exc}"
                )
                return False

        except WebDriverException as exc:
            self._log(
                f"WebDriver click failed for {text!r}: {exc}"
            )
            return False

        except Exception as exc:
            self._log(
                f"Unexpected click error for {text!r}: "
                f"{type(exc).__name__}: {exc}"
            )
            return False

    # ------------------------------------------------------------------
    # Refresh / recovery helpers
    # ------------------------------------------------------------------

    def wait_for_app_stability(self, seconds=1):
        """
        Give the Android application time to stabilize.
        """

        try:
            seconds = max(0, float(seconds))
        except (TypeError, ValueError):
            seconds = 1

        self._log(
            f"Waiting {seconds:.1f}s for app stabilization..."
        )

        time.sleep(seconds)

    def recover_to_home(self):
        """
        Attempt to recover the application to its Home screen.

        This method does not force-stop or restart the application because
        doing so can interfere with the Appium session and Jenkins test
        cleanup. It simply uses Android BACK operations when possible.

        Returns:
            bool
        """

        self._log(
            "Attempting recovery to Home screen..."
        )

        if not self._driver_is_alive():
            self._log(
                "Cannot recover: driver is unavailable."
            )
            return False

        # First determine whether Home is already present.
        try:
            if self._home_text_present():
                self._log(
                    "Already on Home screen."
                )
                return True

            if self._calculator_indicator_present():
                self._log(
                    "Calculator Home UI already present."
                )
                return True

        except Exception:
            pass

        # Attempt Android BACK a small number of times.
        for attempt in range(1, 4):
            try:
                self._log(
                    f"Recovery BACK attempt {attempt}/3..."
                )

                self.driver.back()

                time.sleep(1)

                if self._home_text_present():
                    self._log(
                        "Home screen recovered."
                    )
                    return True

                if self._calculator_indicator_present():
                    self._log(
                        "Calculator Home UI recovered."
                    )
                    return True

            except WebDriverException as exc:
                self._log(
                    f"BACK attempt {attempt} failed: {exc}"
                )

            except Exception as exc:
                self._log(
                    f"Unexpected recovery error: "
                    f"{type(exc).__name__}: {exc}"
                )

        self._log(
            "FAIL: Unable to recover to Home screen."
        )

        return False

    # ------------------------------------------------------------------
    # Backward-compatible aliases
    # ------------------------------------------------------------------

    def verify_home(self):
        """
        Backward-compatible alias for verify_home_loaded().
        """

        return self.verify_home_loaded()

    def is_home_loaded(self):
        """
        Backward-compatible alias for verify_home_loaded().
        """

        return self.verify_home_loaded()

    def home_loaded(self):
        """
        Backward-compatible alias for verify_home_loaded().
        """

        return self.verify_home_loaded()