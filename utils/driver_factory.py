from appium import webdriver
from appium.options.android import UiAutomator2Options


def create_android_driver():
    options = UiAutomator2Options()

    # Core Device Settings
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.device_name = "Android Emulator"

    # App Settings
    options.app_package = "calculator.currencyconverter.tipcalculator.unitconverter"

    # Allow Appium to wait for ANY activity to load after launch
    options.set_capability("appium:appWaitActivity", "*")

    # CRUCIAL: Do not block am start waiting for SplashActivity to report readiness
    options.set_capability("appium:appWaitForLaunch", False)

    # Permissions & Reset State
    options.auto_grant_permissions = True
    options.no_reset = False

    # Timeouts for Jenkins / slow CI agents
    options.set_capability("appium:adbExecTimeout", 300000)  # 5 mins
    options.set_capability("appium:appWaitDuration", 120000)  # 2 mins
    options.set_capability("appium:uiautomator2ServerLaunchTimeout", 300000)  # 5 mins
    options.set_capability("appium:uiautomator2ServerInstallTimeout", 300000)  # 5 mins
    options.set_capability("appium:androidInstallTimeout", 300000)  # 5 mins
    options.set_capability("appium:newCommandTimeout", 300)  # 5 mins

    # Speed Optimizations
    options.set_capability("appium:disableWindowAnimation", True)

    # Initialize Driver
    driver = webdriver.Remote(
        command_executor="http://127.0.0.1:4723",
        options=options
    )

    return driver