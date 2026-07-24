from appium import webdriver
from appium.options.android import UiAutomator2Options

def create_android_driver():
    options = UiAutomator2Options()

    options.platformName = "Android"
    options.automationName = "UiAutomator2"
    options.deviceName = "Android Emulator"
    options.platformVersion = "15"

    options.appPackage = "calculator.currencyconverter.tipcalculator.unitconverter"
    options.appActivity = ".MainActivity"

    options.noReset = False

    return webdriver.Remote(
        command_executor="http://127.0.0.1:4723",
        options=options
    )
