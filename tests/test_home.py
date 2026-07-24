import pytest
import time
from pages.home_page import HomePage
from utils.helpers import appium_transaction, capture_error_snapshot

@pytest.mark.timeout(120)
def test_home(driver):
    #time.sleep(15)
    home = HomePage(driver)

    with appium_transaction("Home"):
        if not home.verify_home_loaded():
            capture_error_snapshot(driver, "Home")
            raise AssertionError("Home screen did not load")
