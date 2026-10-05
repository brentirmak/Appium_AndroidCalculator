import pytest
import time
from pages.side_menu_page import SideMenuPage
from pages.home_page import HomePage
from pages.currency_converter_page import CurrencyConverterPage
from utils.helpers import appium_transaction, capture_error_snapshot

@pytest.mark.timeout(300)
def test_access_currency_converter(driver):
    side_menu = SideMenuPage(driver)
    currency_converter_page = CurrencyConverterPage(driver)
    home = HomePage(driver)

    with appium_transaction("Access Currency Converter"):
        print("Checking to see if we're at Home screen")
        if not home.load_landing_page():
            print("Not at Home screen")
        try:
            print("Will click on the side menu item for Currency Converter")
            side_menu.click_currency_converter()
            assert currency_converter_page.verify_loaded(), "Currency Converter header not found"
        except Exception:
            capture_error_snapshot(driver, "AccessCurrencyConverter")
            raise


@pytest.mark.timeout(175)
def test_perform_usd_to_yen_conversion(driver):
    currency_converter_page = CurrencyConverterPage(driver)

    with appium_transaction("Perform USD to Yen Currency Conversion"):
        try:
            print("Will calculate the USD to Japanese Yen")
            output = currency_converter_page.convert_usd_to_yen()

            output_value = float(output.replace(",", ""))

            print("Calculated the $ conversion- will confirm it's between 15,000 and 16,500 Yen")
            assert 15000 <= output_value <= 16500, (
                f"Expected value between 15,000 and 16,500 but got {output_value}"
            )
        except Exception:
            capture_error_snapshot(driver, "PerformUSDToYenCurrencyConversion")
            raise

@pytest.mark.timeout(175)
def test_perform_gbp_to_lira_conversion(driver):
    currency_converter_page = CurrencyConverterPage(driver)
    side_menu_page = SideMenuPage(driver)

    print("Will open the manu and click on the Currency Converter option")
    side_menu_page.click_currency_converter()
    print("Clicked on the Currency Converter option")
    time.sleep(5)

    with appium_transaction("Perform GBP to TR Lira Currency Conversion"):
        try:
            print("Will calculate the GBP to Turkish Lira")
            output = currency_converter_page.convert_gbp_to_trl()

            output_value = float(output.replace(",", ""))

            print("Calculated the GBP conversion- will confirm it's between 6000 and 7500 Turkish Lira")
            assert 6000 <= output_value <= 7500, (
                f"Expected value between 6000 and 7500 but got {output_value}"
            )
        except Exception:
            capture_error_snapshot(driver, "PerformGBPToTRLiraCurrencyConversion")
            raise
