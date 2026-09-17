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
        try:
            print("Checking for Test Ad")
            self.verify_test_ad()
            print("Test Ad found - Clicking close ad")
            self.dismiss_test_ad()
            print("Closed ad - Verifying Home header")
            self.verify_home_header()
            return True
        except:
            print("2nd attempt - Checking for Test Ad")
            self.verify_test_ad()
            print("2nd attempt - Test Ad found - Clicking close ad")
            self.dismiss_test_ad()
            print("2nd attempt - Closed ad - Verifying Home header")
            self.verify_home_header()
            return True

    def verify_home_header(self):
        print("Verifying Home header")
        WebDriverWait(self.driver, 25).until(
            EC.visibility_of_element_located(self.HOME_HEADER))
        print("Home header found")

    def verify_test_ad(self):
        print("Checking for Test Ad header")
        WebDriverWait(self.driver, 45).until(
            EC.visibility_of_element_located(self.TEST_AD_HEADER))
        print("Test Ad header found")

    def dismiss_test_ad(self):
        self.driver.execute_script("mobile: clickGesture", {"x": 1015, "y": 215})

