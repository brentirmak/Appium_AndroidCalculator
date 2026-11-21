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

############################################################################################
# B
############################################################################################
@pytest.mark.timeout(175)
def test_perform_b_to_gb_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform BToGB Conversion1"):
        try:
            print("Will calculate the data in GB")
            output = unit_converter_page.convert_data("B","963258742","GB")
            print("Calculated the data conversion - will confirm it's 0.8971 GB")
            assert output == "0.8971", f"Expected 0.8971 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformBToGBConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_b_to_gb_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform BToGB Conversion2"):
        try:
            print("Will calculate the data in GB")
            output = unit_converter_page.convert_data("B","5555555555","GB")
            print("Calculated the data conversion - will confirm it's 5.17401 GB")
            assert output == "5.17401", f"Expected 5.17401 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformBToGBConversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_b_to_mb_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform BToMB Conversion1"):
        try:
            print("Will calculate the data in MB")
            output = unit_converter_page.convert_data("B","159357","MB")
            print("Calculated the data conversion - will confirm it's 0.15197 MB")
            assert output == "0.15197", f"Expected 0.15197 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformBToMBConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_b_to_mb_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform BToMB Conversion2"):
        try:
            print("Will calculate the data in MB")
            output = unit_converter_page.convert_data("B","8500000","MB")
            print("Calculated the data conversion - will confirm it's 8.10623 MB")
            assert output == "8.10623", f"Expected 8.10623 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformBToMBConversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_b_to_kb_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform BToKB Conversion1"):
        try:
            print("Will calculate the data in KB")
            output = unit_converter_page.convert_data("B","250","KB")
            print("Calculated the data conversion - will confirm it's 0.24414 KB")
            assert output == "0.24414", f"Expected 0.24414 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformBToKBConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_b_to_kb_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform BToKB Conversion2"):
        try:
            print("Will calculate the data in KB")
            output = unit_converter_page.convert_data("B","450000","KB")
            print("Calculated the data conversion - will confirm it's 439.45313 KB")
            assert output == "439.45313", f"Expected 439.45313 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformBToKBConversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_b_to_tb_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform BToTB Conversion1"):
        try:
            print("Will calculate the data in TB")
            output = unit_converter_page.convert_data("B","125000000000","TB")
            print("Calculated the data conversion - will confirm it's 0.11369 TB")
            assert output == "0.11369", f"Expected 0.11369 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformBToTBConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_b_to_tb_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform BToTB Conversion2"):
        try:
            print("Will calculate the data in TB")
            output = unit_converter_page.convert_data("B","85000000","TB")
            print("Calculated the data conversion - will confirm it's 0.000077307 TB")
            assert output == "0.000077307", f"Expected 0.000077307 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformBToTBConversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_b_to_bit_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform BToBit Conversion1"):
        try:
            print("Will calculate the data in Bit")
            output = unit_converter_page.convert_data("B","23","b")
            print("Calculated the data conversion - will confirm it's 184 bits")
            assert output == "184", f"Expected 184 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformBToBitConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_b_to_bit_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform BToBit Conversion2"):
        try:
            print("Will calculate the data in Bit")
            output = unit_converter_page.convert_data("B","250.999","b")
            print("Calculated the data conversion - will confirm it's 2,007.992 bits")
            assert output == "2,007.992", f"Expected 2,007.992 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformBToBitConversion2")
            raise

############################################################################################
# KB
############################################################################################
@pytest.mark.timeout(175)
def test_perform_kb_to_gb_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform KBToGB Conversion1"):
        try:
            print("Will calculate the data in GB")
            output = unit_converter_page.convert_data("KB","850000","GB")
            print("Calculated the data conversion - will confirm it's 0.81062 GB")
            assert output == "0.81062", f"Expected 0.81062 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformKBToGBConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_kb_to_gb_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform KBToGB Conversion2"):
        try:
            print("Will calculate the data in GB")
            output = unit_converter_page.convert_data("KB","33333333","GB")
            print("Calculated the data conversion - will confirm it's 31.78914 GB")
            assert output == "31.78914", f"Expected 31.78914 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformKBToGBConversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_kb_to_mb_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform KBToMB Conversion1"):
        try:
            print("Will calculate the data in MB")
            output = unit_converter_page.convert_data("KB","325000","MB")
            print("Calculated the data conversion - will confirm it's 317.38281 MB")
            assert output == "317.38281", f"Expected 317.38281 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformKBToMBConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_kb_to_mb_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform KBToMB Conversion2"):
        try:
            print("Will calculate the data in MB")
            output = unit_converter_page.convert_data("KB","0.999","MB")
            print("Calculated the data conversion - will confirm it's 0.00097559 MB")
            assert output == "0.00097559", f"Expected 0.00097559 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformKBToMBConversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_kb_to_b_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform KBToB Conversion1"):
        try:
            print("Will calculate the data in B")
            output = unit_converter_page.convert_data("KB","611","B")
            print("Calculated the data conversion - will confirm it's 625,664 B")
            assert output == "625,664", f"Expected 625,664 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformKBToBConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_kb_to_b_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform KBToB Conversion2"):
        try:
            print("Will calculate the data in B")
            output = unit_converter_page.convert_data("KB","0.71","B")
            print("Calculated the data conversion - will confirm it's 727.04 B")
            assert output == "727.04", f"Expected 727.04 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformKBToBConversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_kb_to_tb_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform KBToTB Conversion1"):
        try:
            print("Will calculate the data in TB")
            output = unit_converter_page.convert_data("KB","2224843","TB")
            print("Calculated the data conversion - will confirm it's 0.002072 TB")
            assert output == "0.002072", f"Expected 0.002072 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformKBToTBConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_kb_to_tb_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform KBToTB Conversion2"):
        try:
            print("Will calculate the data in TB")
            output = unit_converter_page.convert_data("KB","5000000000","TB")
            print("Calculated the data conversion - will confirm it's 4.65661 TB")
            assert output == "4.65661", f"Expected 4.65661 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformKBToTBConversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_kb_to_bit_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform KBTob Conversion1"):
        try:
            print("Will calculate the data in bits")
            output = unit_converter_page.convert_data("KB","842","b")
            print("Calculated the data conversion - will confirm it's 6,897,664 bits")
            assert output == "6,897,664", f"Expected 6,897,664 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformKBTobConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_kb_to_bit_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform KBTob Conversion2"):
        try:
            print("Will calculate the data in bits")
            output = unit_converter_page.convert_data("KB","0.005","b")
            print("Calculated the data conversion - will confirm it's 40.96 bits")
            assert output == "40.96", f"Expected 40.96 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformKBTobConversion2")
            raise

