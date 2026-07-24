import pytest
import time
from utils.driver_factory import create_android_driver

TIMEOUT = 30

@pytest.fixture
def driver():
    driver = create_android_driver()
    time.sleep(15)
    yield driver

    try:
        driver.terminate_app("calculator.currencyconverter.tipcalculator.unitconverter")
    except Exception:
        pass

    try:
        driver.quit()
    except Exception:
        pass
