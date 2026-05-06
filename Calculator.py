from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time
from appium.options.common import AppiumOptions
from contextlib import contextmanager


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

options = AppiumOptions()
options.load_capabilities({
	"platformName": "Android",
	"appium:deviceName": "emulator-5554",
	"appium:automationName": "UiAutomator2",
	"appium:noReset": True,
	"appium:appPackage": "com.google.android.apps.nexuslauncher",
    "appium:appActivity": ".NexusLauncherActivity",
    "appium:appWaitActivity": "*",
    "appium:autoLaunch": True,
    "appium:appWaitDuration": 30000,
    "appium:autoGrantPermissions": True
})

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
driver.implicitly_wait(15)

try:
    print("Successfully connected to Windows Emulator!")

    #time.sleep(100)

    with appium_transaction("Home"):
        try:
            print("Checking the Home header")
            driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Home"]')
            print("Home header was found")

            print("Waiting for Home to load with the Basic Calculator icon")
            driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Basic Calculator"] ')
            print("Basic Calculator icon found")
        except:
            print("Home didn't load - will check to see if Ad screen is active")

        try:
            print("Checking to see if a Test Ad was loaded")
            driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Test Ad"]')
            print("Test Ad displayed - need to close it")
            #time.sleep(10)
            driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@resource-id="dismiss-button"]').click()
            print("Clicked on dismiss button to close Test Ad")
        except:
            try:
                print("Checking to see if there's a Close Ad link on the upper right corner of the Ad")
                driver.find_element(by=AppiumBy.XPATH, value='//android.view.View[@resource-id="close-button"]/android.view.View/android.view.View/android.widget.Image').click()
                print("Found Close Ad link on the upper right corner of the Ad - clicked on it")
            except:
                try:
                    print("Checking to see if there's a Continue to app link on the upper right corner of the Ad")
                    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Continue to app"]').click()
                    print("Found Continue to app link on the upper right corner of the Ad - clicked on it")
                except:
                    print("No Ad was found - proceeding...")

    with appium_transaction("Access Basic Calculator"):
        try:
            print("Will now click on the Basic Calculator icon")
            driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Basic Calculator"]').click()
            print("Clicked on the Basic Calculator icon")
        except:
            print("We are not at the Home screen")

        print("Checking for the Basic Calculator header")
        driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Basic Calculator"]')
        print("Basic Calculator header was found")

    with appium_transaction("Perform Basic Calculation"):
        print("Looking for the '=' icon")
        driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_result"]')
        print("Found the '=' icon")

        print("Looking for the 'C' button")
        driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_result"]').click()
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

    with appium_transaction("Go Back To Home"):
        print("Clicking on the menu")
        driver.find_element(by=AppiumBy.ID,value='calculator.currencyconverter.tipcalculator.unitconverter:id/btn_open_side_menu').click()
        print("Clicked on the menu")

        print("Clicking on the Home link")
        driver.find_element(by=AppiumBy.XPATH,value='//android.widget.TextView[@text="Home"]').click()
        print("Clicked on the Home link")

        print("Checking the Tip Calculator option")
        driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Tip Calculator"]')
        print("Found the Tip Calculator option")

finally:
    print("Terminating the application")
    driver.terminate_app('com.google.android.apps.nexuslauncher')
    driver.execute_script("mobile: terminateApp", {"appId": "com.google.android.apps.nexuslauncher"})

    time.sleep(2)
    print("Quitting the driver")
    driver.quit()