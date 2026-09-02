import pytest
from pages.side_menu_page import SideMenuPage
from pages.home_page import HomePage
from pages.discount_calculator_page import DiscountCalculatorPage
from utils.helpers import appium_transaction, capture_error_snapshot

@pytest.mark.timeout(300)
def test_access_discount_calculator(driver):
    side_menu = SideMenuPage(driver)
    discount_calculator_page = DiscountCalculatorPage(driver)
    home = HomePage(driver)

    with appium_transaction("Access Discount Calculator"):
        print("Checking to see if we're at Home screen")
        if not home.verify_home_loaded():
            print("Not at Home screen")

        try:
            print("Will click on the Discount Calculator option")
            side_menu.click_discount_calculator()
            print("Clicked on the Discount Calculator option")
            assert discount_calculator_page.verify_loaded(), "Discount header not found"
        except Exception:
            capture_error_snapshot(driver, "AccessDiscountCalculator")
            raise

@pytest.mark.timeout(175)
def test_perform_discount_calculation(driver):
    discount_calculator_page = DiscountCalculatorPage(driver)

    with appium_transaction("Perform Discount Calculation"):
        try:
            try:
                print("Clearing previous input on the Discount Page")
                discount_calculator_page.clear_entries()
            except:
                print("No previous entries were seen hence there's no option to clear previous input")
            print("Cleared previous input on the Discount Page")
            assert discount_calculator_page.verify_loaded(), "Discount header not found"
            print("Verify Discount Page loaded properly")

            print("Will calculate the amount saved, tax and final price using the calculator")
            output = discount_calculator_page.calculate_discount("15", "100","5")
            print("Calculated the amount saved, tax and final price using the calculator - will confirm the values are 5.0, 14.25, 109.25")
            amount_saved, tax, price = output
            assert float(amount_saved) == 5.0, f"Amount saved mismatch: {amount_saved}"
            assert float(tax) == 14.25, f"Tax mismatch: {tax}"
            assert float(price) == 109.25, f"Price mismatch: {price}"
            # return self.find(self.FINAL_AMOUNT_SAVED_VALUE).text, self.find(self.FINAL_TAX_VALUE).text, self.find(self.FINAL_PRICE_VALUE).text
            #assert output == (5.0, 14.25, 109.25)
        except Exception:
            capture_error_snapshot(driver, "PerformDiscountCalculation")
            raise
