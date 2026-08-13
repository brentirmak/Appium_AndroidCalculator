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


class HomePage(BasePage):

    # =========================================================
    # LOCATORS
    # =========================================================

    LANGUAGE_HEADER = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@text="Language"]'
    )

    TEST_AD_HEADER = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@text="Test Ad"]'
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

    HOME_HEADER = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@text="Home"]'
    )

    # =========================================================
    # GENERIC ELEMENT HELPERS
    # =========================================================

    def wait_for_element_visible(self, locator, timeout=10):
        """
        Wait for an element to become visible.

        Returns:
            True  - element became visible
            False - element was not found within timeout
        """

        try:

            WebDriverWait(
                self.driver,
                timeout,
                poll_frequency=0.5,
                ignored_exceptions=(
                    NoSuchElementException,
                    StaleElementReferenceException,
                )
            ).until(
                EC.visibility_of_element_located(locator)
            )

            return True

        except TimeoutException:

            return False

    # =========================================================
    # TEST AD
    # =========================================================

    def is_test_ad_visible(self):
        """
        Determine whether the Test Ad is currently visible.
        """

        try:

            element = self.driver.find_element(
                *self.TEST_AD_HEADER
            )

            return element.is_displayed()

        except (
            NoSuchElementException,
            StaleElementReferenceException,
        ):

            return False

    def dismiss_test_ad(self):
        """
        Wait for the application to initialize and dismiss
        the Test Ad if it is displayed.

        The method will continue checking for up to 90 seconds.
        """

        print("\nChecking if Test Ad is visible")

        # -----------------------------------------------------
        # Initial application stabilization
        # -----------------------------------------------------

        print(
            "Allowing application time to initialize..."
        )

        time.sleep(5)

        # -----------------------------------------------------
        # Look for the ad
        # -----------------------------------------------------

        end_time = time.time() + 90

        while time.time() < end_time:

            if not self.is_test_ad_visible():

                print(
                    "Test Ad is no longer visible - exiting loop"
                )

                return True

            print(
                "Test Ad detected - attempting to close it"
            )

            try:

                # Close/clear possible ad controls.
                self.driver.execute_script(
                    "mobile: clickGesture",
                    {
                        "x": 1037,
                        "y": 74
                    }
                )

                self.driver.execute_script(
                    "mobile: clickGesture",
                    {
                        "x": 1031,
                        "y": 215
                    }
                )

                self.driver.execute_script(
                    "mobile: clickGesture",
                    {
                        "x": 87,
                        "y": 96
                    }
                )

            except Exception as e:

                print(
                    f"Warning while attempting to close "
                    f"Test Ad: {e}"
                )

            print(
                "Waiting for Test Ad state to update..."
            )

            time.sleep(2)

        # -----------------------------------------------------
        # Ad failed to disappear
        # -----------------------------------------------------

        raise TimeoutError(
            '"Test Ad" still visible after 90 seconds'
        )

    # =========================================================
    # LANGUAGE / ONBOARDING
    # =========================================================

    def is_language_setup_visible(self):
        """
        Determine whether the language setup screen is visible.
        """

        print(
            "Checking for Language header"
        )

        visible = self.wait_for_element_visible(
            self.LANGUAGE_HEADER,
            timeout=10
        )

        if visible:

            print(
                "Language header is visible"
            )

        else:

            print(
                "Language header is not visible"
            )

        return visible

    def complete_language_setup(self):
        """
        Complete the application's initial language/onboarding
        workflow if it is displayed.

        The method does NOT assume that exactly three Next
        screens exist. It repeatedly looks for a fresh Next
        button and clicks it until the button disappears.
        """

        # -----------------------------------------------------
        # Determine whether onboarding is required
        # -----------------------------------------------------

        if not self.is_language_setup_visible():

            print(
                "Language setup not shown - "
                "assuming onboarding is already complete"
            )

            return True

        print(
            "Language setup detected"
        )

        # =====================================================
        # LANGUAGE CONFIRMATION
        # =====================================================

        print(
            "Waiting for language confirmation icon"
        )

        try:

            confirm_icon = WebDriverWait(
                self.driver,
                45,
                poll_frequency=0.5,
                ignored_exceptions=(
                    NoSuchElementException,
                    StaleElementReferenceException,
                )
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
                "ERROR: Language confirmation icon "
                "was not found"
            )

            return False

        except Exception as e:

            print(
                f"ERROR clicking language confirmation: {e}"
            )

            return False

        # -----------------------------------------------------
        # Allow screen transition
        # -----------------------------------------------------

        time.sleep(2)

        # =====================================================
        # NEXT BUTTON / ONBOARDING
        # =====================================================

        print(
            "\nProcessing onboarding Next buttons"
        )

        max_steps = 4

        for step in range(1, max_steps + 1):

            print(
                f"Looking for Next button "
                f"(onboarding step {step})"
            )

            try:

                # IMPORTANT:
                # Find a NEW element on every iteration.
                # Do not reuse the previous WebElement.
                next_button = WebDriverWait(
                    self.driver,
                    10,
                    poll_frequency=0.5,
                    ignored_exceptions=(
                        NoSuchElementException,
                        StaleElementReferenceException,
                    )
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

            # -------------------------------------------------
            # Click Next
            # -------------------------------------------------

            try:

                print(
                    f"Clicking Next button "
                    f"(step {step})"
                )

                next_button.click()

            except StaleElementReferenceException:

                print(
                    "Next button became stale before "
                    "clicking - reacquiring element"
                )

                try:

                    next_button = WebDriverWait(
                        self.driver,
                        5,
                        poll_frequency=0.5
                    ).until(
                        EC.element_to_be_clickable(
                            self.NEXT_BUTTON
                        )
                    )

                    next_button.click()

                except Exception as e:

                    print(
                        f"ERROR retrying Next button click: {e}"
                    )

                    return False

            except Exception as e:

                print(
                    f"ERROR clicking Next button: {e}"
                )

                return False

            # -------------------------------------------------
            # Allow Android screen transition
            # -------------------------------------------------

            print(
                "Waiting for onboarding screen transition..."
            )

            time.sleep(2)

        # =====================================================
        # WAIT FOR ONBOARDING TO DISAPPEAR
        # =====================================================

        print(
            "\nWaiting for onboarding to finish"
        )

        try:

            WebDriverWait(
                self.driver,
                30,
                poll_frequency=0.5,
                ignored_exceptions=(
                    NoSuchElementException,
                    StaleElementReferenceException,
                )
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
                "WARNING: Next button remained visible "
                "after onboarding wait"
            )

        # -----------------------------------------------------
        # Give final Android transition time
        # -----------------------------------------------------

        time.sleep(3)

        return True

    # =========================================================
    # HOME SCREEN
    # =========================================================

    def verify_home_header(self):
        """
        Wait for the Home header to appear.
        """

        print(
            "\nVerifying Home header"
        )

        try:

            WebDriverWait(
                self.driver,
                60,
                poll_frequency=0.5,
                ignored_exceptions=(
                    NoSuchElementException,
                    StaleElementReferenceException,
                )
            ).until(
                EC.visibility_of_element_located(
                    self.HOME_HEADER
                )
            )

            print(
                "Home header found"
            )

            return True

        except TimeoutException:

            print(
                "Home header NOT found "
                "after 60 seconds"
            )

            return False

    # =========================================================
    # COMPLETE HOME WORKFLOW
    # =========================================================

    def verify_home_loaded(self):
        """
        Complete the entire Home startup workflow.

        Flow:

            1. Handle Test Ad
            2. Complete Language / onboarding
            3. Verify Home screen
        """

        print("\n")
        print("=" * 60)
        print("VERIFYING HOME SCREEN")
        print("=" * 60)

        # =====================================================
        # STEP 1 - TEST AD
        # =====================================================

        print(
            "\n[STEP 1/3] Handling Test Ad"
        )

        self.dismiss_test_ad()

        # =====================================================
        # STEP 2 - LANGUAGE / ONBOARDING
        # =====================================================

        print(
            "\n[STEP 2/3] Handling Language / Onboarding"
        )

        onboarding_result = (
            self.complete_language_setup()
        )

        if not onboarding_result:

            print(
                "\nWARNING: Language/onboarding "
                "did not complete normally"
            )

        # =====================================================
        # STEP 3 - HOME
        # =====================================================

        print(
            "\n[STEP 3/3] Verifying Home screen"
        )

        home_loaded = self.verify_home_header()

        # =====================================================
        # RESULT
        # =====================================================

        print("\n" + "=" * 60)

        if home_loaded:

            print(
                "HOME SCREEN SUCCESSFULLY LOADED"
            )

        else:

            print(
                "HOME SCREEN FAILED TO LOAD"
            )

        print("=" * 60)

        return home_loaded