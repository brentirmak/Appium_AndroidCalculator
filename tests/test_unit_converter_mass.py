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
            unit_converter_page.select_conversion_type_value("Mass")

            conversion_type = unit_converter_page.get_conversion_type()
            assert conversion_type == "Mass", f"Expected 'Mass' but got '{conversion_type}'"

        except Exception:
            capture_error_snapshot(driver, "AccessUnitConverter")
            raise


############################################################################################
# KG
############################################################################################

@pytest.mark.timeout(175)
def test_perform_kg_to_lb_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform KgToLb Conversion1"):
        try:
            print("Will calculate the mass in lb")
            output = unit_converter_page.convert_kg_to_lb("2")
            print("Calculated the mass - will confirm it's 4.40925 lbs")
            assert output == "4.40925", f"Expected 4.40925 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformKgToLbConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_kg_to_lb_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform KgToLb Conversion2"):
        try:
            print("Will calculate the mass in lb")
            output = unit_converter_page.convert_kg_to_lb("950")
            print("Calculated the mass - will confirm it's 2,094.39149 lbs")
            assert output == "2,094.39149", f"Expected 2,094.39149 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformKgToLbConversion2")
            raise

def test_perform_kg_to_mg_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform KgToMg Conversion1"):
        try:
            print("Will calculate the mass in mg")
            output = unit_converter_page.convert_kg_to_mg("1")
            print("Calculated the mass - will confirm it's 1,000,000 mg")
            assert output == "1,000,000", f"Expected 1,000,000 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformKgToMgConversion1")
            raise

def test_perform_kg_to_mg_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform KgToMg Conversion2"):
        try:
            print("Will calculate the mass in mg")
            output = unit_converter_page.convert_kg_to_mg("0.35")
            print("Calculated the mass - will confirm it's 350,000 mg")
            assert output == "350,000", f"Expected 350,000 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformKgToMgConversion2")
            raise

def test_perform_kg_to_g_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform KgTog Conversion1"):
        try:
            print("Will calculate the mass in g")
            output = unit_converter_page.convert_kg_to_g("28")
            print("Calculated the mass - will confirm it's 28,000 g")
            assert output == "28,000", f"Expected 28,000 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformKgTogConversion1")
            raise