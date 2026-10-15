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

############################################################################################
# CM
############################################################################################
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
def test_perform_cm_to_mile_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform CmToMile Conversion1"):
        try:
            print("Will calculate the length in mile(s)")
            output = unit_converter_page.convert_cm_to_mile("247508")
            print("Calculated the length - will confirm it's 1.53794 mile(s)")
            assert output == "1.53794", f"Expected 1.53794 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformCmToMileConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_cm_to_yard_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform CmToYard Conversion1"):
        try:
            print("Will calculate the length in yard(s)")
            output = unit_converter_page.convert_cm_to_yards("395")
            print("Calculated the length - will confirm it's 4.31977 yard(s)")
            assert output == "4.31977", f"Expected 4.31977 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformCmToYardConversion1")
            raise

############################################################################################
# INCHES
############################################################################################
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

@pytest.mark.timeout(175)
def test_perform_in_to_mile_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform InchToMile Conversion1"):
        try:
            print("Will calculate the length in mile(s)")
            output = unit_converter_page.convert_inch_to_mile("214683")
            print("Calculated the length - will confirm it's 3.38831 km(s)")
            assert output == "3.38831", f"Expected 3.38831 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformInchToMileConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_in_to_yard_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform InchToYard Conversion1"):
        try:
            print("Will calculate the length in yard(s)")
            output = unit_converter_page.convert_inch_to_yard("654")
            print("Calculated the length - will confirm it's 18.1667 yd(s)")
            assert output == "18.1667", f"Expected 18.1667 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformInchToYardConversion1")
            raise

############################################################################################
# METERS
############################################################################################

@pytest.mark.timeout(175)
def test_perform_meter_to_cm_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform MeterToCm Conversion1"):
        try:
            print("Will calculate the length in cm")
            output = unit_converter_page.convert_meter_to_cm("2")
            print("Calculated the length - will confirm it's 200 cm(s)")
            assert output == "200", f"Expected 200 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformMeterToCmConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_meter_to_inch_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform MeterToInch Conversion1"):
        try:
            print("Will calculate the length in cm")
            output = unit_converter_page.convert_meter_to_inch("20")
            print("Calculated the length - will confirm it's 787.4 in")
            assert output == "787.4", f"Expected 787.4 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformMeterToInchConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_meter_to_km_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform MeterToKm Conversion1"):
        try:
            print("Will calculate the length in km")
            output = unit_converter_page.convert_meter_to_km("8900")
            print("Calculated the length - will confirm it's 8.9 km")
            assert output == "8.9", f"Expected 8.9 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformMeterToKmConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_meter_to_mile_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform MeterToMile Conversion1"):
        try:
            print("Will calculate the length in mile")
            output = unit_converter_page.convert_meter_to_mile("317064")
            print("Calculated the length - will confirm it's 197.014375 mile(s)")
            assert output == "197.014375", f"Expected 197.014375 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformMeterToMileConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_meter_to_yard_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform MeterToYard Conversion1"):
        try:
            print("Will calculate the length in yard(s)")
            output = unit_converter_page.convert_meter_to_yard("95")
            print("Calculated the length - will confirm it's 103.89326 mile(s)")
            assert output == "103.89326", f"Expected 103.89326 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformMeterToYardConversion1")
            raise

############################################################################################
# KILOMETERS
############################################################################################

@pytest.mark.timeout(175)
def test_perform_km_to_cm_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform KmToCm Conversion1"):
        try:
            print("Will calculate the length in cm")
            output = unit_converter_page.convert_km_to_cm("1.5")
            print("Calculated the length - will confirm it's 150,000 cm(s)")
            assert output == "150,000", f"Expected 150,000 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformKmToCmConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_km_to_inches_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform KmToInches Conversion1"):
        try:
            print("Will calculate the length in cm")
            output = unit_converter_page.convert_km_to_inches("2.9")
            print("Calculated the length - will confirm it's 114,173 inch(es)")
            assert output == "114,173", f"Expected 114,173 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformKmToInchesConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_km_to_meters_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform KmToMeters Conversion1"):
        try:
            print("Will calculate the length in meter(s)")
            output = unit_converter_page.convert_km_to_meters("17.4")
            print("Calculated the length - will confirm it's 17,400 meter(s)")
            assert output == "17,400", f"Expected 17,400 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformKmToMetersConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_km_to_miles_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform KmToMiles Conversion1"):
        try:
            print("Will calculate the length in mile(s)")
            output = unit_converter_page.convert_km_to_miles("69")
            print("Calculated the length - will confirm it's 42.8746 meter(s)")
            assert output == "42.8746", f"Expected 42.8746 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformKmToMilesConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_km_to_yd_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform KmToYd Conversion1"):
        try:
            print("Will calculate the length in mile(s)")
            output = unit_converter_page.convert_km_to_yd("35")
            print("Calculated the length - will confirm it's 38,276.46544 yard(s)")
            assert output == "38,276.46544", f"Expected 38,276.46544 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformKmToYdConversion1")
            raise

