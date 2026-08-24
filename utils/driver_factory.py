from appium import webdriver
from appium.options.android import UiAutomator2Options
import os


def create_android_driver():
    options = UiAutomator2Options()

    # =========================================================================
    # PLATFORM / AUTOMATION
    # =========================================================================

    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"

    # =========================================================================
    # REMOTE ANDROID DEVICE
    #
    # Jenkins runs on Ubuntu.
    # The Android emulator runs on Windows.
    #
    # Linux ADB connects directly to:
    #
    #     192.168.150.1:5555
    #
    # Do NOT use:
    #
    #     emulator-5554
    #     127.0.0.1:5555
    #
    # because those refer to the Windows/local emulator transport.
    # =========================================================================

    android_device = os.getenv(
        "ANDROID_SERIAL",
        "192.168.150.1:5555"
    )

    options.set_capability(
        "appium:udid",
        android_device
    )

    options.set_capability(
        "appium:deviceName",
        "Tunneled-Pixel10"
    )

    # =========================================================================
    # APPLICATION
    # =========================================================================

    options.app_package = (
        "calculator.currencyconverter.tipcalculator.unitconverter"
    )

    options.app_activity = (
        "calculator.currencyconverter.tipcalculator.unitconverter"
        ".ui.splash.SplashActivity"
    )

    # Allow the application to transition from SplashActivity to
    # whatever activity becomes active.
    options.set_capability(
        "appium:appWaitActivity",
        "*"
    )

    options.set_capability(
        "appium:appWaitForLaunch",
        False
    )

    # =========================================================================
    # APPLICATION STATE / PERMISSIONS
    # =========================================================================

    options.auto_grant_permissions = True
    # If the target app is already installed on Pixel_10, set noReset to True in your Appium capabilities setup
    options.no_reset = True

    # =========================================================================
    # JENKINS / SLOW EMULATOR TIMEOUTS
    # =========================================================================

    options.set_capability(
        "appium:adbExecTimeout",
        300000
    )

    options.set_capability(
        "appium:appWaitDuration",
        120000
    )

    options.set_capability(
        "appium:uiautomator2ServerLaunchTimeout",
        300000
    )

    options.set_capability(
        "appium:uiautomator2ServerInstallTimeout",
        300000
    )

    options.set_capability(
        "appium:androidInstallTimeout",
        300000
    )

    options.set_capability(
        "appium:newCommandTimeout",
        300
    )

    # =========================================================================
    # PERFORMANCE
    # =========================================================================

    options.set_capability(
        "appium:disableWindowAnimation",
        True
    )

    # =========================================================================
    # DEBUG INFORMATION
    # =========================================================================

    print()
    print("==============================================================")
    print("APPIUM DRIVER CONFIGURATION")
    print("==============================================================")
    print(f"Platform:          Android")
    print(f"Automation:       UiAutomator2")
    print(f"Device UDID:      {android_device}")
    print(f"Device Name:      Tunneled-Pixel10")
    print(
        "App Package:      "
        "calculator.currencyconverter.tipcalculator.unitconverter"
    )
    print(
        "App Activity:     "
        "calculator.currencyconverter.tipcalculator.unitconverter"
        ".ui.splash.SplashActivity"
    )
    print("Appium Server:     http://127.0.0.1:4723")
    print("==============================================================")
    print()

    # =========================================================================
    # CREATE APPIUM SESSION
    # =========================================================================

    driver = webdriver.Remote(
        command_executor="http://127.0.0.1:4723",
        options=options
    )

    return driver