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
        except Exception:
            capture_error_snapshot(driver, "AccessUnitConverter")
            raise

@pytest.mark.timeout(175)
def test_perform_cm_to_in_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform CmToIn Conversion1"):
        try:
            print("Will calculate the length in inches")
            output = unit_converter_page.convert_cm_to_inches("400")
            print("Calculated the length - will confirm it's 157.48 inches")
            assert output == "157.48", f"Expected 157.48 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformCmToInConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_cm_to_in_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform CmToIn Conversion2"):
        try:
            print("Will calculate the length in inches")
            output = unit_converter_page.convert_cm_to_inches("312475")
            print("Calculated the length - will confirm it's 123,021.4075 inches")
            assert output == "123,021.4075", f"Expected 123,021.4075 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformCmToInConversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_cm_to_m_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform CmToM Conversion1"):
        try:
            print("Will calculate the length in meters")
            output = unit_converter_page.convert_cm_to_meter("100")
            print("Calculated the length - will confirm it's 1 meter(s)")
            assert output == "1", f"Expected 1 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformCmToMConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_cm_to_m_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform CmToM Conversion2"):
        try:
            print("Will calculate the length in meters")
            output = unit_converter_page.convert_cm_to_meter("85000")
            print("Calculated the length - will confirm it's 850 meter(s)")
            assert output == "850", f"Expected 850 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformCmToMConversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_cm_to_km_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform CmToKM Conversion1"):
        try:
            print("Will calculate the length in kilometers")
            output = unit_converter_page.convert_cm_to_km("125750")
            print("Calculated the length - will confirm it's 1.2575 kilometer(s)")
            assert output == "1.2575", f"Expected 1.2575 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformCmToKMConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_in_to_cm_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform InchToCm Conversion1"):
        try:
            print("Will calculate the length in cm")
            output = unit_converter_page.convert_inch_to_cm("1")
            print("Calculated the length - will confirm it's 2.54001 cm(s)")
            assert output == "2.54001", f"Expected 2.54001 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformInchToCmConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_in_to_m_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform InchToM Conversion1"):
        try:
            print("Will calculate the length in m")
            output = unit_converter_page.convert_inch_to_meter("985.12")
            print("Calculated the length - will confirm it's 25.022098 m(s)")
            assert output == "25.022098", f"Expected 25.022098 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformInchToMConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_in_to_km_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform InchToKm Conversion1"):
        try:
            print("Will calculate the length in km")
            output = unit_converter_page.convert_inch_to_kilometer("68942")
            print("Calculated the length - will confirm it's 1.75113 km(s)")
            assert output == "1.75113", f"Expected 1.75113 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformInchToKmConversion1")
            raise

