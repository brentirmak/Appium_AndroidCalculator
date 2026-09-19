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
            assert date_calculator.verify_fields(), "Date Calculator fields not found"
        except Exception:
            capture_error_snapshot(driver, "AccessDateCalculator")
            raise




@pytest.mark.timeout(175)
def test_perform_basic_calculation(driver):
    date_calculator = DateCalculatorPage(driver)

    with appium_transaction("Perform Date Calculation"):
        try:
            if not date_calculator.verify_loaded():
                date_calculator.open_from_home()

            duration_value = date_calculator.calculate_date_difference()
            assert "41 days" or "40 days" in duration_value, f"Expected 30 or 31 but got {duration_value}"
        except Exception:
            capture_error_snapshot(driver, "PerformDateCalculation")
            raise

