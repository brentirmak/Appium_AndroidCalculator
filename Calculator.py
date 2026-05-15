from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time
from appium.options.common import AppiumOptions
from contextlib import contextmanager
import StoreToMySQL
import os
from datetime import datetime

trx_dict = {}
device_info = []

@contextmanager
def appium_transaction(name):
    start_time = time.time()
    print("")
    print(f"Starting Transaction: {name}")
    try:
        yield
    finally:
        end_time = time.time()
        duration = end_time - start_time
        print(f"Transaction {name} took {duration:.2f} seconds")
        trx_dict.update({name: duration})

def capture_error_snapshot(driver, test_name):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    folder = f"Error_Snapshots/{test_name}"
    os.makedirs(folder, exist_ok=True)

    screenshot_path = os.path.join(
        folder,
        f"error_{timestamp}.png"
    )
    driver.save_screenshot(screenshot_path)
    print(f"Saved screenshot: {screenshot_path}")


options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:deviceName": "emulator-5554",
    "appium:automationName": "UiAutomator2",
    "appium:noReset": True,
    # calculator.currencyconverter.tipcalculator.unitconverter/com.google.android.gms.ads.AdActivity}
    "appium:appPackage": "calculator.currencyconverter.tipcalculator.unitconverter",
    "appium:appActivity": ".MainActivity",
    "appium:appWaitActivity": "*",
    "appium:forceAppLaunch": True,
    "appium:autoLaunch": True,
    "appium:appWaitDuration": 30000,
    "appium:autoGrantPermissions": True,
    "appium:adbExecTimeout": 60000,  # Give it 60s to find the device
    "appium:uiautomator2ServerInstallTimeout": 60000,
    "appium:newCommandTimeout": 300,
    # Important
    "appium:waitForIdleTimeout": 0,
    "appium:waitForSelectorTimeout": 10000,
    # Optional stability improvements
    "appium:disableWindowAnimation": True
})

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

caps = driver.capabilities
info = driver.execute_script("mobile: deviceInfo")

platformName = caps.get("platformName")
platformVersion = caps.get("platformVersion")

if info["model"] == "sdk_gphone16k_x86_64":
    info["model"] = "Pixel 10 Emulator"

deviceModel = info["model"]
deviceManufacturer = info["manufacturer"]

device_info.append(platformName)
device_info.append(platformVersion)
device_info.append(deviceModel)
device_info.append(deviceManufacturer)

driver.implicitly_wait(15)

try:
    print("Successfully connected to Windows Emulator!")
    print("Proceeding...")

    with appium_transaction("Home") as home_transaction:
        try:
            print("Checking the Home header")
            driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Home"]')
            print("Home header was found")

            print("Waiting for Home to load with the Basic Calculator icon")
            driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Basic Calculator"] ')
            print("Basic Calculator icon found")
        except:
            try:
                print("Home didn't load - will check to see if Ad screen is active")
                print("Checking to see if a Test Ad was loaded")
                driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Test Ad"] | //android.webkit.WebView')
                print("Test Ad displayed - need to close it")
                driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@resource-id="dismiss-button"]').click()
                print("Clicked on dismiss button to close Test Ad")
            except:
                try:
                    print("There was no close button for the Test Add pop-up - proceeding...")
                    print("Checking to see if there's a Close Ad link on the upper right corner of the Ad")
                    driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@resource-id="close-button"]/android.view.View/android.view.View/android.widget.Image').click()
                    print("Found Close Ad link on the upper right corner of the Ad - clicked on it")
                except:
                    try:
                        print("Checking to see if there's a Continue to app link on the upper right corner of the Ad")
                        driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Continue to app"]').click()
                        print("Found Continue to app link on the upper right corner of the Ad - clicked on it")
                        print("Checking to see if there's a 'x' icon on the upper right corner")
                        driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Image').click()
                        print("Clicked on the 'x' icon on the upper right corner")
                    except:
                        capture_error_snapshot(driver, "Home")
                        raise

    with appium_transaction("Access Basic Calculator"):
        try:
            print("Will now click on the Basic Calculator icon")
            driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Basic Calculator"]').click()
            print("Clicked on the Basic Calculator icon")
        except:
            print("We are not at the Home screen")

        try:
            print("Checking for the Basic Calculator header")
            driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Basic Calculator"]')
            print("Basic Calculator header was found")
        except Exception as e:
            capture_error_snapshot(driver, "AccessBasicCalculator")
            raise
    with appium_transaction("Perform Basic Calculation"):
        try:
            print("Looking for the delete icon")
            driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ImageView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_delete"]')
            print("Found the delete icon")

            print("Looking for the 'C' button")
            driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_clear"]').click()
            print("Found the 'C' button - clicked on it")

            print("Clicking on 9")
            driver.find_element(by=AppiumBy.ID, value='calculator.currencyconverter.tipcalculator.unitconverter:id/btn_num9').click()
            print("Clicked on 9")

            print("Clicking on '+'")
            driver.find_element(by=AppiumBy.ID, value='calculator.currencyconverter.tipcalculator.unitconverter:id/btn_plus').click()
            print("Clicked on '+'")

            print("Clicking on 9 again")
            driver.find_element(by=AppiumBy.ID, value='calculator.currencyconverter.tipcalculator.unitconverter:id/btn_num9').click()
            print("Clicked on 9 again")

            print("Looking for the '=' icon")
            driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_result"]').click()
            print("Found the '=' icon")

            print("Looking for result")
            output = driver.find_element(by=AppiumBy.ID, value='calculator.currencyconverter.tipcalculator.unitconverter:id/tvResult').text
            print(f"Test Result: 9 + 9 {output}")
            print("Found the result")
        except Exception as e:
            capture_error_snapshot(driver, "PerformBasicCalculation")
            raise

    with appium_transaction("Go Back To Home"):
        try:
            print("Clicking on the menu")
            driver.find_element(by=AppiumBy.ID,value='calculator.currencyconverter.tipcalculator.unitconverter:id/btn_open_side_menu').click()
            print("Clicked on the menu")

            print("Clicking on the Home link")
            driver.find_element(by=AppiumBy.XPATH,value='//android.widget.TextView[@text="Home"]').click()
            print("Clicked on the Home link")

            print("Checking the Tip Calculator option")
            driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Tip Calculator"]')
            print("Found the Tip Calculator option")
        except Exception as e:
            capture_error_snapshot(driver, "GoBackToHome")
            raise

        print("************************************")
        print("Script terminated successfully")
        print("************************************")


finally:
    StoreToMySQL.store_to_mysql(trx_dict, device_info)

    print("Terminating the application")
    driver.terminate_app("calculator.currencyconverter.tipcalculator.unitconverter")

    time.sleep(2)
    print("Quitting the driver")
    driver.quit()



