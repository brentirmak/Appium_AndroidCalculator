import pytest
import time
from utils.driver_factory import create_android_driver

TIMEOUT = 30
@pytest.fixture(scope="session")
def driver():
    driver = create_android_driver()
    yield driver
    # 1. Close the app if it's running
    try:
        driver.terminate_app("calculator.currencyconverter.tipcalculator.unitconverter")
    except Exception:
        pass

    # 2. Force-stop the app (more reliable on Android 17)
    try:
        driver.execute_script(
            "mobile: shell",
            {
                "command": "am",
                "args": ["force-stop", "calculator.currencyconverter.tipcalculator.unitconverter"]
            }
        )
    except Exception:
        pass

    # 3. Quit the Appium session
    try:
        driver.quit()
    except Exception:
        pass
