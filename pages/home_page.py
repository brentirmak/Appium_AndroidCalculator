from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class HomePage(BasePage):

    LANGUAGE_HEADER = (AppiumBy.XPATH,'//android.widget.TextView[@text="Language"]')

    TEST_AD_HEADER = (AppiumBy.XPATH,'//android.widget.TextView[@text="Test Ad"]')

    LANGUAGE_CONFIRM_ICON = (AppiumBy.XPATH,'//android.widget.ImageView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_submit"]')

    NEXT_BUTTON = (AppiumBy.XPATH,'//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_next"]')

    HOME_HEADER = (AppiumBy.XPATH, '//android.widget.TextView[@text="Home"]')

    def dismiss_test_ad(self):
        print("Checking for Test Ad")

        try:
            WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located(self.TEST_AD_HEADER)
            )
            print("Test Ad found — tapping X")
            time.sleep(10)
            self.driver.execute_script("mobile: clickGesture", {"x": 1037, "y": 74})
            return True
        except:
            print("No Test Ad displayed")
            return False

    def complete_language_setup(self):
        print("Checking for Language header")

        try:
            WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(self.LANGUAGE_HEADER)
            )
            print("Language header visible — clicking confirm icon")

            confirm_icon = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable(self.LANGUAGE_CONFIRM_ICON)
            )
            confirm_icon.click()

            print("Clicking Next buttons")
            next_button = WebDriverWait(self.driver, 30).until(
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
            WebDriverWait(self.driver, 30).until(
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

    '''
    def verify_home_loaded(self):

        time.sleep(15)

        try:
            print("Checking for Test Ad")
            test_ad_header = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located(self.TEST_AD_HEADER)
            )
            print("Test Ad found - will tap on the x icon on the Test Ad")
            self.driver.execute_script("mobile: clickGesture", {"x": 1037, "y": 74})
            print("Tapped on the x icon on the Test Ad - checking to see if the Language header is displayed")

            language_header = WebDriverWait(self.driver, 45).until(
                EC.presence_of_element_located(self.LANGUAGE_HEADER)
            )
            assert  language_header.is_displayed()
            try:
                print("Language header is displayed - will check if the checkmark icon is displayed")

                language_confirm_icon = WebDriverWait(self.driver, 45).until(
                    EC.presence_of_element_located(self.LANGUAGE_CONFIRM_ICON)
                )
                assert language_confirm_icon.is_displayed()
                print("Checkmark icon is displayed - will click on it")

                language_confirm_icon.click()
                print("Clicked on checkmark icon - will click on the Next button")

                next_button = WebDriverWait(self.driver, 45).until(
                    EC.presence_of_element_located(self.NEXT_BUTTON)
                )
                next_button.click()
                time.sleep(3)
                print("Clicked on the Next button - will click on the Next button a 2nd time")
                next_button.click()
                time.sleep(3)
                print("Clicked on the Next button - will click on the Next button a 3rd time")
                next_button.click()
                time.sleep(3)
                print("Clicked on the Start button - will check for the Home header")
                home_header = WebDriverWait(self.driver, 45).until(
                    EC.presence_of_element_located(self.HOME_HEADER)
                )
                print("Home header found - passing transaction/test")

                return True
            except:
                print("Language header NOT displayed - we're at the menu page")
        except:
            print("Test Ad was not displayed - will check for the Home header")

            home_header = WebDriverWait(self.driver, 45).until(
                EC.presence_of_element_located(self.HOME_HEADER)
            )
            print("Home header found - passing transaction/test")
    '''