import pytest
from pages.side_menu_page import SideMenuPage
from pages.home_page import HomePage
from utils.helpers import appium_transaction, capture_error_snapshot

@pytest.mark.timeout(45)
def test_go_back_to_home(driver):
    side_menu = SideMenuPage(driver)
    home = HomePage(driver)

    with appium_transaction("Go Back To Home"):
        try:
            side_menu.go_home()
            assert home.verify_home_loaded(), "Home screen not detected"
        except Exception:
            capture_error_snapshot(driver, "GoBackToHome")
            raise
