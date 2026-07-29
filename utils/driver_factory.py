from appium import webdriver
from appium.options.android import UiAutomator2Options


def create_android_driver():
    options = UiAutomator2Options()

    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.device_name = "Android Emulator"

    options.app_package = "calculator.currencyconverter.tipcalculator.unitconverter"

    # Use Monkey execution to launch the app as a fresh user action
    options.set_capability("appium:appActivity", "")  # Omit or set empty
    options.set_capability("appium:userTyping", True)

    # Key setting: tells Appium to launch via app icon / launcher intent
    options.set_capability("appium:appWaitForLaunch", True)

    options.auto_grant_permissions = True
    options.no_reset = False

    driver = webdriver.Remote(
        command_executor="http://127.0.0.1:4723",
        options=options
    )

    return driver