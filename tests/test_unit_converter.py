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
            unit_converter_page.select_conversion_type_value("Length")

            conversion_type = unit_converter_page.get_conversion_type()
            assert conversion_type == "Length", f"Expected 'Length' but got '{conversion_type}'"
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
            output = unit_converter_page.convert_length("cm","400","inches")
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
            output = unit_converter_page.convert_length("cm", "312475", "inches")
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
            output = unit_converter_page.convert_length("cm", "100", "meter")
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
            output = unit_converter_page.convert_length("cm", "85000", "meter")
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
            output = unit_converter_page.convert_length("cm", "125750", "kilometer")
            print("Calculated the length - will confirm it's 1.2575 kilometer(s)")
            assert output == "1.2575", f"Expected 1.2575 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformCmToKMConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_cm_to_km_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform CmToKM Conversion2"):
        try:
            print("Will calculate the length in kilometers")
            output = unit_converter_page.convert_length("cm", "2695720", "kilometer")
            print("Calculated the length - will confirm it's 26.9572 kilometer(s)")
            assert output == "26.9572", f"Expected 26.9572 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformCmToKMConversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_cm_to_mile_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform CmToMile Conversion1"):
        try:
            print("Will calculate the length in mile(s)")
            output = unit_converter_page.convert_length("cm", "247508", "mile")
            print("Calculated the length - will confirm it's 1.53794 mile(s)")
            assert output == "1.53794", f"Expected 1.53794 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformCmToMileConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_cm_to_mile_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform CmToMile Conversion2"):
        try:
            print("Will calculate the length in mile(s)")
            output = unit_converter_page.convert_length("cm", "3850000", "mile")
            print("Calculated the length - will confirm it's 23.92278 mile(s)")
            assert output == "23.92278", f"Expected 23.92278 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformCmToMileConversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_cm_to_yard_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform CmToYard Conversion1"):
        try:
            print("Will calculate the length in yard(s)")
            output = unit_converter_page.convert_length("cm", "395", "yd")
            print("Calculated the length - will confirm it's 4.31977 yard(s)")
            assert output == "4.31977", f"Expected 4.31977 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformCmToYardConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_cm_to_yard_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform CmToYard Conversion2"):
        try:
            print("Will calculate the length in yard(s)")
            output = unit_converter_page.convert_length("cm", "575", "yd")
            print("Calculated the length - will confirm it's 6.28828 yard(s)")
            assert output == "6.28828", f"Expected 6.28828 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformCmToYardConversion2")
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
            output = unit_converter_page.convert_length("inches", "1", "cm")
            print("Calculated the length - will confirm it's 2.54001 cm(s)")
            assert output == "2.54001", f"Expected 2.54001 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformInchToCmConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_in_to_cm_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform InchToCm Conversion2"):
        try:
            print("Will calculate the length in cm")
            output = unit_converter_page.convert_length("inches", "2.905", "cm")
            print("Calculated the length - will confirm it's 7.37871 cm(s)")
            assert output == "7.37871", f"Expected 7.37871 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformInchToCmConversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_in_to_m_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform InchToM Conversion1"):
        try:
            print("Will calculate the length in m")
            output = unit_converter_page.convert_length("inches", "985.12", "meter")
            print("Calculated the length - will confirm it's 25.022098 m(s)")
            assert output == "25.022098", f"Expected 25.022098 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformInchToMConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_in_to_m_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform InchToM Conversion2"):
        try:
            print("Will calculate the length in m")
            output = unit_converter_page.convert_length("inches", "695.25", "meter")
            print("Calculated the length - will confirm it's 17.65939 m(s)")
            assert output == "17.65939", f"Expected 17.65939 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformInchToMConversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_in_to_km_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform InchToKm Conversion1"):
        try:
            print("Will calculate the length in km")
            output = unit_converter_page.convert_length("inches", "68942", "kilometer")
            print("Calculated the length - will confirm it's 1.75113 km(s)")
            assert output == "1.75113", f"Expected 1.75113 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformInchToKmConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_in_to_km_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform InchToKm Conversion2"):
        try:
            print("Will calculate the length in km")
            output = unit_converter_page.convert_length("inches", "17500000", "kilometer")
            print("Calculated the length - will confirm it's 444.50089 km(s)")
            assert output == "444.50089", f"Expected 444.50089 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformInchToKmConversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_in_to_mile_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform InchToMile Conversion1"):
        try:
            print("Will calculate the length in mile(s)")
            output = unit_converter_page.convert_length("inches", "214683", "mile")
            print("Calculated the length - will confirm it's 3.38831 km(s)")
            assert output == "3.38831", f"Expected 3.38831 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformInchToMileConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_in_to_mile_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform InchToMile Conversion2"):
        try:
            print("Will calculate the length in mile(s)")
            output = unit_converter_page.convert_length("inches", "360", "mile")
            print("Calculated the length - will confirm it's 0.0056818 km(s)")
            assert output == "0.0056818", f"Expected 0.0056818 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformInchToMileConversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_in_to_yard_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform InchToYard Conversion1"):
        try:
            print("Will calculate the length in yard(s)")
            output = unit_converter_page.convert_length("inches", "654", "yd")
            print("Calculated the length - will confirm it's 18.1667 yd(s)")
            assert output == "18.1667", f"Expected 18.1667 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformInchToYardConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_in_to_yard_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform InchToYard Conversion2"):
        try:
            print("Will calculate the length in yard(s)")
            output = unit_converter_page.convert_length("inches", "1000", "yd")
            print("Calculated the length - will confirm it's 27.77783 yd(s)")
            assert output == "27.77783", f"Expected 27.77783 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformInchToYardConversion2")
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
            output = unit_converter_page.convert_length("meter", "2", "cm")
            print("Calculated the length - will confirm it's 200 cm(s)")
            assert output == "200", f"Expected 200 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformMeterToCmConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_meter_to_cm_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform MeterToCm Conversion2"):
        try:
            print("Will calculate the length in cm")
            output = unit_converter_page.convert_length("meter", "333.99", "cm")
            print("Calculated the length - will confirm it's 33,399 cm(s)")
            assert output == "33,399", f"Expected 33,399 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformMeterToCmConversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_meter_to_inch_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform MeterToInch Conversion1"):
        try:
            print("Will calculate the length in cm")
            output = unit_converter_page.convert_length("meter", "20", "inches")
            print("Calculated the length - will confirm it's 787.4 in")
            assert output == "787.4", f"Expected 787.4 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformMeterToInchConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_meter_to_inch_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform MeterToInch Conversion2"):
        try:
            print("Will calculate the length in cm")
            output = unit_converter_page.convert_length("meter", "0.85", "inches")
            print("Calculated the length - will confirm it's 33.4645 in")
            assert output == "33.4645", f"Expected 33.4645 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformMeterToInchConversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_meter_to_km_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform MeterToKm Conversion1"):
        try:
            print("Will calculate the length in km")
            output = unit_converter_page.convert_length("meter", "8900", "kilometer")
            print("Calculated the length - will confirm it's 8.9 km")
            assert output == "8.9", f"Expected 8.9 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformMeterToKmConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_meter_to_km_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform MeterToKm Conversion2"):
        try:
            print("Will calculate the length in km")
            output = unit_converter_page.convert_length("meter", "740550", "kilometer")
            print("Calculated the length - will confirm it's 740.55 km")
            assert output == "740.55", f"Expected 740.55 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformMeterToKmConversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_meter_to_mile_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform MeterToMile Conversion1"):
        try:
            print("Will calculate the length in mile")
            output = unit_converter_page.convert_length("meter", "317064", "mile")
            print("Calculated the length - will confirm it's 197.014375 mile(s)")
            assert output == "197.014375", f"Expected 197.014375 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformMeterToMileConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_meter_to_mile_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform MeterToMile Conversion2"):
        try:
            print("Will calculate the length in mile")
            output = unit_converter_page.convert_length("meter", "194250", "mile")
            print("Calculated the length - will confirm it's 120.70132 mile(s)")
            assert output == "120.70132", f"Expected 120.70132 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformMeterToMileConversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_meter_to_yard_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform MeterToYard Conversion1"):
        try:
            print("Will calculate the length in yard(s)")
            output = unit_converter_page.convert_length("meter", "95", "yd")
            print("Calculated the length - will confirm it's 103.89326 mile(s)")
            assert output == "103.89326", f"Expected 103.89326 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformMeterToYardConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_meter_to_yard_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform MeterToYard Conversion2"):
        try:
            print("Will calculate the length in yard(s)")
            output = unit_converter_page.convert_length("meter", "250", "yd")
            print("Calculated the length - will confirm it's 273.40332 mile(s)")
            assert output == "273.40332", f"Expected 273.40332 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformMeterToYardConversion2")
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
            output = unit_converter_page.convert_length("kilometer", "1.5", "cm")
            print("Calculated the length - will confirm it's 150,000 cm(s)")
            assert output == "150,000", f"Expected 150,000 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformKmToCmConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_km_to_cm_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform KmToCm Conversion2"):
        try:
            print("Will calculate the length in cm")
            output = unit_converter_page.convert_length("kilometer", "0.05", "cm")
            print("Calculated the length - will confirm it's 5,000 cm(s)")
            assert output == "5,000", f"Expected 5,000 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformKmToCmConversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_km_to_inches_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform KmToInches Conversion1"):
        try:
            print("Will calculate the length in cm")
            output = unit_converter_page.convert_length("kilometer", "2.9", "inches")
            print("Calculated the length - will confirm it's 114,173 inch(es)")
            assert output == "114,173", f"Expected 114,173 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformKmToInchesConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_km_to_inches_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform KmToInches Conversion2"):
        try:
            print("Will calculate the length in cm")
            output = unit_converter_page.convert_length("kilometer", "31", "inches")
            print("Calculated the length - will confirm it's 1,220,470 inch(es)")
            assert output == "1,220,470", f"Expected 1,220,470 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformKmToInchesConversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_km_to_meters_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform KmToMeters Conversion1"):
        try:
            print("Will calculate the length in meter(s)")
            output = unit_converter_page.convert_length("kilometer", "17.4", "meter")
            print("Calculated the length - will confirm it's 17,400 meter(s)")
            assert output == "17,400", f"Expected 17,400 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformKmToMetersConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_km_to_meters_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform KmToMeters Conversion2"):
        try:
            print("Will calculate the length in meter(s)")
            output = unit_converter_page.convert_length("kilometer", "0.65", "meter")
            print("Calculated the length - will confirm it's 650 meter(s)")
            assert output == "650", f"Expected 650 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformKmToMetersConversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_km_to_miles_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform KmToMiles Conversion1"):
        try:
            print("Will calculate the length in mile(s)")
            output = unit_converter_page.convert_length("kilometer", "69", "mile")
            print("Calculated the length - will confirm it's 42.8746 mile(s)")
            assert output == "42.8746", f"Expected 42.8746 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformKmToMilesConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_km_to_miles_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform KmToMiles Conversion2"):
        try:
            print("Will calculate the length in mile(s)")
            output = unit_converter_page.convert_length("kilometer", "300", "mile")
            print("Calculated the length - will confirm it's 186.4113 mile(s)")
            assert output == "186.4113", f"Expected 186.4113 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformKmToMilesConversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_km_to_yd_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform KmToYd Conversion1"):
        try:
            print("Will calculate the length in mile(s)")
            output = unit_converter_page.convert_length("kilometer", "35", "yd")
            print("Calculated the length - will confirm it's 38,276.46544 yard(s)")
            assert output == "38,276.46544", f"Expected 38,276.46544 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformKmToYdConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_km_to_yd_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform KmToYd Conversion2"):
        try:
            print("Will calculate the length in mile(s)")
            output = unit_converter_page.convert_length("kilometer", "0.25", "yd")
            print("Calculated the length - will confirm it's 273.40332 yard(s)")
            assert output == "273.40332", f"Expected 273.40332 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformKmToYdConversion2")
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
            output = unit_converter_page.convert_length("mile", "0.65", "cm")
            print("Calculated the length - will confirm it's 104,607.39236 cm(s)")
            assert output == "104,607.39236", f"Expected 104,607.39236 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformMilesToCmConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_miles_to_cm_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform MilesToCm Conversion2"):
        try:
            print("Will calculate the length in cm")
            output = unit_converter_page.convert_length("mile", "1.2", "cm")
            print("Calculated the length - will confirm it's 193,121.33975 cm(s)")
            assert output == "193,121.33975", f"Expected 193,121.33975 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformMilesToCmConversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_miles_to_inches_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform MilesToInches Conversion1"):
        try:
            print("Will calculate the length in inches")
            output = unit_converter_page.convert_length("mile", "0.03", "inches")
            print("Calculated the length - will confirm it's 1,900.79679 inch(es)")
            assert output == "1,900.79679", f"Expected 1,900.79679 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformMilesToInchesConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_miles_to_inches_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform MilesToInches Conversion2"):
        try:
            print("Will calculate the length in inches")
            output = unit_converter_page.convert_length("mile", "0.0095", "inches")
            print("Calculated the length - will confirm it's 601.91898 inch(es)")
            assert output == "601.91898", f"Expected 601.91898 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformMilesToInchesConversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_miles_to_meters_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform MilesToMeters Conversion1"):
        try:
            print("Will calculate the length in meters")
            output = unit_converter_page.convert_length("mile", "3.55", "meter")
            print("Calculated the length - will confirm it's 5,713.17297 meter(s)")
            assert output == "5,713.17297", f"Expected 5,713.17297 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformMilesToMetersConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_miles_to_meters_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform MilesToMeters Conversion2"):
        try:
            print("Will calculate the length in meters")
            output = unit_converter_page.convert_length("mile", "25", "meter")
            print("Calculated the length - will confirm it's 40,233.61245 meter(s)")
            assert output == "40,233.61245", f"Expected 40,233.61245 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformMilesToMetersConversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_miles_to_km_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform MilesToKm Conversion1"):
        try:
            print("Will calculate the length in kilometers")
            output = unit_converter_page.convert_length("mile", "1", "kilometer")
            print("Calculated the length - will confirm it's 1.60934 meter(s)")
            assert output == "1.60934", f"Expected 1.60934 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformMilesToKmConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_miles_to_km_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform MilesToKm Conversion2"):
        try:
            print("Will calculate the length in kilometers")
            output = unit_converter_page.convert_length("mile", "55", "kilometer")
            print("Calculated the length - will confirm it's 88.51395 meter(s)")
            assert output == "88.51395", f"Expected 88.51395 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformMilesToKmConversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_miles_to_yd_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform MilesToYd Conversion1"):
        try:
            print("Will calculate the length in yard(s)")
            output = unit_converter_page.convert_length("mile", "60", "yd")
            print("Calculated the length - will confirm it's 105,600.03267 yard(s)")
            assert output == "105,600.03267", f"Expected 105,600.03267 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformMilesToYdConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_miles_to_yd_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform MilesToYd Conversion2"):
        try:
            print("Will calculate the length in yard(s)")
            output = unit_converter_page.convert_length("mile", "0.020", "yd")
            print("Calculated the length - will confirm it's 35.20001 yard(s)")
            assert output == "35.20001", f"Expected 35.20001 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformMilesToYdConversion2")
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
            output = unit_converter_page.convert_length("yd", "10", "cm")
            print("Calculated the length - will confirm it's 914.4 cm(s)")
            assert output == "914.4", f"Expected 914.4 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformYardsToCmConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_yards_to_cm_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform YardsToCm Conversion2"):
        try:
            print("Will calculate the length in cm")
            output = unit_converter_page.convert_length("yd", "88.3", "cm")
            print("Calculated the length - will confirm it's 8,074.152 cm(s)")
            assert output == "8,074.152", f"Expected 8,074.152 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformYardsToCmConversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_yards_to_inches_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform YardsToInches Conversion1"):
        try:
            print("Will calculate the length in inches")
            output = unit_converter_page.convert_length("yd", "15.6", "inches")
            print("Calculated the length - will confirm it's 561.59888 inch(es)")
            assert output == "561.59888", f"Expected 561.59888 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformYardsToInchesConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_yards_to_inches_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform YardsToInches Conversion2"):
        try:
            print("Will calculate the length in inches")
            output = unit_converter_page.convert_length("yd", "5", "inches")
            print("Calculated the length - will confirm it's 179.99964 inch(es)")
            assert output == "179.99964", f"Expected 179.99964 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformYardsToInchesConversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_yards_to_meters_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform YardsToMeters Conversion1"):
        try:
            print("Will calculate the length in meters")
            output = unit_converter_page.convert_length("yd", "346.2", "meter")
            print("Calculated the length - will confirm it's 316.56528 m(s)")
            assert output == "316.56528", f"Expected 316.56528 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformYardsToMetersConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_yards_to_meters_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform YardsToMeters Conversion2"):
        try:
            print("Will calculate the length in meters")
            output = unit_converter_page.convert_length("yd", "40", "meter")
            print("Calculated the length - will confirm it's 36.576 m(s)")
            assert output == "36.576", f"Expected 36.576 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformYardsToMetersConversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_yards_to_kilometers_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform YardsToKm Conversion1"):
        try:
            print("Will calculate the length in meters")
            output = unit_converter_page.convert_length("yd", "835", "kilometer")
            print("Calculated the length - will confirm it's 0.76352 km(s)")
            assert output == "0.76352", f"Expected 0.76352 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformYardsToKmConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_yards_to_kilometers_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform YardsToKm Conversion2"):
        try:
            print("Will calculate the length in meters")
            output = unit_converter_page.convert_length("yd", "395", "kilometer")
            print("Calculated the length - will confirm it's 0.36119 km(s)")
            assert output == "0.36119", f"Expected 0.36119 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformYardsToKmConversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_yards_to_miles_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform YardsToMiles Conversion1"):
        try:
            print("Will calculate the length in miles")
            output = unit_converter_page.convert_length("yd", "967", "mile")
            print("Calculated the length - will confirm it's 0.54943 mile(s)")
            assert output == "0.54943", f"Expected 0.54943 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformYardsToMilesConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_yards_to_miles_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform YardsToMiles Conversion2"):
        try:
            print("Will calculate the length in miles")
            output = unit_converter_page.convert_length("yd", "25000", "mile")
            print("Calculated the length - will confirm it's 14.20454 mile(s)")
            assert output == "14.20454", f"Expected 14.20454 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformYardsToMilesConversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_yards_to_ft_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform YardsToFt Conversion1"):
        try:
            print("Will calculate the length in ft")
            output = unit_converter_page.convert_length("yd", "2380", "ft")
            print("Calculated the length - will confirm it's 7,140 ft")
            assert output == "7,140", f"Expected 7,140 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformYardsToFtConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_yards_to_ft_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform YardsToFt Conversion2"):
        try:
            print("Will calculate the length in ft")
            output = unit_converter_page.convert_length("yd", "897.543", "ft")
            print("Calculated the length - will confirm it's 2,692.629 ft")
            assert output == "2,692.629", f"Expected 2,692.629 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformYardsToFtConversion2")
            raise