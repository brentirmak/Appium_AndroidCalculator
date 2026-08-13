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
    Page Object for the application's Home screen.

    Handles:
        - Test advertisements
        - Language selection
        - Initial onboarding
        - Post-onboarding "Important Update" dialog
        - Home screen verification
    """

    APP_PACKAGE = (
        "calculator.currencyconverter.tipcalculator.unitconverter"
    )

    # ------------------------------------------------------------------
    # HOME SCREEN LOCATORS
    # ------------------------------------------------------------------

    HOME_HEADER = (
        AppiumBy.ID,
        f"{APP_PACKAGE}:id/tvTitle"
    )

    # Known text-based home indicators.
    HOME_TEXT_INDICATORS = [
        "Calculator",
        "Basic Calculator",
        "Scientific",
        "History",
        "Unit",
        "Currency",
    ]

    # ------------------------------------------------------------------
    # IMPORTANT UPDATE DIALOG
    # ------------------------------------------------------------------

    IMPORTANT_UPDATE_TITLE = (
        AppiumBy.ID,
        f"{APP_PACKAGE}:id/tvTitle"
    )

    IMPORTANT_UPDATE_CLOSE_BUTTON = (
        AppiumBy.ID,
        f"{APP_PACKAGE}:id/btnClose"
    )

    IMPORTANT_UPDATE_BOTTOM_SHEET = (
        AppiumBy.ID,
        f"{APP_PACKAGE}:id/design_bottom_sheet"
    )

    # ------------------------------------------------------------------
    # LANGUAGE / ONBOARDING LOCATORS
    # ------------------------------------------------------------------

    LANGUAGE_HEADER = (
        AppiumBy.XPATH,
        "//*[@text='Language']"
    )

    LANGUAGE_CONFIRMATION = (
        AppiumBy.XPATH,
        "//*[contains(@content-desc,'Continue') "
        "or contains(@content-desc,'Confirm') "
        "or contains(@text,'Continue') "
        "or contains(@text,'Confirm')]"
    )

    # ------------------------------------------------------------------
    # INITIAL TEST AD
    # ------------------------------------------------------------------

    TEST_AD_CLOSE_LOCATORS = [
        (
            AppiumBy.ID,
            f"{APP_PACKAGE}:id/ad_close"
        ),
        (
            AppiumBy.ID,
            f"{APP_PACKAGE}:id/close"
        ),
        (
            AppiumBy.XPATH,
            "//*[@text='Close']"
        ),
        (
            AppiumBy.XPATH,
            "//*[@content-desc='Close']"
        ),
        (
            AppiumBy.XPATH,
            "//*[contains(@text,'Close')]"
        ),
    ]

    # ------------------------------------------------------------------
    # ONBOARDING NEXT BUTTON
    # ------------------------------------------------------------------

    ONBOARDING_NEXT_LOCATORS = [
        (
            AppiumBy.XPATH,
            "//*[@text='Next']"
        ),
        (
            AppiumBy.XPATH,
            "//*[@content-desc='Next']"
        ),
        (
            AppiumBy.XPATH,
            "//*[contains(@text,'Next')]"
        ),
        (
            AppiumBy.XPATH,
            "//*[contains(@content-desc,'Next')]"
        ),
    ]

    # ------------------------------------------------------------------
    # INITIALIZATION
    # ------------------------------------------------------------------

    def __init__(self, driver):
        super().__init__(driver)

        self.default_wait = int(
            os.getenv("APPIUM_DEFAULT_WAIT", "10")
        )

        self.home_wait = int(
            os.getenv("APPIUM_HOME_WAIT", "30")
        )

        self.jenkins = bool(
            os.getenv("JENKINS_HOME")
            or os.getenv("BUILD_ID")
            or os.getenv("JENKINS_SERVER_COOKIE")
        )

    # ==================================================================
    # GENERIC HELPERS
    # ==================================================================

    def _find_visible(self, locator, timeout=3):
        """
        Return a visible element if it exists.
        Return None if it does not exist.
        """

        try:
            return WebDriverWait(
                self.driver,
                timeout
            ).until(
                EC.visibility_of_element_located(locator)
            )

        except (
            TimeoutException,
            NoSuchElementException,
            StaleElementReferenceException,
            WebDriverException,
        ):
            return None

    def _click_if_visible(self, locator, timeout=3):
        """
        Click an element if it becomes visible/clickable.
        Returns True if clicked.
        """

        try:
            element = WebDriverWait(
                self.driver,
                timeout
            ).until(
                EC.element_to_be_clickable(locator)
            )

            element.click()
            return True

        except (
            TimeoutException,
            NoSuchElementException,
            StaleElementReferenceException,
            WebDriverException,
        ):
            return False

    def _element_exists(self, locator, timeout=2):
        """
        Determine whether an element exists and is visible.
        """

        return self._find_visible(
            locator,
            timeout=timeout
        ) is not None

    # ==================================================================
    # TEST AD
    # ==================================================================

    def handle_test_ad(self):
        """
        Detect and dismiss the test advertisement if it appears.

        This method is intentionally tolerant because the ad does not
        necessarily appear on every application launch.
        """

        print("\n============================================================")
        print("VERIFYING / DISMISSING TEST AD")
        print("============================================================")

        init_delay = int(
            os.getenv(
                "APPIUM_APP_INIT_DELAY",
                "20" if self.jenkins else "10"
            )
        )

        if self.jenkins:
            print(
                f"Running under Jenkins - allowing "
                f"{init_delay} seconds for application initialization"
            )
        else:
            print(
                f"Running locally - allowing "
                f"{init_delay} seconds for application initialization"
            )

        time.sleep(init_delay)

        max_attempts = 3

        for attempt in range(1, max_attempts + 1):

            print("Checking if Test Ad is visible")

            ad_found = False

            # Look for common close buttons.
            for locator in self.TEST_AD_CLOSE_LOCATORS:

                if self._element_exists(locator, timeout=2):

                    ad_found = True

                    print(
                        "Test Ad detected - attempting to close it"
                    )

                    if self._click_if_visible(
                        locator,
                        timeout=5
                    ):
                        print("Test Ad close button clicked")

                        time.sleep(2)
                        break

            if not ad_found:

                # Some ads expose recognizable text instead of a
                # stable resource ID.
                ad_texts = [
                    "Test Ad",
                    "Advertisement",
                    "Ad",
                ]

                for text in ad_texts:

                    locator = (
                        AppiumBy.XPATH,
                        f"//*[contains(@text,'{text}')]"
                    )

                    if self._element_exists(locator, timeout=1):
                        ad_found = True

                        print(
                            f"Test Ad detected using text: {text}"
                        )

                        break

            if not ad_found:
                print("Test Ad is not currently visible.")
                return True

            print("Waiting for Test Ad state to update...")
            time.sleep(2)

        print(
            "Test Ad handling completed."
        )

        return True

    # ==================================================================
    # LANGUAGE / ONBOARDING
    # ==================================================================

    def handle_language_and_onboarding(self):
        """
        Handle the initial language selection and onboarding flow.

        The method is intentionally tolerant because onboarding normally
        appears only on the first application launch.
        """

        print("\n============================================================")
        print("HANDLING LANGUAGE / ONBOARDING")
        print("============================================================")

        # --------------------------------------------------------------
        # LANGUAGE SCREEN
        # --------------------------------------------------------------

        print("Checking for Language header")

        language_header = self._find_visible(
            self.LANGUAGE_HEADER,
            timeout=5
        )

        if language_header:

            print("Language header is visible")
            print("Language setup detected")

            # Try the known confirmation locator first.
            print(
                "Waiting for language confirmation icon"
            )

            confirmation = self._find_visible(
                self.LANGUAGE_CONFIRMATION,
                timeout=10
            )

            if confirmation:

                print(
                    "Language confirmation icon found"
                )

                try:
                    confirmation.click()
                    print(
                        "Language confirmation clicked"
                    )
                except Exception as exc:
                    print(
                        f"Unable to click language confirmation: "
                        f"{exc}"
                    )

            else:
                print(
                    "Language confirmation icon not found."
                )

            time.sleep(2)

        else:

            print(
                "Language screen not detected."
            )

        # --------------------------------------------------------------
        # ONBOARDING NEXT BUTTONS
        # --------------------------------------------------------------

        print("\nProcessing onboarding Next buttons")

        max_onboarding_steps = 6

        for step in range(
            1,
            max_onboarding_steps + 1
        ):

            print(
                f"Looking for Next button "
                f"(onboarding step {step})"
            )

            next_button = None

            for locator in self.ONBOARDING_NEXT_LOCATORS:

                next_button = self._find_visible(
                    locator,
                    timeout=2
                )

                if next_button:
                    break

            if not next_button:

                print(
                    "Next button is no longer visible."
                )

                print(
                    "Onboarding appears to be complete."
                )

                break

            try:

                print(
                    f"Clicking Next button "
                    f"(step {step})"
                )

                next_button.click()

                print(
                    "Waiting for onboarding screen "
                    "transition..."
                )

                time.sleep(2)

            except (
                StaleElementReferenceException,
                WebDriverException,
            ) as exc:

                print(
                    f"Unable to click onboarding Next "
                    f"button: {exc}"
                )

                time.sleep(1)

        print(
            "Waiting for onboarding to finish"
        )

        time.sleep(2)

        # Final check.
        for locator in self.ONBOARDING_NEXT_LOCATORS:

            if self._element_exists(
                locator,
                timeout=1
            ):

                print(
                    "Onboarding Next button is still visible"
                )

                return False

        print(
            "Onboarding Next button is no longer visible"
        )

        return True

    # ==================================================================
    # IMPORTANT UPDATE DIALOG
    # ==================================================================

    def dismiss_important_update(self):
        """
        Dismiss the post-onboarding 'Important Update' bottom sheet.

        The Jenkins UI hierarchy showed:

            resource-id="...:id/design_bottom_sheet"

            text="Important Update"

            resource-id="...:id/tvTitle"

            resource-id="...:id/btnClose"

        This dialog can appear after onboarding and cover the home
        screen. It therefore MUST be handled before home verification.
        """

        print("\n============================================================")
        print("CHECKING FOR IMPORTANT UPDATE")
        print("============================================================")

        # --------------------------------------------------------------
        # First check for the specific title.
        # --------------------------------------------------------------

        title = self._find_visible(
            self.IMPORTANT_UPDATE_TITLE,
            timeout=3
        )

        if title:

            try:

                title_text = title.text

                print(
                    f"Dialog title detected: "
                    f"'{title_text}'"
                )

                if (
                    title_text
                    and "important update"
                    in title_text.lower()
                ):

                    print(
                        "Important Update dialog detected."
                    )

                else:

                    print(
                        "tvTitle is visible, but it does not "
                        "appear to be the Important Update dialog."
                    )

            except Exception:

                print(
                    "Important Update title element "
                    "is visible."
                )

        else:

            # Try the actual text directly in case the resource ID
            # is reused by another screen.

            important_update_text = (
                AppiumBy.XPATH,
                "//*[@text='Important Update']"
            )

            if not self._element_exists(
                important_update_text,
                timeout=2
            ):

                print(
                    "Important Update dialog is not present."
                )

                return False

            print(
                "Important Update dialog detected "
                "using text."
            )

        # --------------------------------------------------------------
        # Close button
        # --------------------------------------------------------------

        print(
            "Looking for Important Update close button..."
        )

        if self._click_if_visible(
            self.IMPORTANT_UPDATE_CLOSE_BUTTON,
            timeout=5
        ):

            print(
                "Important Update close button clicked."
            )

            time.sleep(2)

            # Verify that the dialog disappeared.
            if not self._element_exists(
                self.IMPORTANT_UPDATE_BOTTOM_SHEET,
                timeout=3
            ):

                print(
                    "Important Update dialog dismissed."
                )

                return True

            print(
                "Close button was clicked, but the "
                "bottom sheet is still present."
            )

            # One additional attempt.
            if self._click_if_visible(
                self.IMPORTANT_UPDATE_CLOSE_BUTTON,
                timeout=3
            ):

                time.sleep(2)

                print(
                    "Second close attempt completed."
                )

                return True

            return False

        # --------------------------------------------------------------
        # Fallback close strategies
        # --------------------------------------------------------------

        print(
            "Standard close button not found."
        )

        fallback_locators = [

            (
                AppiumBy.XPATH,
                "//*[@resource-id='"
                f"{self.APP_PACKAGE}:id/btnClose']"
            ),

            (
                AppiumBy.XPATH,
                "//*[@content-desc='Close']"
            ),

            (
                AppiumBy.XPATH,
                "//*[@text='Close']"
            ),

        ]

        for locator in fallback_locators:

            if self._click_if_visible(
                locator,
                timeout=2
            ):

                print(
                    "Important Update dismissed "
                    "using fallback close locator."
                )

                time.sleep(2)

                return True

        # --------------------------------------------------------------
        # Final fallback: Android back
        # --------------------------------------------------------------

        print(
            "Attempting Android BACK as final fallback..."
        )

        try:

            self.driver.back()

            time.sleep(2)

            if not self._element_exists(
                self.IMPORTANT_UPDATE_BOTTOM_SHEET,
                timeout=2
            ):

                print(
                    "Important Update dismissed "
                    "using Android BACK."
                )

                return True

        except Exception as exc:

            print(
                f"Android BACK failed: {exc}"
            )

        print(
            "Unable to dismiss Important Update dialog."
        )

        return False

    # ==================================================================
    # HOME SCREEN VERIFICATION
    # ==================================================================

    def _check_home_text_indicators(self):
        """
        Check the UI hierarchy for known home-screen text indicators.
        """

        for text in self.HOME_TEXT_INDICATORS:

            print(
                f"Checking home indicator: {text}"
            )

            locator = (
                AppiumBy.XPATH,
                f"//*[contains(@text,'{text}')]"
            )

            if self._element_exists(
                locator,
                timeout=2
            ):

                print(
                    f"Home indicator found: {text}"
                )

                return True

        return False

    def _check_home_header(self):
        """
        Check the original home header locator.
        """

        print(
            "Checking original Home header locator..."
        )

        element = self._find_visible(
            self.HOME_HEADER,
            timeout=5
        )

        if element:

            try:

                text = element.text

                print(
                    f"Home header found: '{text}'"
                )

            except Exception:

                print(
                    "Home header element found."
                )

            return True

        print(
            "Original Home header not found."
        )

        return False

    def _dump_ui_hierarchy(self):
        """
        Print the current Android UI hierarchy for diagnostics.
        """

        print(
            "\nCurrent Android UI hierarchy:"
        )

        try:

            hierarchy = self.driver.page_source

            print(hierarchy)

        except Exception as exc:

            print(
                f"Unable to retrieve UI hierarchy: {exc}"
            )

    def verify_home_loaded(self):
        """
        Complete Home screen initialization and verification.

        Returns:
            True  - Home screen successfully loaded.
            False - Home screen could not be verified.
        """

        print("\n============================================================")
        print("VERIFYING HOME SCREEN")
        print("============================================================")

        # --------------------------------------------------------------
        # STEP 1
        # --------------------------------------------------------------

        print("\n[STEP 1/4] Handling Test Ad")

        try:

            self.handle_test_ad()

        except Exception as exc:

            print(
                f"Test Ad handling raised an exception: "
                f"{exc}"
            )

            # Do not immediately fail. Continue to onboarding/home
            # because the ad may have already disappeared.

        # --------------------------------------------------------------
        # STEP 2
        # --------------------------------------------------------------

        print(
            "\n[STEP 2/4] Handling Language / Onboarding"
        )

        try:

            onboarding_success = (
                self.handle_language_and_onboarding()
            )

            if not onboarding_success:

                print(
                    "WARNING: Onboarding handling did not "
                    "fully confirm completion."
                )

        except Exception as exc:

            print(
                f"Language/onboarding handling raised "
                f"an exception: {exc}"
            )

        # --------------------------------------------------------------
        # STEP 3
        # --------------------------------------------------------------

        print(
            "\n[STEP 3/4] Handling Important Update"
        )

        try:

            self.dismiss_important_update()

        except Exception as exc:

            print(
                f"Important Update handling raised "
                f"an exception: {exc}"
            )

        # --------------------------------------------------------------
        # STEP 4
        # --------------------------------------------------------------

        print(
            "\n[STEP 4/4] Verifying Home screen"
        )

        print(
            "Waiting for calculator home screen to initialize..."
        )

        # Give the application time to render the actual home
        # screen after onboarding/dialog dismissal.
        home_wait = self.home_wait

        start_time = time.time()

        while (
            time.time() - start_time
            < home_wait
        ):

            # ----------------------------------------------------------
            # Important Update may reappear.
            # ----------------------------------------------------------

            try:

                if self._element_exists(
                    (
                        AppiumBy.XPATH,
                        "//*[@text='Important Update']"
                    ),
                    timeout=1
                ):

                    print(
                        "Important Update appeared again."
                    )

                    self.dismiss_important_update()

            except Exception:
                pass

            # ----------------------------------------------------------
            # Original home header
            # ----------------------------------------------------------

            if self._check_home_header():

                print(
                    "\nHOME SCREEN VERIFIED "
                    "USING ORIGINAL HEADER"
                )

                return True

            # ----------------------------------------------------------
            # Known home text indicators
            # ----------------------------------------------------------

            if self._check_home_text_indicators():

                print(
                    "\nHOME SCREEN VERIFIED "
                    "USING HOME INDICATOR"
                )

                return True

            time.sleep(2)

        # --------------------------------------------------------------
        # HOME SCREEN NOT FOUND
        # --------------------------------------------------------------

        print(
            "\n============================================================"
        )

        print(
            "HOME SCREEN FAILED TO LOAD"
        )

        print(
            "============================================================"
        )

        # Check one final time for the Important Update dialog.
        try:

            if self._element_exists(
                (
                    AppiumBy.XPATH,
                    "//*[@text='Important Update']"
                ),
                timeout=2
            ):

                print(
                    "\nIMPORTANT UPDATE DIALOG IS STILL "
                    "COVERING THE APPLICATION."
                )

                self.dismiss_important_update()

                # Give the home screen one final opportunity.
                time.sleep(3)

                if self._check_home_header():
                    return True

                if self._check_home_text_indicators():
                    return True

        except Exception:
            pass

        # Dump UI for diagnostics.
        self._dump_ui_hierarchy()

        return False