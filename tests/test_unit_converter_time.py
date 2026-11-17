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
            print("Will calculate the time in sec")
            output = unit_converter_page.convert_time("h","2","s")
            print("Calculated the time - will confirm it's 7,200 s")
            assert output == "7,200", f"Expected 7,200 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformHrToSecConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_hr_to_sec_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform HrToSec Conversion2"):
        try:
            print("Will calculate the time in sec")
            output = unit_converter_page.convert_time("h","0.5","s")
            print("Calculated the time - will confirm it's 1,800 s")
            assert output == "1,800", f"Expected 1,800 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformHrToSecConversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_hr_to_ms_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform HrToMs Conversion1"):
        try:
            print("Will calculate the time in ms")
            output = unit_converter_page.convert_time("h","0.003","ms")
            print("Calculated the time - will confirm it's 10,800 ms")
            assert output == "10,800", f"Expected 10,800 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformHrToMsConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_hr_to_ms_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform HrToMs Conversion2"):
        try:
            print("Will calculate the time in ms")
            output = unit_converter_page.convert_time("h","0.0097","ms")
            print("Calculated the time - will confirm it's 34,920 ms")
            assert output == "34,920", f"Expected 34,920 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformHrToMsConversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_hr_to_micros_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform HrToµs Conversion1"):
        try:
            print("Will calculate the time in µs")
            output = unit_converter_page.convert_time("h","0.08","µs")
            print("Calculated the time - will confirm it's 288,000,000 ms")
            assert output == "288,000,000", f"Expected 288,000,000 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformHrToµsConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_hr_to_micros_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform HrToµs Conversion2"):
        try:
            print("Will calculate the time in µs")
            output = unit_converter_page.convert_time("h","0.000525","µs")
            print("Calculated the time - will confirm it's 1,890,000 ms")
            assert output == "1,890,000", f"Expected 1,890,000 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformHrToµsConversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_hr_to_ns_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform HrToNs Conversion1"):
        try:
            print("Will calculate the time in ns")
            output = unit_converter_page.convert_time("h","0.00000369","ns")
            print("Calculated the time - will confirm it's 13,284,000 ms")
            assert output == "13,284,000", f"Expected 13,284,000 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformHrToNsConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_hr_to_ns_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform HrToNs Conversion2"):
        try:
            print("Will calculate the time in ns")
            output = unit_converter_page.convert_time("h","0.1","ns")
            print("Calculated the time - will confirm it's 360,000,000,000 ms")
            assert output == "360,000,000,000", f"Expected 360,000,000,000 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformHrToNsConversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_hr_to_min_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform HrToMin Conversion1"):
        try:
            print("Will calculate the time in min")
            output = unit_converter_page.convert_time("h","0.1","min")
            print("Calculated the time - will confirm it's 6 min")
            assert output == "6", f"Expected 6 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformHrToMinConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_hr_to_min_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform HrToMin Conversion2"):
        try:
            print("Will calculate the time in min")
            output = unit_converter_page.convert_time("h","3.78","min")
            print("Calculated the time - will confirm it's 226.8 min")
            assert output == "226.8", f"Expected 226.8 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformHrToMinConversion2")
            raise

############################################################################################
# SEC
############################################################################################

