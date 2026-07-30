import pytest
import time
from pages.side_menu_page import SideMenuPage
from pages.home_page import HomePage
from pages.tip_calculator_page import TipCalculatorPage
from utils.helpers import appium_transaction, capture_error_snapshot

@pytest.mark.timeout(75)
def test_access_tip_calculator(driver):
    side_menu = SideMenuPage(driver)
    tip_page = TipCalculatorPage(driver)
    home = HomePage(driver)

    with appium_transaction("Access Tip Calculator"):
        print("Checking to see if we're at Home screen")
        if not home.verify_home_loaded():
            print("Not at Home screen")

        try:
            print("Will click on the Tip Calculator option")
            side_menu.go_tip_calculator()
            print("Clicked on the Tip Calculator option")
            assert tip_page.verify_loaded(), "Tip header not found"
        except Exception:
            capture_error_snapshot(driver, "AccessTipCalculator")
            raise

@pytest.mark.timeout(75)
def test_perform_tip_calculation(driver):
    tip_page = TipCalculatorPage(driver)

    with appium_transaction("Perform Tip Calculation"):
        try:
            print("Clearing previous input on the Tip Page")
            tip_page.clear_previous_entries()
            print("Cleared previous input on the Tip Page")
            assert tip_page.verify_loaded(), "Tip header not found"
            print("Verify tip page loaded properly")

            print("Will calculate the tip and total values using the calculator")
            output = tip_page.calculate_tip("100", "20")
            print("Calculated the tip and total values using the calculator - will confirm it's 120.00")
            assert output == "120.00", f"Expected 120.00 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformTipCalculation")
            raise
