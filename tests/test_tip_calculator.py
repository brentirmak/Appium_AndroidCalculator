import pytest
from pages.side_menu_page import SideMenuPage
from pages.tip_calculator_page import TipCalculatorPage
from utils.helpers import appium_transaction, capture_error_snapshot

@pytest.mark.timeout(45)
def test_access_tip_calculator(driver):
    side_menu = SideMenuPage(driver)
    tip_page = TipCalculatorPage(driver)

    with appium_transaction("Access Tip Calculator"):
        try:
            side_menu.go_tip_calculator()
            assert tip_page.verify_loaded(), "Tip header not found"
        except Exception:
            capture_error_snapshot(driver, "AccessTipCalculator")
            raise


@pytest.mark.timeout(45)
def test_perform_tip_calculation(driver):
    tip_page = TipCalculatorPage(driver)

    with appium_transaction("Perform Tip Calculation"):
        try:
            tip_page.clear_previous_entries()
            assert tip_page.verify_loaded(), "Tip header not found"

            output = tip_page.calculate_tip("100", "20")
            assert output == "120.00", f"Expected 120.00 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformTipCalculation")
            raise
