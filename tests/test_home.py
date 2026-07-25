import pytest
from pages.home_page import HomePage
from utils.helpers import appium_transaction, capture_error_snapshot

@pytest.mark.timeout(120)
@pytest.mark.dependency(name="home_loaded")
def test_home(driver):
    home = HomePage(driver)

    with appium_transaction("Home"):
        try:
            assert home.verify_home_loaded(), "Home screen did not load"
        except Exception:
            capture_error_snapshot(driver, "Home")
            raise
