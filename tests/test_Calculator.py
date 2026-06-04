import pytest
import StoreToMySQL
from appium.webdriver.common.appiumby import AppiumBy
from helpers import appium_transaction, capture_error_snapshot, trx_dict


class TestCalculator:

    def test_home(self, driver):
        with appium_transaction("Home"):
            try:
                driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Home"]')
                print("Home header found")
                driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Basic Calculator"] ')
                print("Basic Calculator icon found")
            except:
                try:
                    driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Test Ad"] | //android.webkit.WebView')
                    driver.find_element(AppiumBy.XPATH, '//android.view.View[@resource-id="dismiss-button"]').click()
                except:
                    try:
                        driver.find_element(AppiumBy.XPATH, '//android.view.View[@resource-id="close-button"]/android.view.View/android.view.View/android.widget.Image').click()
                    except:
                        try:
                            driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Continue to app"]').click()
                            driver.find_element(AppiumBy.XPATH, '//android.widget.Image').click()
                        except:
                            capture_error_snapshot(driver, "Home")
                            raise

    def test_access_basic_calculator(self, driver):
        with appium_transaction("Access Basic Calculator"):
            try:
                driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Basic Calculator"]').click()
                print("Clicked Basic Calculator icon")
            except:
                print("Not at Home screen")

            try:
                driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Basic Calculator"]')
                print("Basic Calculator header found")
            except Exception:
                capture_error_snapshot(driver, "AccessBasicCalculator")
                raise

    def test_perform_basic_calculation(self, driver):
        with appium_transaction("Perform Basic Calculation"):
            try:
                driver.find_element(AppiumBy.XPATH, '//android.widget.ImageView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_delete"]')
                driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_clear"]').click()

                driver.find_element(AppiumBy.ID, 'calculator.currencyconverter.tipcalculator.unitconverter:id/btn_num9').click()
                driver.find_element(AppiumBy.ID, 'calculator.currencyconverter.tipcalculator.unitconverter:id/btn_plus').click()
                driver.find_element(AppiumBy.ID, 'calculator.currencyconverter.tipcalculator.unitconverter:id/btn_num9').click()
                driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_result"]').click()

                output = driver.find_element(AppiumBy.ID, 'calculator.currencyconverter.tipcalculator.unitconverter:id/tvResult').text
                print(f"Test Result: 9 + 9 = {output}")

                assert output == "= 18", f"Expected 18 but got {output}"

            except Exception:
                capture_error_snapshot(driver, "PerformBasicCalculation")
                raise

    def test_go_back_to_home(self, driver):
        with appium_transaction("Go Back To Home"):
            try:
                driver.find_element(AppiumBy.ID, 'calculator.currencyconverter.tipcalculator.unitconverter:id/btn_open_side_menu').click()
                driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Home"]').click()
                driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Tip Calculator"]')
                print("Found Tip Calculator option — back at Home")
            except Exception:
                capture_error_snapshot(driver, "GoBackToHome")
                raise