@pytest.mark.timeout(175)
def test_perform_sec_to_hr_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform SecToHr Conversion1"):
        try:
            print("Will calculate the time in hr")
            output = unit_converter_page.convert_time("s","35000","h")
            print("Calculated the time - will confirm it's 9.72222 hr")
            assert output == "9.72222", f"Expected 9.72222 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformSecToHrConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_sec_to_hr_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform SecToHr Conversion2"):
        try:
            print("Will calculate the time in hr")
            output = unit_converter_page.convert_time("s","1000000","h")
            print("Calculated the time - will confirm it's 277.77778 hr")
            assert output == "277.77778", f"Expected 277.77778 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformSecToHrConversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_sec_to_ms_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform SecToMs Conversion1"):
        try:
            print("Will calculate the time in ms")
            output = unit_converter_page.convert_time("s","3.85","ms")
            print("Calculated the time - will confirm it's 3,850 ms")
            assert output == "3,850", f"Expected 3,850 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformSecToMsConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_sec_to_ms_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform SecToMs Conversion2"):
        try:
            print("Will calculate the time in ms")
            output = unit_converter_page.convert_time("s","502.97","ms")
            print("Calculated the time - will confirm it's 502,970 ms")
            assert output == "502,970", f"Expected 502,970 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformSecToMsConversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_sec_to_micros_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform SecToµs Conversion1"):
        try:
            print("Will calculate the time in ms")
            output = unit_converter_page.convert_time("s","9625","µs")
            print("Calculated the time - will confirm it's 9,625,000,000 µs")
            assert output == "9,625,000,000", f"Expected 9,625,000,000 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformSecToµsConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_sec_to_micros_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform SecToµs Conversion2"):
        try:
            print("Will calculate the time in ms")
            output = unit_converter_page.convert_time("s","0.0005","µs")
            print("Calculated the time - will confirm it's 500 µs")
            assert output == "500", f"Expected 500 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformSecToµsConversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_sec_to_ns_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform SecTons Conversion1"):
        try:
            print("Will calculate the time in ns")
            output = unit_converter_page.convert_time("s","0.080","ns")
            print("Calculated the time - will confirm it's 80,000,000 ns")
            assert output == "80,000,000", f"Expected 80,000,000 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformSecTonsConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_sec_to_ns_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform SecTons Conversion2"):
        try:
            print("Will calculate the time in ns")
            output = unit_converter_page.convert_time("s","0.00000125","ns")
            print("Calculated the time - will confirm it's 1,250 ns")
            assert output == "1,250", f"Expected 1,250 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformSecTonsConversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_sec_to_min_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform SecToMin Conversion1"):
        try:
            print("Will calculate the time in min")
            output = unit_converter_page.convert_time("s","3600","min")
            print("Calculated the time - will confirm it's 60 min")
            assert output == "60", f"Expected 60 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformSecToMinConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_sec_to_min_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform SecToMin Conversion2"):
        try:
            print("Will calculate the time in min")
            output = unit_converter_page.convert_time("s","250000","min")
            print("Calculated the time - will confirm it's 4,166.66667 min")
            assert output == "4,166.66667", f"Expected 4,166.66667 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformSecToMinConversion2")
            raise

############################################################################################
# MS
############################################################################################

@pytest.mark.timeout(175)
def test_perform_ms_to_hr_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform MsToHr Conversion1"):
        try:
            print("Will calculate the time in hr")
            output = unit_converter_page.convert_time("ms","250000","h")
            print("Calculated the time - will confirm it's 0.069444 hr")
            assert output == "0.069444", f"Expected 0.069444 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformMsToHrConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_ms_to_hr_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform MsToHr Conversion2"):
        try:
            print("Will calculate the time in hr")
            output = unit_converter_page.convert_time("ms","100000000","h")
            print("Calculated the time - will confirm it's 27.77778 hr")
            assert output == "27.77778", f"Expected 27.77778 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformMsToHrConversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_ms_to_sec_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform MsToSec Conversion1"):
        try:
            print("Will calculate the time in sec")
            output = unit_converter_page.convert_time("ms","450","s")
            print("Calculated the time - will confirm it's 0.45 sec")
            assert output == "0.45", f"Expected 0.45 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformMsToSecConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_ms_to_sec_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform MsToSec Conversion2"):
        try:
            print("Will calculate the time in sec")
            output = unit_converter_page.convert_time("ms","35298","s")
            print("Calculated the time - will confirm it's 35.298 sec")
            assert output == "35.298", f"Expected 35.298 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformMsToSecConversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_ms_to_micros_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform MsToµs Conversion1"):
        try:
            print("Will calculate the time in µs")
            output = unit_converter_page.convert_time("ms","20","µs")
            print("Calculated the time - will confirm it's 20,000 µs")
            assert output == "20,000", f"Expected 20,000 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformMsToµsConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_ms_to_micros_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform MsToµs Conversion2"):
        try:
            print("Will calculate the time in µs")
            output = unit_converter_page.convert_time("ms","0.323","µs")
            print("Calculated the time - will confirm it's 323 µs")
            assert output == "323", f"Expected 323 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformMsToµsConversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_ms_to_ns_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform MsToNs Conversion1"):
        try:
            print("Will calculate the time in ns")
            output = unit_converter_page.convert_time("ms","637","ns")
            print("Calculated the time - will confirm it's 637,000,000 ns")
            assert output == "637,000,000", f"Expected 637,000,000 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformMsToNsConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_ms_to_ns_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform MsToNs Conversion2"):
        try:
            print("Will calculate the time in ns")
            output = unit_converter_page.convert_time("ms","2585","ns")
            print("Calculated the time - will confirm it's 2,585,000,000 ns")
            assert output == "2,585,000,000", f"Expected 2,585,000,000 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformMsToNsConversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_ms_to_min_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform MsToMin Conversion1"):
        try:
            print("Will calculate the time in min")
            output = unit_converter_page.convert_time("ms","825","min")
            print("Calculated the time - will confirm it's 0.01375 min")
            assert output == "0.01375", f"Expected 0.01375 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformMsToMinConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_ms_to_min_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform MsToMin Conversion2"):
        try:
            print("Will calculate the time in min")
            output = unit_converter_page.convert_time("ms","92226","min")
            print("Calculated the time - will confirm it's 1.5371 min")
            assert output == "1.5371", f"Expected 1.5371 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformMsToMinConversion2")
            raise