############################################################################################
# MILES
############################################################################################

@pytest.mark.timeout(175)
def test_perform_miles_to_cm_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform MilesToCm Conversion1"):
        try:
            print("Will calculate the length in cm")
            output = unit_converter_page.convert_miles_to_cm("0.65")
            print("Calculated the length - will confirm it's 104,607.39236 cm(s)")
            assert output == "104,607.39236", f"Expected 104,607.39236 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformMilesToCmConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_miles_to_inches_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform MilesToInches Conversion1"):
        try:
            print("Will calculate the length in inches")
            output = unit_converter_page.convert_miles_to_inches("0.03")
            print("Calculated the length - will confirm it's 1,900.79679 inch(es)")
            assert output == "1,900.79679", f"Expected 1,900.79679 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformMilesToInchesConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_miles_to_meters_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform MilesToMeters Conversion1"):
        try:
            print("Will calculate the length in meters")
            output = unit_converter_page.convert_miles_to_meters("3.55")
            print("Calculated the length - will confirm it's 5,713.17297 meter(s)")
            assert output == "5,713.17297", f"Expected 5,713.17297 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformMilesToMetersConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_miles_to_km_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform MilesToKm Conversion1"):
        try:
            print("Will calculate the length in kilometers")
            output = unit_converter_page.convert_miles_to_kilometers("1")
            print("Calculated the length - will confirm it's 1.60934 meter(s)")
            assert output == "1.60934", f"Expected 1.60934 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformMilesToKmConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_miles_to_yd_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform MilesToYd Conversion1"):
        try:
            print("Will calculate the length in yard(s)")
            output = unit_converter_page.convert_miles_to_yards("60")
            print("Calculated the length - will confirm it's 105,600.03267 yard(s)")
            assert output == "105,600.03267", f"Expected 105,600.03267 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformMilesToYdConversion1")
            raise

############################################################################################
# YARDS
############################################################################################

@pytest.mark.timeout(175)
def test_perform_yards_to_cm_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform YardsToCm Conversion1"):
        try:
            print("Will calculate the length in cm")
            output = unit_converter_page.convert_yards_to_cm("10")
            print("Calculated the length - will confirm it's 914.4 cm(s)")
            assert output == "914.4", f"Expected 914.4 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformYardsToCmConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_yards_to_inches_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform YardsToInches Conversion1"):
        try:
            print("Will calculate the length in inches")
            output = unit_converter_page.convert_yards_to_inches("15.6")
            print("Calculated the length - will confirm it's 561.59888 cm(s)")
            assert output == "561.59888", f"Expected 561.59888 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformYardsToInchesConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_yards_to_meters_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform YardsToMeters Conversion1"):
        try:
            print("Will calculate the length in meters")
            output = unit_converter_page.convert_yards_to_meters("346.2")
            print("Calculated the length - will confirm it's 316.56528 cm(s)")
            assert output == "316.56528", f"Expected 316.56528 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformYardsToMetersConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_yards_to_kilometers_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform YardsToKm Conversion1"):
        try:
            print("Will calculate the length in meters")
            output = unit_converter_page.convert_yards_to_kilometers("835")
            print("Calculated the length - will confirm it's 0.76352 cm(s)")
            assert output == "0.76352", f"Expected 0.76352 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformYardsToKmConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_yards_to_miles_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform YardsToMiles Conversion1"):
        try:
            print("Will calculate the length in miles")
            output = unit_converter_page.convert_yards_to_miles("967")
            print("Calculated the length - will confirm it's 0.54943 mile(s)")
            assert output == "0.54943", f"Expected 0.54943 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformYardsToMiles")
            raise

@pytest.mark.timeout(175)
def test_perform_yards_to_ft_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform YardsToFt Conversion1"):
        try:
            print("Will calculate the length in ft")
            output = unit_converter_page.convert_yards_to_ft("2380")
            print("Calculated the length - will confirm it's 7,140 mile(s)")
            assert output == "7,140", f"Expected 7,140 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformYardsToFt")
            raise