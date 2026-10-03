import pytest
import time
from pages.side_menu_page import SideMenuPage
from pages.home_page import HomePage
from pages.loan_calculator_page import LoanCalculatorPage
from utils.helpers import appium_transaction, capture_error_snapshot

@pytest.mark.timeout(300)
def test_access_loan_calculator(driver):
    side_menu = SideMenuPage(driver)
    loan_calculator_page = LoanCalculatorPage(driver)
    home = HomePage(driver)

    with appium_transaction("Access Loan Calculator"):
        print("Checking to see if we're at Home screen")
        if not home.load_landing_page():
            print("Not at Home screen")
        try:
            print("Will click on the side menu item for Loan Calculator")
            side_menu.click_loan_calculator()
            assert loan_calculator_page.verify_loaded(), "Loan Calculator header not found"
        except Exception:
            capture_error_snapshot(driver, "AccessLoanCalculator")
            raise

@pytest.mark.timeout(175)
def test_perform_equal_principle_payment_loan_calculation(driver):
    loan_calculator_page = LoanCalculatorPage(driver)

    with appium_transaction("PerformEqualPrinciplePaymentLoanCalculation"):
        try:
            print("Will calculate the loan")
            output = loan_calculator_page.calculate_equal_principal_payment_repayment_loan()
            print("Calculated the loan - will confirm it's 50.21")
            assert output == "50.21", f"Expected 50.21 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformEqualPrinciplePaymentLoanCalculation")
            raise