############################################################################################
# MicroSecond
############################################################################################

@pytest.mark.timeout(175)
def test_perform_micros_to_hr_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform µsToHr Conversion1"):
        try:
            print("Will calculate the time in hr")
            output = unit_converter_page.convert_time("µs","55000000","h")
            print("Calculated the time - will confirm it's 0.015278 hr")
            assert output == "0.015278", f"Expected 0.015278 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformµsToHrConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_micros_to_hr_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform µsToHr Conversion2"):
        try:
            print("Will calculate the time in hr")
            output = unit_converter_page.convert_time("µs","888777666","h")
            print("Calculated the time - will confirm it's 0.24688 hr")
            assert output == "0.24688", f"Expected 0.24688 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformµsToHrConversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_micros_to_s_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform µsTos Conversion1"):
        try:
            print("Will calculate the time in sec")
            output = unit_converter_page.convert_time("µs","200000","s")
            print("Calculated the time - will confirm it's 0.2 s")
            assert output == "0.2", f"Expected 0.2 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformµsToSConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_micros_to_s_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform µsTos Conversion2"):
        try:
            print("Will calculate the time in sec")
            output = unit_converter_page.convert_time("µs","745","s")
            print("Calculated the time - will confirm it's 0.000745 s")
            assert output == "0.000745", f"Expected 0.000745 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformµsToSConversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_micros_to_ms_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform µsToms Conversion1"):
        try:
            print("Will calculate the time in ms")
            output = unit_converter_page.convert_time("µs","623","ms")
            print("Calculated the time - will confirm it's 0.623 ms")
            assert output == "0.623", f"Expected 0.623 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformµsTomsConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_micros_to_ms_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform µsToms Conversion2"):
        try:
            print("Will calculate the time in ms")
            output = unit_converter_page.convert_time("µs","250000","ms")
            print("Calculated the time - will confirm it's 250 ms")
            assert output == "250", f"Expected 250 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformµsTomsConversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_micros_to_ns_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform µsTons Conversion1"):
        try:
            print("Will calculate the time in ns")
            output = unit_converter_page.convert_time("µs","1250","ns")
            print("Calculated the time - will confirm it's 1,250,000 ns")
            assert output == "1,250,000", f"Expected 1,250,000 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformµsTonsConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_micros_to_ns_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform µsTons Conversion2"):
        try:
            print("Will calculate the time in ns")
            output = unit_converter_page.convert_time("µs","999","ns")
            print("Calculated the time - will confirm it's 999,000 ns")
            assert output == "999,000", f"Expected 999,000 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformµsTonsConversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_micros_to_min_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform µsToMin Conversion1"):
        try:
            print("Will calculate the time in min")
            output = unit_converter_page.convert_time("µs","1000000","min")
            print("Calculated the time - will confirm it's 0.016667 min")
            assert output == "0.016667", f"Expected 0.016667 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformµsToMinConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_micros_to_min_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform µsToMin Conversion2"):
        try:
            print("Will calculate the time in min")
            output = unit_converter_page.convert_time("µs","250000000","min")
            print("Calculated the time - will confirm it's 4.16667 min")
            assert output == "4.16667", f"Expected 4.16667 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformµsToMinConversion2")
            raise
        