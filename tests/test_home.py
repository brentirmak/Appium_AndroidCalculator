import pytest
from pages.home_page import HomePage
from utils.helpers import appium_transaction, capture_error_snapshot

@pytest.mark.timeout(45)
def test_home(driver):
    home = HomePage(driver)

    with appium_transaction("Home"):
        if not home.verify_home_loaded():
            capture_error_snapshot(driver, "Home")
            raise AssertionError("Home screen did not load")
