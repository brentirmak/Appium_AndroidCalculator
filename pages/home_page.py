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

    Jenkins considerations:
        - Uses longer startup delays when running under Jenkins.
        - Uses retry logic for transient Appium failures.
        - Dumps the Android UI hierarchy when Home verification fails.
    """

    APP_PACKAGE = (
        "calculator.currencyconverter.tipcalculator.unitconverter"
    )

    # ==================================================================
    # HOME SCREEN LOCATORS
    # ==================================================================

    # IMPORTANT:
    #
    # tvTitle is shared by multiple screens/dialogs in the application.
    # It MUST NOT be used by itself to determine whether Home is loaded.
    #
    # We retain the locator because it is useful for reading the title,
    # but _check_home_header() validates the actual text before accepting
    # it as a Home indicator.

    HOME_HEADER = (
        AppiumBy.ID,
        f"{APP_PACKAGE}:id/tvTitle"
    )

    # Text values that can legitimately indicate the Home screen.
    #
    # Keep these broad enough to support application variations, but
    # specific enough that a dialog title such as "Important Update"
    # will not accidentally qualify as Home.
    HOME_TEXT_INDICATORS = [
        "Calculator",
        "Basic Calculator",
        "Scientific",
        "History",
        "Unit",
        "Currency",
    ]

    # ==================================================================
    # IMPORTANT UPDATE DIALOG
    # ==================================================================

    IMPORTANT_UPDATE_TITLE = (
        AppiumBy.ID,
        f"{APP_PACKAGE}:id/tvTitle"
    )

    IMPORTANT_UPDATE_TEXT = (
        AppiumBy.XPATH,
        "//*[@text='Important Update']"
    )

    IMPORTANT_UPDATE_CLOSE_BUTTON = (
        AppiumBy.ID,
        f"{APP_PACKAGE}:id/btnClose"
    )

    IMPORTANT_UPDATE_BOTTOM_SHEET = (
        AppiumBy.ID,
        f"{APP_PACKAGE}:id/design_bottom_sheet"
    )

    # ==================================================================
    # LANGUAGE / ONBOARDING LOCATORS
    # ==================================================================

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

    # ==================================================================
    # INITIAL TEST AD
    # ==================================================================

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

    # ==================================================================
    # ONBOARDING NEXT BUTTON
    # ==================================================================

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

    # ==================================================================
    # INITIALIZATION
    # ==================================================================

    def __init__(self, driver):
        super().__init__(driver)

        self.default_wait = int(
            os.getenv(
                "APPIUM_DEFAULT_WAIT",
                "10"
            )
        )

        self.home_wait = int(
            os.getenv(
                "APPIUM_HOME_WAIT",
                "30"
            )
        )

        self.jenkins = bool(
            os.getenv("JENKINS_HOME")
            or os.getenv("BUILD_ID")
            or os.getenv("JENKINS_SERVER_COOKIE")
        )

        print("\n============================================================")
        print("HOMEPAGE INITIALIZED")
        print("============================================================")

        print(
            f"APPIUM_DEFAULT_WAIT = {self.default_wait}"
        )

        print(
            f"APPIUM_HOME_WAIT = {self.home_wait}"
        )

        print(
            f"Jenkins environment detected = {self.jenkins}"
        )

    # ==================================================================
    # GENERIC HELPERS
    # ==================================================================

    def _find_visible(self, locator, timeout=3):
        """
        Return a visible element if it exists.

        Returns:
            WebElement if found and visible
            None if not found or an Appium/Selenium error occurs
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

        Returns:
            True if clicked successfully.
            False otherwise.
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

        return (
            self._find_visible(
                locator,
                timeout=timeout
            )
            is not None
        )

    # ==================================================================
    # IMPORTANT UPDATE DETECTION
    # ==================================================================

    def _important_update_visible(self, timeout=2):
        """
        Determine whether the Important Update dialog is currently
        visible.

        This method deliberately checks both the actual text and the
        bottom-sheet container.

        tvTitle alone is NOT used because tvTitle is shared with the
        Home screen.
        """

        # --------------------------------------------------------------
        # Most reliable check: actual dialog text
        # --------------------------------------------------------------

        if self._element_exists(
            self.IMPORTANT_UPDATE_TEXT,
            timeout=timeout
        ):

            return True

        # --------------------------------------------------------------
        # Secondary check: bottom-sheet container
        # --------------------------------------------------------------

        if self._element_exists(
            self.IMPORTANT_UPDATE_BOTTOM_SHEET,
            timeout=timeout
        ):

            # The container may exist for another purpose, so verify
            # that the Important Update title is associated with it.
            try:

                title = self._find_visible(
                    self.IMPORTANT_UPDATE_TITLE,
                    timeout=1
                )

                if title:

                    title_text = (
                        title.text
                        or ""
                    ).strip().lower()

                    if "important update" in title_text:

                        return True

            except Exception:
                pass

        return False

    # ==================================================================
    # TEST AD
    # ==================================================================

    def handle_test_ad(self):
        """
        Detect and dismiss the test advertisement if it appears.

        The advertisement may not appear on every launch, so failure to
        find it is considered a normal condition.
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
                "Running under Jenkins - allowing "
                f"{init_delay} seconds for application "
                "initialization"
            )

        else:

            print(
                "Running locally - allowing "
                f"{init_delay} seconds for application "
                "initialization"
            )

        time.sleep(init_delay)

        max_attempts = 3

        for attempt in range(
            1,
            max_attempts + 1
        ):

            print(
                f"\nTest Ad check attempt "
                f"{attempt}/{max_attempts}"
            )

            ad_found = False

            # ----------------------------------------------------------
            # Check known close buttons
            # ----------------------------------------------------------

            for locator in self.TEST_AD_CLOSE_LOCATORS:

                if self._element_exists(
                    locator,
                    timeout=2
                ):

                    ad_found = True

                    print(
                        "Test Ad detected - attempting "
                        "to close it"
                    )

                    if self._click_if_visible(
                        locator,
                        timeout=5
                    ):

                        print(
                            "Test Ad close button clicked"
                        )

                        time.sleep(2)

                        break

            # ----------------------------------------------------------
            # Check recognizable advertisement text
            # ----------------------------------------------------------

            if not ad_found:

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

                    if self._element_exists(
                        locator,
                        timeout=1
                    ):

                        ad_found = True

                        print(
                            f"Test Ad detected using text: "
                            f"{text}"
                        )

                        break

            # ----------------------------------------------------------
            # Nothing found
            # ----------------------------------------------------------

            if not ad_found:

                print(
                    "Test Ad is not currently visible."
                )

                return True

            print(
                "Waiting for Test Ad state to update..."
            )

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
        Handle initial language selection and onboarding.

        Onboarding normally appears only on the first application
        launch, so absence of the Language or Next screens is treated
        as normal.
        """

        print("\n============================================================")
        print("HANDLING LANGUAGE / ONBOARDING")
        print("============================================================")

        # --------------------------------------------------------------
        # LANGUAGE SCREEN
        # --------------------------------------------------------------

        print(
            "Checking for Language header"
        )

        language_header = self._find_visible(
            self.LANGUAGE_HEADER,
            timeout=5
        )

        if language_header:

            print(
                "Language header is visible"
            )

            print(
                "Language setup detected"
            )

            print(
                "Waiting for language confirmation"
            )

            confirmation = self._find_visible(
                self.LANGUAGE_CONFIRMATION,
                timeout=10
            )

            if confirmation:

                print(
                    "Language confirmation found"
                )

                try:

                    confirmation.click()

                    print(
                        "Language confirmation clicked"
                    )

                except Exception as exc:

                    print(
                        "Unable to click language "
                        f"confirmation: {exc}"
                    )

            else:

                print(
                    "Language confirmation was not found."
                )

            time.sleep(2)

        else:

            print(
                "Language screen not detected."
            )

        # --------------------------------------------------------------
        # ONBOARDING NEXT BUTTONS
        # --------------------------------------------------------------

        print(
            "\nProcessing onboarding Next buttons"
        )

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
                    "Waiting for onboarding "
                    "screen transition..."
                )

                time.sleep(2)

            except (
                StaleElementReferenceException,
                WebDriverException,
            ) as exc:

                print(
                    "Unable to click onboarding "
                    f"Next button: {exc}"
                )

                time.sleep(1)

        # --------------------------------------------------------------
        # Allow final transition
        # --------------------------------------------------------------

        print(
            "Waiting for onboarding to finish"
        )

        time.sleep(2)

        # --------------------------------------------------------------
        # Final Next button check
        # --------------------------------------------------------------

        for locator in self.ONBOARDING_NEXT_LOCATORS:

            if self._element_exists(
                locator,
                timeout=1
            ):

                print(
                    "Onboarding Next button is "
                    "still visible"
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
        Dismiss the post-onboarding Important Update bottom sheet.

        Returns:
            True  - Dialog was found and dismissed.
            False - Dialog was not present OR could not be dismissed.

        A return value of False when the dialog was not present is
        intentionally treated as normal behavior by verify_home_loaded().
        """

        print("\n============================================================")
        print("CHECKING FOR IMPORTANT UPDATE")
        print("============================================================")

        # --------------------------------------------------------------
        # Determine whether dialog exists
        # --------------------------------------------------------------

        if not self._important_update_visible(
            timeout=3
        ):

            print(
                "Important Update dialog is not present."
            )

            return False

        print(
            "Important Update dialog detected."
        )

        # --------------------------------------------------------------
        # Read title for diagnostics
        # --------------------------------------------------------------

        try:

            title = self._find_visible(
                self.IMPORTANT_UPDATE_TITLE,
                timeout=2
            )

            if title:

                title_text = (
                    title.text
                    or ""
                ).strip()

                print(
                    f"Dialog title detected: "
                    f"'{title_text}'"
                )

        except Exception:

            print(
                "Unable to read Important Update title."
            )

        # --------------------------------------------------------------
        # Standard close button
        # --------------------------------------------------------------

        print(
            "Looking for Important Update "
            "close button..."
        )

        if self._click_if_visible(
            self.IMPORTANT_UPDATE_CLOSE_BUTTON,
            timeout=5
        ):

            print(
                "Important Update close button clicked."
            )

            time.sleep(2)

            # ----------------------------------------------------------
            # Verify dismissal
            # ----------------------------------------------------------

            if not self._important_update_visible(
                timeout=2
            ):

                print(
                    "Important Update dialog dismissed."
                )

                return True

            print(
                "Close button was clicked, but the "
                "Important Update dialog is still present."
            )

            # ----------------------------------------------------------
            # Second close attempt
            # ----------------------------------------------------------

            if self._click_if_visible(
                self.IMPORTANT_UPDATE_CLOSE_BUTTON,
                timeout=3
            ):

                print(
                    "Second Important Update close "
                    "attempt completed."
                )

                time.sleep(2)

                if not self._important_update_visible(
                    timeout=2
                ):

                    print(
                        "Important Update dialog dismissed "
                        "on second attempt."
                    )

                    return True

        # --------------------------------------------------------------
        # Fallback close strategies
        # --------------------------------------------------------------

        print(
            "Standard close button did not dismiss "
            "Important Update."
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

            print(
                "Trying fallback Important Update "
                "close locator..."
            )

            if self._click_if_visible(
                locator,
                timeout=2
            ):

                print(
                    "Important Update dismissed "
                    "using fallback close locator."
                )

                time.sleep(2)

                if not self._important_update_visible(
                    timeout=2
                ):

                    return True

        # --------------------------------------------------------------
        # Final fallback: Android BACK
        # --------------------------------------------------------------

        print(
            "Attempting Android BACK as final fallback..."
        )

        try:

            self.driver.back()

            time.sleep(2)

            if not self._important_update_visible(
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
        Check the UI hierarchy for known Home screen text indicators.

        This is one of the primary Home verification methods.
        """

        for text in self.HOME_TEXT_INDICATORS:

            print(
                f"Checking Home indicator: {text}"
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
        Check the tvTitle element, but DO NOT treat the existence of
        tvTitle alone as proof that Home is loaded.

        tvTitle is also used by the Important Update dialog.

        The element is accepted only when its actual text matches a
        known Home-screen title.
        """

        print(
            "Checking Home header locator..."
        )

        element = self._find_visible(
            self.HOME_HEADER,
            timeout=3
        )

        if not element:

            print(
                "Home header element not found."
            )

            return False

        try:

            text = (
                element.text
                or ""
            ).strip()

        except Exception:

            text = ""

        print(
            f"tvTitle text detected: '{text}'"
        )

        # --------------------------------------------------------------
        # Never accept Important Update as Home
        # --------------------------------------------------------------

        if (
            "important update"
            in text.lower()
        ):

            print(
                "tvTitle belongs to Important Update."
            )

            return False

        # --------------------------------------------------------------
        # Validate actual Home title
        # --------------------------------------------------------------

        for indicator in self.HOME_TEXT_INDICATORS:

            if (
                indicator.lower()
                in text.lower()
            ):

                print(
                    "tvTitle contains recognized "
                    f"Home text: '{indicator}'"
                )

                return True

        print(
            "tvTitle exists, but its text does not "
            "identify the Home screen."
        )

        return False

    def _home_is_clear_of_dialogs(self):
        """
        Confirm that the Important Update dialog is not covering Home.

        This is deliberately performed before accepting any Home
        indicator.
        """

        if self._important_update_visible(
            timeout=1
        ):

            print(
                "Important Update is still visible. "
                "Home cannot yet be considered verified."
            )

            return False

        return True

    def _check_home_screen(self):
        """
        Perform one complete Home-screen verification attempt.

        Order:
            1. Confirm Important Update is absent.
            2. Check validated tvTitle.
            3. Check known Home text indicators.
        """

        # --------------------------------------------------------------
        # Dialog protection
        # --------------------------------------------------------------

        if not self._home_is_clear_of_dialogs():

            return False

        # --------------------------------------------------------------
        # Header
        # --------------------------------------------------------------

        if self._check_home_header():

            print(
                "Home verified using validated tvTitle."
            )

            return True

        # --------------------------------------------------------------
        # Text indicators
        # --------------------------------------------------------------

        if self._check_home_text_indicators():

            print(
                "Home verified using Home text indicator."
            )

            return True

        return False

    # ==================================================================
    # UI DIAGNOSTICS
    # ==================================================================

    def _dump_ui_hierarchy(self):
        """
        Print the current Android UI hierarchy for diagnostics.
        """

        print(
            "\n============================================================"
        )

        print(
            "CURRENT ANDROID UI HIERARCHY"
        )

        print(
            "============================================================"
        )

        try:

            hierarchy = self.driver.page_source

            print(hierarchy)

        except Exception as exc:

            print(
                f"Unable to retrieve UI hierarchy: {exc}"
            )

    # ==================================================================
    # HOME VERIFICATION
    # ==================================================================

    def verify_home_loaded(self):
        """
        Complete Home-screen initialization and verification.

        Returns:
            True  - Home screen successfully loaded.
            False - Home screen could not be verified.
        """

        print("\n============================================================")
        print("VERIFYING HOME SCREEN")
        print("============================================================")

        # ==============================================================
        # STEP 1 - TEST AD
        # ==============================================================

        print(
            "\n[STEP 1/4] Handling Test Ad"
        )

        try:

            self.handle_test_ad()

        except Exception as exc:

            print(
                "Test Ad handling raised an exception: "
                f"{exc}"
            )

            print(
                "Continuing because the ad may have "
                "already disappeared."
            )

        # ==============================================================
        # STEP 2 - LANGUAGE / ONBOARDING
        # ==============================================================

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
                "Language/onboarding handling raised "
                f"an exception: {exc}"
            )

        # ==============================================================
        # STEP 3 - IMPORTANT UPDATE
        # ==============================================================

        print(
            "\n[STEP 3/4] Handling Important Update"
        )

        try:

            self.dismiss_important_update()

        except Exception as exc:

            print(
                "Important Update handling raised "
                f"an exception: {exc}"
            )

        # ==============================================================
        # STEP 4 - HOME VERIFICATION
        # ==============================================================

        print(
            "\n[STEP 4/4] Verifying Home screen"
        )

        print(
            "Waiting for calculator Home screen "
            "to initialize..."
        )

        home_wait = self.home_wait

        start_time = time.time()

        attempt = 0

        while (
            time.time() - start_time
            < home_wait
        ):

            attempt += 1

            elapsed = (
                time.time()
                - start_time
            )

            remaining = max(
                0,
                home_wait - elapsed
            )

            print(
                "\n------------------------------------------------------------"
            )

            print(
                f"Home verification attempt #{attempt}"
            )

            print(
                f"Elapsed: {elapsed:.1f}s | "
                f"Remaining: {remaining:.1f}s"
            )

            print(
                "------------------------------------------------------------"
            )

            # ----------------------------------------------------------
            # Important Update may appear after onboarding or after
            # the application finishes loading.
            # ----------------------------------------------------------

            try:

                if self._important_update_visible(
                    timeout=1
                ):

                    print(
                        "Important Update detected during "
                        "Home verification."
                    )

                    dismissed = (
                        self.dismiss_important_update()
                    )

                    if dismissed:

                        print(
                            "Important Update dismissed. "
                            "Continuing Home verification."
                        )

                    else:

                        print(
                            "Important Update could not be "
                            "dismissed during this attempt."
                        )

                        time.sleep(2)

                        continue

            except Exception as exc:

                print(
                    "Exception while checking Important "
                    f"Update: {exc}"
                )

            # ----------------------------------------------------------
            # Home verification
            # ----------------------------------------------------------

            try:

                if self._check_home_screen():

                    print(
                        "\n============================================================"
                    )

                    print(
                        "HOME SCREEN VERIFIED SUCCESSFULLY"
                    )

                    print(
                        "============================================================"
                    )

                    return True

            except Exception as exc:

                print(
                    "Home verification attempt raised "
                    f"an exception: {exc}"
                )

            print(
                "Home screen not verified yet."
            )

            time.sleep(2)

        # ==============================================================
        # HOME SCREEN NOT FOUND
        # ==============================================================

        print(
            "\n============================================================"
        )

        print(
            "HOME SCREEN FAILED TO LOAD"
        )

        print(
            "============================================================"
        )

        # ==============================================================
        # FINAL IMPORTANT UPDATE CHECK
        # ==============================================================

        try:

            if self._important_update_visible(
                timeout=2
            ):

                print(
                    "\nIMPORTANT UPDATE DIALOG IS STILL "
                    "COVERING THE APPLICATION."
                )

                dismissed = (
                    self.dismiss_important_update()
                )

                if dismissed:

                    print(
                        "Important Update was dismissed "
                        "during final recovery."
                    )

                    # Give Home one final opportunity.
                    time.sleep(3)

                    if self._check_home_screen():

                        print(
                            "Home screen verified after "
                            "final Important Update recovery."
                        )

                        return True

        except Exception as exc:

            print(
                "Final Important Update recovery failed: "
                f"{exc}"
            )

        # ==============================================================
        # FINAL HOME CHECK
        # ==============================================================

        print(
            "\nPerforming final Home-screen verification..."
        )

        try:

            if self._check_home_screen():

                print(
                    "Home screen verified during final check."
                )

                return True

        except Exception as exc:

            print(
                "Final Home verification failed: "
                f"{exc}"
            )

        # ==============================================================
        # DIAGNOSTICS
        # ==============================================================

        print(
            "\nHome screen could not be verified."
        )

        print(
            "Dumping Android UI hierarchy for diagnostics..."
        )

        self._dump_ui_hierarchy()

        return False