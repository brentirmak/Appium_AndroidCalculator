from appium.webdriver.common.appiumby import AppiumBy
from utils.helpers import appium_transaction, capture_error_snapshot
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pytest, time

TIMEOUT = 10

# requires pytest-timeout
@pytest.mark.timeout(45)

class TestCalculator:

    def test_home(self, driver):
        wait = WebDriverWait(driver, TIMEOUT)
        with appium_transaction("Home"):
            try:
                print("Checking Home header")
                wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@text="Home"]')))
                print("Home header found - checking for Basic Calculator icon")
                wait.until(EC.presence_of_element_located(
                    (AppiumBy.XPATH, '//android.widget.TextView[@text="Basic Calculator"]')))
                print("Basic Calculator icon found")
            except:
                try:
                    print("Checking for Test Ad")
                    wait.until(EC.presence_of_element_located(
                        (AppiumBy.XPATH, '//android.widget.TextView[@text="Test Ad"] | //android.webkit.WebView')))
                    print("Test Ad link found - will click on the Dismiss button")
                    wait.until(EC.element_to_be_clickable(
                        (AppiumBy.XPATH, '//android.view.View[@resource-id="dismiss-button"]'))).click()
                    print("Clicked on Dismiss button")
                except:
                    try:
                        wait.until(EC.element_to_be_clickable((AppiumBy.XPATH,
                            '//android.view.View[@resource-id="close-button"]/android.view.View/android.view.View/android.widget.Image'))).click()
                    except:
                        try:
                            wait.until(EC.element_to_be_clickable(
                                (AppiumBy.XPATH, '//android.widget.TextView[@text="Continue to app"]'))).click()
                            wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.Image'))).click()
                            print("Clicked on Continue to app button")
                        except:
                            print("Failing transaction - could not get passed Home step")
                            capture_error_snapshot(driver, "Home")
                            raise

    def test_access_basic_calculator(self, driver):
        with appium_transaction("Access Basic Calculator"):
            try:
                print("Looking for Basic Calculator icon")
                driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Basic Calculator"]').click()
                print("Clicked Basic Calculator icon")
            except:
                print("Not at Home screen")

            try:
                print("Checking for Calculator header")
                driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Basic Calculator"]')
                print("Basic Calculator header found")
            except Exception:
                capture_error_snapshot(driver, "AccessBasicCalculator")
                print("Failing AccessBasicCalculator transaction")
                raise

    def test_perform_basic_calculation(self, driver):
        with appium_transaction("Perform Basic Calculation"):
            try:
                print("Checking for Clear button")
                driver.find_element(AppiumBy.XPATH, '//android.widget.ImageView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_delete"]')
                driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_clear"]').click()
                print("Clear button clicked")

                print("Clicking on '9'")
                driver.find_element(AppiumBy.ID, 'calculator.currencyconverter.tipcalculator.unitconverter:id/btn_num9').click()
                print("Clicking on '+'")
                driver.find_element(AppiumBy.ID, 'calculator.currencyconverter.tipcalculator.unitconverter:id/btn_plus').click()
                print("Clicking on '9'")
                driver.find_element(AppiumBy.ID, 'calculator.currencyconverter.tipcalculator.unitconverter:id/btn_num9').click()
                print("Clicking on result button")
                driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_result"]').click()
                print("Capturing output")
                output = driver.find_element(AppiumBy.ID, 'calculator.currencyconverter.tipcalculator.unitconverter:id/tvResult').text
                print(f"Test Result: 9 + 9 = {output}")

                assert output == "= 18", f"Expected 18 but got {output}"

            except Exception:
                capture_error_snapshot(driver, "PerformBasicCalculation")
                print("Failing PerformBasicCalculation transaction")
                raise

    def test_access_tip_calculator(self, driver):
        with appium_transaction("Access Tip Calculator"):
            try:
                driver.find_element(AppiumBy.XPATH, '//android.widget.ImageView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_open_side_menu"]').click()
                print("Clicked on Menu (upper left corner)")
                try:
                    driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Tip Calculator"]').click()
                    print("Clicked on Tip Calculator option")
                    driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/tv_tip_on"]')
                    print("Checking for Tip header")
                except:
                    driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Tip Calculator"]').click()
                    print("2nd try - Clicked on Tip Calculator option")
                    driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/tv_tip_on"]')
                    print("2nd try - Checking for Tip header")
            except Exception:
                capture_error_snapshot(driver, "AccessTipCalculator")
                print("Failing AccessTipCalculator transaction")
                raise

    def test_perform_tip_calculation(self, driver):
        with appium_transaction("Perform Tip Calculation"):
            try:
                try:
                    print("Clearing previous entries that were left")
                    driver.find_element(AppiumBy.XPATH, '//android.widget.ImageView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_more"]').click()
                    driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/recycleActions"]').click()
                    driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_save"]').click()
                    print("Cleared previous entries")
                except:
                    print("Nothing to clear")

                print("Checking for Tip header")
                driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/tv_tip_on"]')
                print("Tip header found")

                print("Checking for Bill field")
                driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/et_bill"]').click()
                driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/et_bill"]').send_keys("100")
                print("Enter '100' for the Bill field")

                print("Clear tip field")
                driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/et_tip"]').clear()
                driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/et_tip"]').click()
                print("Click on tip field")
                driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/et_tip"]').send_keys("20")
                print("Enter 20 into the tip field")
                driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_equal"]').click()
                print("Click on the '=' button")
                output = driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/tv_average_amount_value"]').text
                print(f"Total per person {output}")
                assert output == "120.00", f"Expected 120.00 but got {output}"

            except Exception:
                capture_error_snapshot(driver, "PerformTipCalculation")
                print("Failing PerformTipCalculation transaction")
                raise

    def test_go_back_to_home(self, driver):
        with appium_transaction("Go Back To Home"):
            try:
                print("Click on the side menu")
                driver.find_element(AppiumBy.ID, 'calculator.currencyconverter.tipcalculator.unitconverter:id/btn_open_side_menu').click()
                driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Home"]').click()
                print("Clicked on the 'Home' option")
                driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Tip Calculator"]')
                print("Found Tip Calculator menu option — back at Home")
            except Exception:
                capture_error_snapshot(driver, "GoBackToHome")
                print("Failing GoBackToHome transaction")
                raise
