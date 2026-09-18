import pytest
from pages.home_page import HomePage
from pages.date_calculator_page import DateCalculatorPage
from utils.helpers import appium_transaction, capture_error_snapshot

@pytest.mark.timeout(300)
def test_access_date_calculator(driver):
    home = HomePage(driver)
    date_calculator = DateCalculatorPage(driver)

    with appium_transaction("Access Date Calculator"):
        if not home.load_landing_page():
            print("Not at Home screen")

        try:
            date_calculator.open_from_home()
            assert date_calculator.verify_loaded(), "Date Calculator header not found"
        except Exception:
            capture_error_snapshot(driver, "AccessDateCalculator")
            raise

'''
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
'''
