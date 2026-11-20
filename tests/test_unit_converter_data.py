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
            print("Calculated the data conversion - will confirm it's 332,800 MB")
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
            print("Calculated the data conversion - will confirm it's 9,728 MB")
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
            print("Calculated the data conversion - will confirm it's 5,368,709.12 B")
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
            print("Calculated the data conversion - will confirm it's 397,284.47488 B")
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
            print("Calculated the data conversion - will confirm it's 6,291,456 KB")
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
            print("Calculated the data conversion - will confirm it's 314,572.8 KB")
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
            print("Calculated the data conversion - will confirm it's 7.61328 TB")
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
            print("Calculated the data conversion - will confirm it's 8.67979 TB")
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
            print("Calculated the data conversion - will confirm it's 34,359,738.368 bit")
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
            print("Calculated the data conversion - will confirm it's 47,674.13699 bit")
            assert output == "47,674.13699", f"Expected 47,674.13699 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformGBTobitConversion2")
            raise

############################################################################################
# MB
############################################################################################
@pytest.mark.timeout(175)
def test_perform_mb_to_gb_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform MBToGB Conversion1"):
        try:
            print("Will calculate the data in GB")
            output = unit_converter_page.convert_data("MB","1000","GB")
            print("Calculated the data conversion - will confirm it's 0.97656 GB")
            assert output == "0.97656", f"Expected 0.97656 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformMBToGBConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_mb_to_gb_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform MBToGB Conversion2"):
        try:
            print("Will calculate the data in GB")
            output = unit_converter_page.convert_data("MB","35000","GB")
            print("Calculated the data conversion - will confirm it's 34.17969 GB")
            assert output == "34.17969", f"Expected 34.17969 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformMBToGBConversion2")
            raise

def test_perform_mb_to_b_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform MBToB Conversion1"):
        try:
            print("Will calculate the data in B")
            output = unit_converter_page.convert_data("MB","0.75","B")
            print("Calculated the data conversion - will confirm it's 786,432 B")
            assert output == "786,432", f"Expected 786,432 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformMBToBConversion1")
            raise

def test_perform_mb_to_b_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform MBToB Conversion2"):
        try:
            print("Will calculate the data in B")
            output = unit_converter_page.convert_data("MB","39","B")
            print("Calculated the data conversion - will confirm it's 40,894,464 B")
            assert output == "40,894,464", f"Expected 40,894,464 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformMBToBConversion2")
            raise

def test_perform_mb_to_kb_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform MBToKB Conversion1"):
        try:
            print("Will calculate the data in KB")
            output = unit_converter_page.convert_data("MB","0.06","KB")
            print("Calculated the data conversion - will confirm it's 61.44 KB")
            assert output == "61.44", f"Expected 61.44 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformMBToKBConversion1")
            raise

def test_perform_mb_to_kb_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform MBToKB Conversion2"):
        try:
            print("Will calculate the data in KB")
            output = unit_converter_page.convert_data("MB","8.77","KB")
            print("Calculated the data conversion - will confirm it's 8,980.48 KB")
            assert output == "8,980.48", f"Expected 8,980.48 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformMBToKBConversion2")
            raise

def test_perform_mb_to_tb_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform MBToTB Conversion1"):
        try:
            print("Will calculate the data in TB")
            output = unit_converter_page.convert_data("MB","100000","TB")
            print("Calculated the data conversion - will confirm it's 0.095367 TB")
            assert output == "0.095367", f"Expected 0.095367 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformMBToTBConversion1")
            raise

def test_perform_mb_to_tb_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform MBToTB Conversion2"):
        try:
            print("Will calculate the data in TB")
            output = unit_converter_page.convert_data("MB","2500","TB")
            print("Calculated the data conversion - will confirm it's 0.0023842 TB")
            assert output == "0.0023842", f"Expected 0.0023842 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformMBToTBConversion2")
            raise

def test_perform_mb_to_bit_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform MBToBit Conversion1"):
        try:
            print("Will calculate the data in bits")
            output = unit_converter_page.convert_data("MB","6666","b")
            print("Calculated the data conversion - will confirm it's 55,918,460,928 bits")
            assert output == "55,918,460,928", f"Expected 55,918,460,928 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformMBToBitConversion1")
            raise

def test_perform_mb_to_bit_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform MBToBit Conversion2"):
        try:
            print("Will calculate the data in bits")
            output = unit_converter_page.convert_data("MB","0.0009","b")
            print("Calculated the data conversion - will confirm it's 7,549.7472 bits")
            assert output == "7,549.7472", f"Expected 7,549.7472 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformMBToBitConversion2")
            raise