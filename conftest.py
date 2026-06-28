import pytest
import os
from utils import StoreToMySQL
from appium import webdriver
from appium.options.common import AppiumOptions
from dotenv import load_dotenv
from utils.helpers import trx_dict

# Shared container so pytest_sessionfinish can access device_info
collected_device_info = []

@pytest.fixture(scope="session")
def driver():
    load_dotenv()
    webdriver_remote_url = os.getenv("WEBDRIVER_REMOTE_URL")

    options = AppiumOptions()
    options.load_capabilities({
        "platformName": "Android",
        "appium:deviceName": "emulator-5554",
        "appium:automationName": "UiAutomator2",
        "appium:appPackage": "calculator.currencyconverter.tipcalculator.unitconverter",
        "appium:appActivity": ".MainActivity",
        "appium:appWaitActivity": "*",
        "appium:forceAppLaunch": True,
        "appium:autoLaunch": True,
        "appium:appWaitDuration": 30000,
        "appium:autoGrantPermissions": True,
        "appium:adbExecTimeout": 60000,
        "appium:uiautomator2ServerLaunchTimeout": 60000,  # ms — time to launch UIA2 server
        "appium:uiautomator2ServerInstallTimeout": 60000,  # already have this — good
        "appium:mjpegServerPort": 7810,  # avoid port conflicts with UIA2 stream
        "appium:skipServerInstallation": False,  # ensure fresh UIA2 server each session
        "appium:newCommandTimeout": 300,
        "appium:waitForIdleTimeout": 0,
        "appium:waitForSelectorTimeout": 10000,
        "appium:disableWindowAnimation": True
    })

    drv = webdriver.Remote(webdriver_remote_url, options=options)
    drv.implicitly_wait(15)

    yield drv

    drv.terminate_app("calculator.currencyconverter.tipcalculator.unitconverter")
    drv.quit()

@pytest.fixture(scope="session", autouse=True)
def device_info(driver):
    caps = driver.capabilities
    info = driver.execute_script("mobile: deviceInfo")

    if info["model"] == "sdk_gphone16k_x86_64":
        info["model"] = "Pixel 10 Emulator"

    data = [
        caps.get("platformName"),
        caps.get("platformVersion"),
        info["model"],
        info["manufacturer"]
    ]

    # Populate the shared container so pytest_sessionfinish can access it
    collected_device_info.extend(data)

    return data

def pytest_sessionfinish(session, exitstatus):
    print("\nStoring results to MySQL...")
    StoreToMySQL.store_to_mysql(trx_dict, collected_device_info)
    print("Results stored successfully")

def pytest_runtest_makereport(item, call):
    if call.excinfo is not None:
        item.session._shouldstop = True