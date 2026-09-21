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

@pytest.mark.timeout(175)
def test_perform_2nd_ai_chat_calculation(driver):
    ai_calculator = AICalculatorPage(driver)

    with appium_transaction("Perform 2nd AI Chat Calculation"):
        try:
            if not ai_calculator.verify_loaded():
                ai_calculator.open_from_home()

            ai_calculator.access_ai_chat_screen()
            simple_subtraction_result = ai_calculator.perform_simple_subtraction()

            assert ("10" in simple_subtraction_result), f"Expected 10 but got {simple_subtraction_result}"
        except Exception:
            capture_error_snapshot(driver, "Perform2ndAIChatCalculation")
            raise