############################################################################################
# TB
############################################################################################
@pytest.mark.timeout(175)
def test_perform_tb_to_gb_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform TBToGB Conversion1"):
        try:
            print("Will calculate the data in GB")
            output = unit_converter_page.convert_data("TB","100","GB")
            print("Calculated the data conversion - will confirm it's 102,400 GB")
            assert output == "102,400", f"Expected 102,400 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformTBToGBConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_tb_to_gb_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform TBToGB Conversion2"):
        try:
            print("Will calculate the data in GB")
            output = unit_converter_page.convert_data("TB","0.25","GB")
            print("Calculated the data conversion - will confirm it's 256 GB")
            assert output == "256", f"Expected 256 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformTBToGBConversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_tb_to_mb_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform TBToMB Conversion1"):
        try:
            print("Will calculate the data in MB")
            output = unit_converter_page.convert_data("TB","525","MB")
            print("Calculated the data conversion - will confirm it's 550,502,400 MB")
            assert output == "550,502,400", f"Expected 550,502,400 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformTBToMBConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_tb_to_mb_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform TBToMB Conversion2"):
        try:
            print("Will calculate the data in MB")
            output = unit_converter_page.convert_data("TB","0.88","MB")
            print("Calculated the data conversion - will confirm it's 922,746.88 MB")
            assert output == "922,746.88", f"Expected 922,746.88 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformTBToMBConversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_tb_to_b_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform TBToB Conversion1"):
        try:
            print("Will calculate the data in B")
            output = unit_converter_page.convert_data("TB","0.003","B")
            print("Calculated the data conversion - will confirm it's 3,298,534,883.328 B")
            assert output == "3,298,534,883.328", f"Expected 3,298,534,883.328 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformTBToBConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_tb_to_b_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform TBToB Conversion2"):
        try:
            print("Will calculate the data in B")
            output = unit_converter_page.convert_data("TB","0.000003","B")
            print("Calculated the data conversion - will confirm it's 3,298,534.88333 B")
            assert output == "3,298,534.88333", f"Expected 3,298,534.88333 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformTBToBConversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_tb_to_kb_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform TBToKB Conversion1"):
        try:
            print("Will calculate the data in KB")
            output = unit_converter_page.convert_data("TB","0.000002","KB")
            print("Calculated the data conversion - will confirm it's 2,147.48365 KB")
            assert output == "2,147.48365", f"Expected 2,147.48365 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformTBToKBConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_tb_to_kb_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform TBToKB Conversion2"):
        try:
            print("Will calculate the data in KB")
            output = unit_converter_page.convert_data("TB","0.0005","KB")
            print("Calculated the data conversion - will confirm it's 536,870.912 KB")
            assert output == "536,870.912", f"Expected 536,870.912 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformTBToKBConversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_tb_to_bit_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform TBToBit Conversion1"):
        try:
            print("Will calculate the data in bit")
            output = unit_converter_page.convert_data("TB","0.000006","b")
            print("Calculated the data conversion - will confirm it's 52,776,558.13325 bit")
            assert output == "52,776,558.13325", f"Expected 52,776,558.13325 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformTBToBitConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_tb_to_bit_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform TBToBit Conversion2"):
        try:
            print("Will calculate the data in bit")
            output = unit_converter_page.convert_data("TB","0.0009","b")
            print("Calculated the data conversion - will confirm it's 7,916,483,719.9872 bit")
            assert output == "7,916,483,719.9872", f"Expected 7,916,483,719.9872 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformTBToBitConversion2")
            raise