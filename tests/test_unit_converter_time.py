'''
11/17/26 -  61 transactions
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
            unit_converter_page.select_conversion_type_value("Time")

            conversion_type = unit_converter_page.get_conversion_type()
            assert conversion_type == "Time", f"Expected 'Time' but got '{conversion_type}'"

        except Exception:
            capture_error_snapshot(driver, "AccessUnitConverter")
            raise


############################################################################################
# H
############################################################################################

@pytest.mark.timeout(175)
def test_perform_hr_to_sec_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform HrToSec Conversion1"):
        try:
            print("Will calculate the volume in sec")
            output = unit_converter_page.convert_time("h","2","s")
            print("Calculated the mass - will confirm it's 7,200 s")
            assert output == "7,200", f"Expected 7,200 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformHrToSecConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_hr_to_sec_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform HrToSec Conversion2"):
        try:
            print("Will calculate the volume in sec")
            output = unit_converter_page.convert_time("h","0.5","s")
            print("Calculated the mass - will confirm it's 1,800 s")
            assert output == "1,800", f"Expected 1,800 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformHrToSecConversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_hr_to_ms_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform HrToMs Conversion1"):
        try:
            print("Will calculate the volume in ms")
            output = unit_converter_page.convert_time("h","0.003","ms")
            print("Calculated the mass - will confirm it's 10,800 ms")
            assert output == "10,800", f"Expected 10,800 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformHrToMsConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_hr_to_ms_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform HrToMs Conversion2"):
        try:
            print("Will calculate the volume in ms")
            output = unit_converter_page.convert_time("h","0.0097","ms")
            print("Calculated the mass - will confirm it's 34,920 ms")
            assert output == "34,920", f"Expected 34,920 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformHrToMsConversion2")
            raise