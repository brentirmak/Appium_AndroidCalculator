import pytest
from pages.home_page import HomePage
from pages.basic_calculator_page import BasicCalculatorPage
from pages.side_menu_page import SideMenuPage
from utils.helpers import appium_transaction, capture_error_snapshot

@pytest.mark.timeout(45)
def test_access_basic_calculator(driver):
    home = HomePage(driver)
    calc = BasicCalculatorPage(driver)
    side_menu = SideMenuPage(driver)

    with appium_transaction("Access Basic Calculator"):
        if not home.verify_home_loaded():
            print("Not at Home screen")

        try:
            calc.open_from_home()
            assert calc.verify_loaded(), "Basic Calculator header not found"
        except Exception:
            capture_error_snapshot(driver, "AccessBasicCalculator")
            raise


@pytest.mark.timeout(45)
def test_perform_basic_calculation(driver):
    calc = BasicCalculatorPage(driver)

    with appium_transaction("Perform Basic Calculation"):
        try:
            if not calc.verify_loaded():
                calc.open_from_home()

            output = calc.calculate_9_plus_9()
            assert output == "= 18", f"Expected 18 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformBasicCalculation")
            raise

