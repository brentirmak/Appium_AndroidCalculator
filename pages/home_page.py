from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

import time
import os

class HomePage(BasePage):

    LANGUAGE_HEADER = (AppiumBy.XPATH,'//android.widget.TextView[@text="Language"]')
    TEST_AD_HEADER = (AppiumBy.XPATH,'//android.widget.TextView[@text="Test Ad"]')
    LANGUAGE_CONFIRM_ICON = (AppiumBy.XPATH,'//android.widget.ImageView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_submit"]')
    NEXT_BUTTON = (AppiumBy.XPATH,'//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_next"]')
    HOME_HEADER = (AppiumBy.XPATH, '//android.widget.TextView[@text="Home"]')
    CLOSE_POPUP_ICON = (AppiumBy.XPATH, '//android.widget.ImageView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btnClose"]')


    def load_landing_page(self):
        run_type = self.get_run_type()

        if run_type.lower() == "jenkins":
            print("We are running from Jenkins - adding 15 seconds sleep time")
            time.sleep(15)
        else:
            print("This is a manual run - adding 5 seconds sleep time")
            time.sleep(5)

        home_loaded = False
        counter = 0

        while home_loaded == False & counter < 15:
            print("\nCounter: ", counter)
            print("Checking for Test Ad")
            self.verify_test_ad()
            print("Test Ad found - Clicking close ad")
            self.dismiss_test_ad()
            print("Attempted to close ad - Verifying Home header")
            home_check = self.verify_home_header()

            if home_check:
                home_loaded = True
                print("Home header found")
            else:
                home_loaded = False
                print("Home header not found yet")
                counter = counter + 1

        return True

    def verify_home_header(self):
        print("Verifying Home header")
        try:
            test = WebDriverWait(self.driver, 3).until(
                EC.visibility_of_element_located(self.HOME_HEADER)
            )
            return True
        except:
            return False

    def verify_test_ad(self):
        print("Checking for Test Ad header")
        try:
            WebDriverWait(self.driver, 3).until(
                EC.visibility_of_element_located(self.TEST_AD_HEADER)
            )
            print("Test Ad header found")
            return True
        except:
            print("Test Ad header NOT found")
            return False

    def dismiss_test_ad(self):
        self.driver.execute_script("mobile: clickGesture", {"x": 1015, "y": 215})

    def get_run_type(self):
        if "JENKINS_SERVER_COOKIE" in os.environ or "BUILD_NUMBER" in os.environ:
            return "jenkins"
        return "manual"