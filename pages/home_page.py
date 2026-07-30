from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

import time

class HomePage(BasePage):

    LANGUAGE_HEADER = (AppiumBy.XPATH,'//android.widget.TextView[@text="Language"]')
    TEST_AD_HEADER = (AppiumBy.XPATH,'//android.widget.TextView[@text="Test Ad"]')
    LANGUAGE_CONFIRM_ICON = (AppiumBy.XPATH,'//android.widget.ImageView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_submit"]')
    NEXT_BUTTON = (AppiumBy.XPATH,'//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_next"]')
    HOME_HEADER = (AppiumBy.XPATH, '//android.widget.TextView[@text="Home"]')

    def dismiss_test_ad(self):
        """
        Repeatedly taps the ad close button while "Test Ad" is visible,
        waiting `poll_interval` seconds between checks, until it's gone
        or `timeout` seconds have elapsed.
        """
        locator = (AppiumBy.XPATH, '//android.widget.TextView[@text="Test Ad"]')
        end_time = time.time() + 30

        time.sleep(5)

        def is_ad_visible():
            try:
                return self.driver.find_element(*locator).is_displayed()
            except (NoSuchElementException, StaleElementReferenceException):
                return False

        while time.time() < end_time:
            print("Checking if Test Ad is visible")
            if not is_ad_visible():
                print("Test Ad is no longer visible - exiting loop")
                return True  # ad is gone
            print("Perform a couple of clicks to close out the Ad..")
            self.driver.execute_script("mobile: clickGesture", {"x": 1037, "y": 74})
            self.driver.execute_script("mobile: clickGesture", {"x": 1031, "y": 215})
            self.driver.execute_script("mobile: clickGesture", {"x": 87, "y": 96})
            print("Waiting for a second...")
            time.sleep(1)

        raise TimeoutError('"Test Ad" still visible after 30 seconds')



    def complete_language_setup(self):
        print("Checking for Language header")

        try:
            WebDriverWait(self.driver, 45).until(
                EC.visibility_of_element_located(self.LANGUAGE_HEADER)
            )
            print("Language header visible — clicking confirm icon")

            confirm_icon = WebDriverWait(self.driver, 45).until(
                EC.element_to_be_clickable(self.LANGUAGE_CONFIRM_ICON)
            )
            confirm_icon.click()

            print("Clicking Next buttons")
            next_button = WebDriverWait(self.driver, 45).until(
                EC.element_to_be_clickable(self.NEXT_BUTTON)
            )

            for _ in range(3):
                next_button.click()
                time.sleep(1)

            return True

        except:
            print("Language setup not shown — skipping")
            return False

    def verify_home_header(self):
        print("Verifying Home header")

        try:
            WebDriverWait(self.driver, 45).until(
                EC.visibility_of_element_located(self.HOME_HEADER)
            )
            print("Home header found")
            return True
        except:
            print("Home header NOT found")
            return False

    def verify_home_loaded(self):
        # Step 1: dismiss ad if present
        self.dismiss_test_ad()

        # Step 2: complete language setup if present
        self.complete_language_setup()

        # Step 3: verify home screen
        return self.verify_home_header()
