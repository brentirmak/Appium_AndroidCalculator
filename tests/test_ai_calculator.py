import pytest
from pages.home_page import HomePage
from pages.ai_calculator_page import AICalculatorPage
from utils.helpers import appium_transaction, capture_error_snapshot
from datetime import datetime, timedelta

future_date = datetime.now() + timedelta(days=60)
formatted_future_date = f"{future_date:%b} {future_date.day}, {future_date:%Y}"
print(formatted_future_date)  # e.g. Nov 17, 2026

@pytest.mark.timeout(300)
def test_access_date_calculator(driver):
    home = HomePage(driver)
    ai_calculator = AICalculatorPage(driver)

    with appium_transaction("Access Date Calculator"):
        if not home.load_landing_page():
            print("Not at Home screen")

        try:
            ai_calculator.open_from_home()
            page_header = ai_calculator.verify_loaded()
            assert "AI Scan" in page_header, f"AI Scan header not found. Got: '{page_header}'"
            print("AI Scan header found")
        except AssertionError:
            capture_error_snapshot(driver, "AccessDateCalculator")
            raise
        except Exception:
            capture_error_snapshot(driver, "AccessDateCalculator")
            raise

@pytest.mark.timeout(175)
def test_perform_ai_chat_calculation(driver):
    ai_calculator = AICalculatorPage(driver)

    with appium_transaction("Perform AI Chat Calculation"):
        try:
            if not ai_calculator.verify_loaded():
                ai_calculator.open_from_home()

            ai_calculator.access_ai_chat_screen()
            simple_addition_result = ai_calculator.perform_simple_addition()

            assert ("4" in simple_addition_result), f"Expected 4 but got {simple_addition_result}"
        except Exception:
            capture_error_snapshot(driver, "PerformAIChatCalculation")
            raise

'''
@pytest.mark.timeout(175)
def test_perform_basic_calculation(driver):
    date_calculator = DateCalculatorPage(driver)

    with appium_transaction("Perform Date Calculation"):
        try:
            if not date_calculator.verify_loaded():
                date_calculator.open_from_home()

            duration_value = date_calculator.calculate_date_difference()
            assert ("41 days" in duration_value) or ("40 days" in duration_value), f"Expected 40 or 41 but got {duration_value}"
        except Exception:
            capture_error_snapshot(driver, "PerformDateCalculation")
            raise

@pytest.mark.timeout(175)
def test_perform_alternative_calculation(driver):
    date_calculator = DateCalculatorPage(driver)

    with appium_transaction("Perform Alternative Date Calculation"):
        try:
            if not date_calculator.verify_loaded():
                date_calculator.open_from_home()

            duration_value = date_calculator.calculate_to_date()

            assert (formatted_future_date in duration_value), f"Expected {formatted_future_date} to be within {duration_value}"
        except Exception:
            capture_error_snapshot(driver, "PerformAlternativeDateCalculation")
            raise
'''