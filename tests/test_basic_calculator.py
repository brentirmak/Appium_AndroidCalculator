import pytest
from pages.home_page import HomePage
from pages.basic_calculator_page import BasicCalculatorPage
from utils.helpers import appium_transaction, capture_error_snapshot

@pytest.mark.timeout(300)
def test_access_basic_calculator(driver):
    home = HomePage(driver)
    calc = BasicCalculatorPage(driver)

    with appium_transaction("Access Basic Calculator"):
        if not home.load_landing_page():
            print("Not at Home screen")

        try:
            calc.open_from_home()
            is_displayed, page_title = calc.verify_loaded()

            assert is_displayed, "Basic Calculator header is not displayed"
            assert page_title == "Basic Calculator", f"Expected page title 'Basic Calculator' but found '{page_title}'"

        except Exception:
            capture_error_snapshot(driver, "AccessBasicCalculator")
            raise

@pytest.mark.timeout(175)
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

