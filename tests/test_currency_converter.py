'''
11/11/26 - 10 tests
'''
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
            is_displayed, page_title = currency_converter_page.verify_loaded()

            assert is_displayed, "Currency Converter header is not displayed"
            assert page_title == "Currency Converter", f"Expected page title 'Currency Converter' but found '{page_title}'"

        except Exception:
            capture_error_snapshot(driver, "AccessCurrencyConverter")
            raise


@pytest.mark.timeout(175)
def test_perform_usd_to_yen_conversion(driver):
    currency_converter_page = CurrencyConverterPage(driver)

    with appium_transaction("Perform USD to Yen Currency Conversion"):
        try:
            print("Will calculate the USD to Japanese Yen")
            output = currency_converter_page.convert_currency("USD", 100, "JPY")

            output_value = float(output.replace(",", ""))

            print("Calculated the $ conversion - will confirm it's between 15,000 and 16,500 Yen")
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

    print("Will open the menu and click on the Currency Converter option")
    side_menu_page.click_currency_converter()
    print("Clicked on the Currency Converter option")
    time.sleep(5)

    with appium_transaction("Perform GBP to TR Lira Currency Conversion"):
        try:
            print("Will calculate the GBP to Turkish Lira")
            output = currency_converter_page.convert_currency("GBP", 100, "TRY")

            output_value = float(output.replace(",", ""))

            print("Calculated the GBP conversion - will confirm it's between 6000 and 7500 Turkish Lira")
            assert 6000 <= output_value <= 7500, (
                f"Expected value between 6000 and 7500 but got {output_value}"
            )
        except Exception:
            capture_error_snapshot(driver, "PerformGBPToTRLiraCurrencyConversion")
            raise

@pytest.mark.timeout(175)
def test_perform_usd_to_gbp_conversion(driver):
    currency_converter_page = CurrencyConverterPage(driver)
    side_menu_page = SideMenuPage(driver)

    print("Will open the menu and click on the Currency Converter option")
    side_menu_page.click_currency_converter()
    print("Clicked on the Currency Converter option")
    time.sleep(5)

    with appium_transaction("Perform USD to GBP Currency Conversion"):
        try:
            print("Will calculate USD to GBP")
            output = currency_converter_page.convert_currency("USD", 395, "GBP")

            output_value = float(output.replace(",", ""))

            print("Calculated the USD conversion - will confirm it's between 280.00 and 320.00 GBP")
            assert 280.00 <= output_value <= 320.00, (
                f"Expected value between 280.00 and 320.00 but got {output_value}"
            )
        except Exception:
            capture_error_snapshot(driver, "PerformUSDToGBPCurrencyConversion")
            raise


@pytest.mark.timeout(175)
def test_perform_eur_to_mxn_conversion(driver):
    currency_converter_page = CurrencyConverterPage(driver)
    side_menu_page = SideMenuPage(driver)

    print("Will open the menu and click on the Currency Converter option")
    side_menu_page.click_currency_converter()
    print("Clicked on the Currency Converter option")
    time.sleep(5)

    with appium_transaction("Perform EUR to MXN Currency Conversion"):
        try:
            print("Will calculate EUR to MXN")
            output = currency_converter_page.convert_currency("EUR", 100, "MXN")
            output_value = float(output.replace(",", ""))

            print("Calculated the USD conversion - will confirm it's between 1,900 and 2,700 MXN")
            assert 1900.00 <= output_value <= 2700.00, (
                f"Expected value between 1,900 and 2,700 but got {output_value}"
            )
        except Exception:
            capture_error_snapshot(driver, "PerformEURToMXNCurrencyConversion")
            raise

@pytest.mark.timeout(175)
def test_perform_cad_to_aud_conversion(driver):
    currency_converter_page = CurrencyConverterPage(driver)
    side_menu_page = SideMenuPage(driver)

    print("Will open the menu and click on the Currency Converter option")
    side_menu_page.click_currency_converter()
    print("Clicked on the Currency Converter option")
    time.sleep(5)

    with appium_transaction("Perform EUR to MXN Currency Conversion"):
        try:
            print("Will calculate EUR to MXN")
            output = currency_converter_page.convert_currency("CAD", 765, "AUD")
            output_value = float(output.replace(",", ""))

            print("Calculated the USD conversion - will confirm it's between 1,900 and 2,300 MXN")
            assert 770.0 <= output_value <= 800.0, (
                f"Expected value between 770.0 and 800.0 but got {output_value}"
            )
        except Exception:
            capture_error_snapshot(driver, "PerformCADToAUDCurrencyConversion")
            raise

