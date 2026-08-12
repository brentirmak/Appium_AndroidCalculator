from appium import webdriver
from appium.options.android import UiAutomator2Options


def create_android_driver():
    options = UiAutomator2Options()

    # Core Device Settings
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"

    # Bind EXPLICITLY to the Windows Pixel 10 emulator
    #options.set_capability("appium:udid", "127.0.0.1:5555")
    options.set_capability("appium:udid", "192.168.150.1:5555")
    options.set_capability("appium:deviceName", "Tunneled-Pixel10")

    # App Settings (correct values from dumpsys)
    options.app_package = "calculator.currencyconverter.tipcalculator.unitconverter"
    options.app_activity = "calculator.currencyconverter.tipcalculator.unitconverter.ui.splash.SplashActivity"

    # Allow Appium to wait for ANY activity after launch
    options.set_capability("appium:appWaitActivity", "*")

    # Do not block waiting for SplashActivity readiness
    options.set_capability("appium:appWaitForLaunch", False)

    # Permissions & Reset State
    options.auto_grant_permissions = True
    options.no_reset = False

    # Timeouts for Jenkins / slow CI agents
    options.set_capability("appium:adbExecTimeout", 300000)
    options.set_capability("appium:appWaitDuration", 120000)
    options.set_capability("appium:uiautomator2ServerLaunchTimeout", 300000)
    options.set_capability("appium:uiautomator2ServerInstallTimeout", 300000)
    options.set_capability("appium:androidInstallTimeout", 300000)
    options.set_capability("appium:newCommandTimeout", 300)

    # Speed Optimizations
    options.set_capability("appium:disableWindowAnimation", True)

    # Initialize Driver (Ubuntu Appium server)
    driver = webdriver.Remote(
        command_executor="http://127.0.0.1:4723",
        options=options
    )

    return driver
