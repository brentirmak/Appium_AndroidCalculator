from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    NoSuchElementException,
    StaleElementReferenceException,
    TimeoutException,
)

import time
import os


class HomePage(BasePage):

    # ============================================================
    # APP PACKAGE
    # ============================================================

    APP_PACKAGE = "calculator.currencyconverter.tipcalculator.unitconverter"

    # ============================================================
    # ONBOARDING / LANGUAGE
    # ============================================================

    LANGUAGE_HEADER = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@text="Language"]'
    )

    LANGUAGE_CONFIRM_ICON = (
        AppiumBy.XPATH,
        '//android.widget.ImageView'
        '[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_submit"]'
    )

    NEXT_BUTTON = (
        AppiumBy.XPATH,
        '//android.widget.TextView'
        '[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_next"]'
    )

    # ============================================================
    # AD
    # ============================================================

    TEST_AD_HEADER = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@text="Test Ad"]'
    )

    # ============================================================
    # HOME
    # ============================================================

    # Original locator retained as a possible indicator.
    HOME_HEADER = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@text="Home"]'
    )

    # Possible home-screen indicators.
    #
    # We intentionally do NOT depend on a single "Home" TextView.
    # The application can change the widget type/text while the
    # actual home screen remains perfectly usable.

    CALCULATOR_TEXT = (
        AppiumBy.XPATH,
        '//*[contains(@text,"Calculator")]'
    )

    BASIC_CALCULATOR_TEXT = (
        AppiumBy.XPATH,
        '//*[contains(@text,"Basic")]'
    )

    SCIENTIFIC_TEXT = (
        AppiumBy.XPATH,
        '//*[contains(@text,"Scientific")]'
    )

    HISTORY_TEXT = (
        AppiumBy.XPATH,
        '//*[contains(@text,"History")]'
    )

    UNIT_CONVERTER_TEXT = (
        AppiumBy.XPATH,
        '//*[contains(@text,"Unit")]'
    )

    CURRENCY_TEXT = (
        AppiumBy.XPATH,
        '//*[contains(@text,"Currency")]'
    )

    # ============================================================
    # GENERIC HELPERS
    # ============================================================

    def _is_element_visible(self, locator):
        """
        Safely determine whether an element is currently visible.
        Never raises NoSuchElementException or StaleElementReferenceException.
        """

        try:
            element = self.driver.find_element(*locator)
            return element.is_displayed()

        except (
            NoSuchElementException,
            StaleElementReferenceException,
        ):
            return False

    def _wait_for_element(self, locator, timeout=30):
        """
        Wait for an element to become visible.
        Returns the element or None.
        """

        try:
            return WebDriverWait(
                self.driver,
                timeout,
                poll_frequency=1
            ).until(
                EC.visibility_of_element_located(locator)
            )

        except TimeoutException:
            return None

    # ============================================================
    # TEST AD
    # ============================================================

    def dismiss_test_ad(self):
        """
        Wait for the application to initialize and repeatedly attempt
        to close the Test Ad.

        Jenkins is intentionally given more startup time because the
        remote Windows emulator is being accessed through ADB over TCP.
        """

        print()
        print("============================================================")
        print("VERIFYING / DISMISSING TEST AD")
        print("============================================================")

        # --------------------------------------------------------
        # Jenkins startup delay
        # --------------------------------------------------------

        if os.getenv("RUNNING_IN_JENKINS", "").lower() == "true":

            print(
                "Running from Jenkins - allowing 60 seconds "
                "for application initialization"
            )

            time.sleep(60)

        else:

            print(
                "Running locally - allowing 10 seconds "
                "for application initialization"
            )

            time.sleep(10)

        # --------------------------------------------------------
        # Allow the ad time to appear
        # --------------------------------------------------------

        end_time = time.time() + 90

        while time.time() < end_time:

            print("Checking if Test Ad is visible")

            if not self._is_element_visible(self.TEST_AD_HEADER):

                print(
                    "Test Ad is not currently visible."
                )

                return True

            print(
                "Test Ad detected - attempting to close it"
            )

            # ----------------------------------------------------
            # The application has historically required several
            # taps to dismiss the test advertisement.
            # ----------------------------------------------------

            try:

                self.driver.execute_script(
                    "mobile: clickGesture",
                    {
                        "x": 1037,
                        "y": 74
                    }
                )

            except Exception as e:

                print(
                    f"Ad close click #1 failed: {e}"
                )

            try:

                self.driver.execute_script(
                    "mobile: clickGesture",
                    {
                        "x": 1031,
                        "y": 215
                    }
                )

            except Exception as e:

                print(
                    f"Ad close click #2 failed: {e}"
                )

            try:

                self.driver.execute_script(
                    "mobile: clickGesture",
                    {
                        "x": 87,
                        "y": 96
                    }
                )

            except Exception as e:

                print(
                    f"Ad close click #3 failed: {e}"
                )

            print(
                "Waiting for Test Ad state to update..."
            )

            time.sleep(2)

        # --------------------------------------------------------
        # Final check
        # --------------------------------------------------------

        if self._is_element_visible(self.TEST_AD_HEADER):

            print(
                'Test Ad is still visible after 90 seconds.'
            )

            raise TimeoutError(
                '"Test Ad" still visible after 90 seconds'
            )

        print(
            "Test Ad successfully dismissed."
        )

        return True

    # ============================================================
    # LANGUAGE / ONBOARDING
    # ============================================================

    def complete_language_setup(self):

        print()
        print("============================================================")
        print("HANDLING LANGUAGE / ONBOARDING")
        print("============================================================")

        print(
            "Checking for Language header"
        )

        # --------------------------------------------------------
        # Language screen is optional.
        # --------------------------------------------------------

        try:

            WebDriverWait(
                self.driver,
                15,
                poll_frequency=1
            ).until(
                EC.visibility_of_element_located(
                    self.LANGUAGE_HEADER
                )
            )

            print(
                "Language header is visible"
            )

            print(
                "Language setup detected"
            )

        except TimeoutException:

            print(
                "Language setup is not displayed."
            )

            # Even when language setup isn't present, there may
            # still be onboarding screens.
            return self._process_onboarding()

        # --------------------------------------------------------
        # Confirm language
        # --------------------------------------------------------

        print(
            "Waiting for language confirmation icon"
        )

        try:

            confirm_icon = WebDriverWait(
                self.driver,
                30,
                poll_frequency=1
            ).until(
                EC.element_to_be_clickable(
                    self.LANGUAGE_CONFIRM_ICON
                )
            )

            print(
                "Language confirmation icon found"
            )

            confirm_icon.click()

            print(
                "Language confirmation clicked"
            )

        except TimeoutException:

            print(
                "Language confirmation icon was not found."
            )

            return False

        except Exception as e:

            print(
                f"Unable to click language confirmation: {e}"
            )

            return False

        # --------------------------------------------------------
        # Process onboarding
        # --------------------------------------------------------

        return self._process_onboarding()

    def _process_onboarding(self):

        print()
        print(
            "Processing onboarding Next buttons"
        )

        # --------------------------------------------------------
        # Do not assume there are exactly 3 screens.
        #
        # This is important because application versions can add
        # or remove onboarding screens.
        # --------------------------------------------------------

        max_steps = 8

        for step in range(1, max_steps + 1):

            print(
                f"Looking for Next button "
                f"(onboarding step {step})"
            )

            try:

                next_button = WebDriverWait(
                    self.driver,
                    10,
                    poll_frequency=1
                ).until(
                    EC.element_to_be_clickable(
                        self.NEXT_BUTTON
                    )
                )

            except TimeoutException:

                print(
                    "Next button is no longer visible."
                )

                print(
                    "Onboarding appears to be complete."
                )

                break

            except Exception as e:

                print(
                    f"Error locating Next button: {e}"
                )

                break

            try:

                print(
                    f"Clicking Next button (step {step})"
                )

                next_button.click()

            except (
                StaleElementReferenceException,
                Exception
            ) as e:

                print(
                    f"Next button became stale or "
                    f"click failed: {e}"
                )

                # Try one more time after the screen settles.
                time.sleep(2)

                try:

                    next_button = WebDriverWait(
                        self.driver,
                        5,
                        poll_frequency=1
                    ).until(
                        EC.element_to_be_clickable(
                            self.NEXT_BUTTON
                        )
                    )

                    next_button.click()

                except Exception:

                    print(
                        "Unable to click Next button "
                        "after retry."
                    )

                    break

            print(
                "Waiting for onboarding screen transition..."
            )

            time.sleep(2)

        # --------------------------------------------------------
        # Confirm onboarding has finished.
        # --------------------------------------------------------

        print(
            "Waiting for onboarding to finish"
        )

        try:

            WebDriverWait(
                self.driver,
                15,
                poll_frequency=1
            ).until_not(
                EC.visibility_of_element_located(
                    self.NEXT_BUTTON
                )
            )

            print(
                "Onboarding Next button is no longer visible"
            )

        except TimeoutException:

            print(
                "Next button may still be present."
            )

        return True

    # ============================================================
    # HOME SCREEN VERIFICATION
    # ============================================================

    def verify_home_header(self):

        print()
        print(
            "Verifying Home screen"
        )

        # --------------------------------------------------------
        # IMPORTANT:
        #
        # Do NOT wait 60 seconds for only:
        #
        #   TextView[@text="Home"]
        #
        # That is the problem with the previous implementation.
        #
        # Instead, check several possible indicators.
        # --------------------------------------------------------

        print(
            "Checking original Home header locator..."
        )

        if self._is_element_visible(self.HOME_HEADER):

            print(
                "Home header found"
            )

            return True

        print(
            "Original Home header not found."
        )

        # --------------------------------------------------------
        # Give the application some additional time to settle.
        # --------------------------------------------------------

        print(
            "Waiting for calculator home screen to initialize..."
        )

        time.sleep(5)

        # --------------------------------------------------------
        # Candidate home-screen indicators.
        # --------------------------------------------------------

        candidates = [
            (
                "Calculator",
                self.CALCULATOR_TEXT
            ),
            (
                "Basic Calculator",
                self.BASIC_CALCULATOR_TEXT
            ),
            (
                "Scientific",
                self.SCIENTIFIC_TEXT
            ),
            (
                "History",
                self.HISTORY_TEXT
            ),
            (
                "Unit",
                self.UNIT_CONVERTER_TEXT
            ),
            (
                "Currency",
                self.CURRENCY_TEXT
            ),
        ]

        for name, locator in candidates:

            print(
                f"Checking home indicator: {name}"
            )

            if self._is_element_visible(locator):

                print(
                    f"Home screen indicator found: {name}"
                )

                return True

        # --------------------------------------------------------
        # Last resort:
        #
        # Inspect the current UI hierarchy for useful evidence.
        # This makes Jenkins logs much more useful when the app
        # changes its UI.
        # --------------------------------------------------------

        print()
        print(
            "No known home-screen indicator found."
        )

        try:

            page_source = self.driver.page_source

            print()
            print(
                "Current Android UI hierarchy:"
            )

            print(
                page_source[:12000]
            )

        except Exception as e:

            print(
                f"Unable to retrieve page source: {e}"
            )

        return False

    # ============================================================
    # MAIN HOME VERIFICATION
    # ============================================================

    def verify_home_loaded(self):

        print()
        print("============================================================")
        print("VERIFYING HOME SCREEN")
        print("============================================================")

        # --------------------------------------------------------
        # Step 1
        # --------------------------------------------------------

        print()
        print(
            "[STEP 1/3] Handling Test Ad"
        )

        self.dismiss_test_ad()

        # --------------------------------------------------------
        # Step 2
        # --------------------------------------------------------

        print()
        print(
            "[STEP 2/3] Handling Language / Onboarding"
        )

        self.complete_language_setup()

        # --------------------------------------------------------
        # Step 3
        # --------------------------------------------------------

        print()
        print(
            "[STEP 3/3] Verifying Home screen"
        )

        home_loaded = self.verify_home_header()

        if home_loaded:

            print()
            print(
                "============================================================"
            )

            print(
                "HOME SCREEN SUCCESSFULLY LOADED"
            )

            print(
                "============================================================"
            )

            return True

        print()
        print(
            "============================================================"
        )

        print(
            "HOME SCREEN FAILED TO LOAD"
        )

        print(
            "============================================================"
        )

        return False