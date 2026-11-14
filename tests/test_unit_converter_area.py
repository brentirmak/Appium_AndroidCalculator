'''
11/13/26 - 61 transactions
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
            unit_converter_page.select_conversion_type_value("Area")

            conversion_type = unit_converter_page.get_conversion_type()
            assert conversion_type == "Area", f"Expected 'Area' but got '{conversion_type}'"

        except Exception:
            capture_error_snapshot(driver, "AccessUnitConverter")
            raise


############################################################################################
# m²
############################################################################################

@pytest.mark.timeout(175)
def test_perform_square_m_to_square_inch_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform m²_to_in² Conversion1"):
        try:
            print("Will calculate the area in in²")
            output = unit_converter_page.convert_area("m²","200","in²")
            print("Calculated the area - will confirm it's 310,000 in²")
            assert output == "310,000", f"Expected 310,000 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "Perform_m²_to_in²_Conversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_square_m_to_square_inch_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform m²_to_in² Conversion2"):
        try:
            print("Will calculate the area in in²")
            output = unit_converter_page.convert_area("m²","0.25","in²")
            print("Calculated the area - will confirm it's 387.5 in²")
            assert output == "387.5", f"Expected 387.5 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "Perform_m²_to_in²_Conversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_square_m_to_square_ft_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform m²_to_ft² Conversion1"):
        try:
            print("Will calculate the area in ft²")
            output = unit_converter_page.convert_area("m²","867","ft²")
            print("Calculated the area - will confirm it's 9,332.31033 ft²")
            assert output == "9,332.31033", f"Expected 9,332.31033 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "Perform_m²_to_ft²_Conversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_square_m_to_square_ft_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform m²_to_ft² Conversion2"):
        try:
            print("Will calculate the area in ft²")
            output = unit_converter_page.convert_area("m²","0.35","ft²")
            print("Calculated the area - will confirm it's 3.76737 ft²")
            assert output == "3.76737", f"Expected 3.76737 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "Perform_m²_to_ft²_Conversion2")
            raise