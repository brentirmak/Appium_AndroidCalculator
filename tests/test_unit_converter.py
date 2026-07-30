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
        if not home.verify_home_loaded():
            print("Not at Home screen")
        try:
            print("Will click on the side menu item for Unit Converter")
            side_menu.go_unit_converter()
            assert unit_converter_page.verify_loaded(), "Unit Converter header not found"
        except Exception:
            capture_error_snapshot(driver, "AccessUnitConverter")
            raise


@pytest.mark.timeout(175)
def test_perform_unit_conversion(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform Unit Conversion"):
        try:
            print("Will calculate the length in inches")
            output = unit_converter_page.convert_cm_inches()
            print("Calculated the length - will confirm it's 4.3307 inches")
            assert output == "4.3307", f"Expected 4.3307 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformUnitConversion")
            raise
