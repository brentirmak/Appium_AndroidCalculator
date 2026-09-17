import pytest
import time
from pages.home_page import HomePage
from utils.helpers import appium_transaction, capture_error_snapshot

@pytest.mark.timeout(180)
@pytest.mark.dependency(name="home_loaded")
def test_home(driver):
    home = HomePage(driver)

    with appium_transaction("Home"):
        try:
            #print("Will wait 15 seconds for the application to load - then will check for the Ad/Home")
            #time.sleep(15)
            assert home.load_landing_page(), "Home screen did not load"
        except Exception:
            capture_error_snapshot(driver, "Home")
            raise