@pytest.mark.timeout(175)
def test_perform_cop_to_inr_conversion(driver):
    currency_converter_page = CurrencyConverterPage(driver)
    side_menu_page = SideMenuPage(driver)

    print("Will open the menu and click on the Currency Converter option")
    side_menu_page.click_currency_converter()
    print("Clicked on the Currency Converter option")
    time.sleep(5)

    with appium_transaction("Perform COP to INR Currency Conversion"):
        try:
            print("Will calculate COP to INR")
            output = currency_converter_page.convert_currency("COP", 325985, "INR")
            output_value = float(output.replace(",", ""))

            print("Calculated the COP conversion - will confirm it's between 9,000 and 10,000 INR")
            assert 9000 <= output_value <= 10000, (
                f"Expected value between 9000 and 10000 but got {output_value}"
            )
        except Exception:
            capture_error_snapshot(driver, "PerformCOPToINRCurrencyConversion")
            raise

@pytest.mark.timeout(175)
def test_perform_krw_to_usd_conversion(driver):
    currency_converter_page = CurrencyConverterPage(driver)
    side_menu_page = SideMenuPage(driver)

    print("Will open the menu and click on the Currency Converter option")
    side_menu_page.click_currency_converter()
    print("Clicked on the Currency Converter option")
    time.sleep(5)

    with appium_transaction("Perform KRW to USD Currency Conversion"):
        try:
            print("Will calculate KRW to USD")
            output = currency_converter_page.convert_currency("KRW", 95280, "USD")
            output_value = float(output.replace(",", ""))

            print("Calculated the KRW conversion - will confirm it's between 65 and 75 USD")
            assert 65.00 <= output_value <= 75.00, (
                f"Expected value between 65 and 75 but got {output_value}"
            )
        except Exception:
            capture_error_snapshot(driver, "PerformKRWToUSDCurrencyConversion")
            raise

@pytest.mark.timeout(175)
def test_perform_hkd_to_jpy_conversion(driver):
    currency_converter_page = CurrencyConverterPage(driver)
    side_menu_page = SideMenuPage(driver)

    print("Will open the menu and click on the Currency Converter option")
    side_menu_page.click_currency_converter()
    print("Clicked on the Currency Converter option")
    time.sleep(5)

    with appium_transaction("Perform HKD to JPY Currency Conversion"):
        try:
            print("Will calculate HKD to JPY")
            output = currency_converter_page.convert_currency("HKD", 275, "JPY")
            output_value = float(output.replace(",", ""))

            print("Calculated the HKD conversion - will confirm it's between 65 and 75 JPY")
            assert 4750.00 <= output_value <= 6000.00, (
                f"Expected value between 4750 and 6000 but got {output_value}"
            )
        except Exception:
            capture_error_snapshot(driver, "PerformHKDToJPYCurrencyConversion")
            raise

@pytest.mark.timeout(175)
def test_perform_try_to_eur_conversion(driver):
    currency_converter_page = CurrencyConverterPage(driver)
    side_menu_page = SideMenuPage(driver)

    print("Will open the menu and click on the Currency Converter option")
    side_menu_page.click_currency_converter()
    print("Clicked on the Currency Converter option")
    time.sleep(5)

    with appium_transaction("Perform TRY to EUR Currency Conversion"):
        try:
            print("Will calculate TRY to EUR")
            output = currency_converter_page.convert_currency("TRY", 663311, "EUR")
            output_value = float(output.replace(",", ""))

            print("Calculated the HKD conversion - will confirm it's between 1850000.00 and 2500000.00 EUR")
            assert 11500.00 <= output_value <= 12500.00, (
                f"Expected value between 11500 and 12500 but got {output_value}"
            )
        except Exception:
            capture_error_snapshot(driver, "PerformTRYToEURCurrencyConversion")
            raise