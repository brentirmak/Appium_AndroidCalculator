import pytest
import time
from pages.side_menu_page import SideMenuPage
from pages.home_page import HomePage
from pages.bmi_calculator_page import BMICalculatorPage
from utils.helpers import appium_transaction, capture_error_snapshot

@pytest.mark.timeout(300)
def test_access_bmi_calculator(driver):
    side_menu = SideMenuPage(driver)
    bmi_calculator_page = BMICalculatorPage(driver)
    home = HomePage(driver)

    with appium_transaction("Access BMI Calculator"):
        print("Checking to see if we're at Home screen")
        if not home.load_landing_page():
            print("Not at Home screen")
        try:
            print("Will click on the side menu item for BMI Calculator")
            side_menu.click_bmi_calculator()
            assert bmi_calculator_page.verify_loaded(), "BMI Calculator header not found"
        except Exception:
            capture_error_snapshot(driver, "Access BMI Calculator")
            raise





