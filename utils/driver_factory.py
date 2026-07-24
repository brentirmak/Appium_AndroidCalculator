from appium import webdriver
from appium.options.android import UiAutomator2Options
import time

def create_android_driver():
    options = UiAutomator2Options()

    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.device_name = "Android Emulator"
    options.platform_version = "17"

    options.app_package = "calculator.currencyconverter.tipcalculator.unitconverter"
    options.app_activity = ".ui.splash.SplashActivity"

    options.app_wait_activity = "*"
    options.app_wait_package = "calculator.currencyconverter.tipcalculator.unitconverter"
    options.app_wait_duration = 60000
    options.app_wait_for_launch = True

    options.intent_action = "android.intent.action.MAIN"
    options.intent_category = "android.intent.category.LAUNCHER"

    options.auto_grant_permissions = True
    options.ensure_webviews_have_pages = True
    options.auto_launch = True
    options.no_reset = False

    options.uiautomator2_server_launch_timeout = 180000
    options.adb_exec_timeout = 120000
    options.new_command_timeout = 120

    time.sleep(5)

    return webdriver.Remote(
        command_executor="http://127.0.0.1:4723",
        options=options
    )

