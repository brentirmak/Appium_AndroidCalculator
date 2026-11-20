'''
11/13/26 - 63 transactions
Still need to implement mm and dm conversions
'''

import pytest
import time
from pages.side_menu_page import SideMenuPage
from pages.home_page import HomePage
from pages.unit_converter_page import UnitConverterPage
from utils.helpers import appium_transaction, capture_error_snapshot

@pytest.mark.timeout(300)
def test_access_unit_converter(driver):
    side_menu = SideMenuPage(driver)
    unit_converter_page = UnitConverterPage(driver)
    home = HomePage(driver)

    with appium_transaction("Access Unit Converter"):
        print("Checking to see if we're at Home screen")
        if not home.load_landing_page():
            print("Not at Home screen")
        try:
            print("Will click on the side menu item for Unit Converter")
            side_menu.go_unit_converter()
            is_displayed, page_title = unit_converter_page.verify_loaded()

            assert is_displayed, "Unit Converter header is not displayed"
            assert page_title == "Unit Converter", f"Expected page title 'Unit Converter' but found '{page_title}'"

            unit_converter_page.click_conversion_type_option()
            unit_converter_page.select_conversion_type_value("Data")

            conversion_type = unit_converter_page.get_conversion_type()
            assert conversion_type == "Data", f"Expected 'Data' but got '{conversion_type}'"
        except Exception:
            capture_error_snapshot(driver, "AccessUnitConverter")
            raise

############################################################################################
# GB
############################################################################################
@pytest.mark.timeout(175)
def test_perform_gb_to_mb_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform GBToMB Conversion1"):
        try:
            print("Will calculate the data in MB")
            output = unit_converter_page.convert_data("GB","325","MB")
            print("Calculated the length - will confirm it's 332,800 MB")
            assert output == "332,800", f"Expected 332,800 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformGBToMBConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_gb_to_mb_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform GBToMB Conversion2"):
        try:
            print("Will calculate the data in MB")
            output = unit_converter_page.convert_data("GB","9.5","MB")
            print("Calculated the length - will confirm it's 9,728 MB")
            assert output == "9,728", f"Expected 9,728 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformGBToMBConversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_gb_to_b_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform GBToB Conversion1"):
        try:
            print("Will calculate the data in B")
            output = unit_converter_page.convert_data("GB","0.005","B")
            print("Calculated the length - will confirm it's 5,368,709.12 B")
            assert output == "5,368,709.12", f"Expected 5,368,709.12 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformGBToBConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_gb_to_b_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform GBToB Conversion2"):
        try:
            print("Will calculate the data in B")
            output = unit_converter_page.convert_data("GB","0.00037","B")
            print("Calculated the length - will confirm it's 397,284.47488 B")
            assert output == "397,284.47488", f"Expected 397,284.47488 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformGBToBConversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_gb_to_kb_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform GBToKB Conversion1"):
        try:
            print("Will calculate the data in KB")
            output = unit_converter_page.convert_data("GB","6","KB")
            print("Calculated the length - will confirm it's 6,291,456 KB")
            assert output == "6,291,456", f"Expected 6,291,456 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformGBToKBConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_gb_to_kb_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform GBToKB Conversion2"):
        try:
            print("Will calculate the data in KB")
            output = unit_converter_page.convert_data("GB","0.3","KB")
            print("Calculated the length - will confirm it's 314,572.8 KB")
            assert output == "314,572.8", f"Expected 314,572.8 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformGBToKBConversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_gb_to_tb_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform GBToTB Conversion1"):
        try:
            print("Will calculate the data in TB")
            output = unit_converter_page.convert_data("GB","7796","TB")
            print("Calculated the length - will confirm it's 7.61328 TB")
            assert output == "7.61328", f"Expected 7.61328 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformGBToTBConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_gb_to_tb_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform GBToTB Conversion2"):
        try:
            print("Will calculate the data in TB")
            output = unit_converter_page.convert_data("GB","8888.11","TB")
            print("Calculated the length - will confirm it's 8.67979 TB")
            assert output == "8.67979", f"Expected 8.67979 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformGBToTBConversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_gb_to_bit_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform GBTobit Conversion1"):
        try:
            print("Will calculate the data in bit")
            output = unit_converter_page.convert_data("GB","0.004","b")
            print("Calculated the length - will confirm it's 34,359,738.368 bit")
            assert output == "34,359,738.368", f"Expected 34,359,738.368 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformGBTobitConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_gb_to_bit_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform GBTobit Conversion2"):
        try:
            print("Will calculate the data in bit")
            output = unit_converter_page.convert_data("GB","0.00000555","b")
            print("Calculated the length - will confirm it's 47,674.13699 bit")
            assert output == "47,674.13699", f"Expected 47,674.13699 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformGBTobitConversion2")
            raise