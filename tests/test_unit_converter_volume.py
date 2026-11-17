'''
11/17/26 -  transactions
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
            unit_converter_page.select_conversion_type_value("Volume")

            conversion_type = unit_converter_page.get_conversion_type()
            assert conversion_type == "Volume", f"Expected 'Volume' but got '{conversion_type}'"

        except Exception:
            capture_error_snapshot(driver, "AccessUnitConverter")
            raise


############################################################################################
# L
############################################################################################

@pytest.mark.timeout(175)
def test_perform_l_to_ml_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform LTomL Conversion1"):
        try:
            print("Will calculate the volume in mL")
            output = unit_converter_page.convert_volume("L","2","mL")
            print("Calculated the mass - will confirm it's 2,000 mL")
            assert output == "2,000", f"Expected 2,000 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformLTomLConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_l_to_ml_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform LTomL Conversion2"):
        try:
            print("Will calculate the volume in mL")
            output = unit_converter_page.convert_volume("L","0.05","mL")
            print("Calculated the mass - will confirm it's 50 mL")
            assert output == "50", f"Expected 50 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformLTomLConversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_l_to_cl_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform LTocL Conversion1"):
        try:
            print("Will calculate the volume in cL")
            output = unit_converter_page.convert_volume("L","225","cL")
            print("Calculated the mass - will confirm it's 22,500 cL")
            assert output == "22,500", f"Expected 22,500 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformLTocLConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_l_to_cl_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform LTocL Conversion2"):
        try:
            print("Will calculate the volume in cL")
            output = unit_converter_page.convert_volume("L","785.66","cL")
            print("Calculated the mass - will confirm it's 78,566 cL")
            assert output == "78,566", f"Expected 78,566 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformLTocLConversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_l_to_dl_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform LTodL Conversion1"):
        try:
            print("Will calculate the volume in dL")
            output = unit_converter_page.convert_volume("L","45.853","dL")
            print("Calculated the mass - will confirm it's 458.53 dL")
            assert output == "458.53", f"Expected 458.53 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformLTodLConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_l_to_dl_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform LTodL Conversion2"):
        try:
            print("Will calculate the volume in dL")
            output = unit_converter_page.convert_volume("L","85671","dL")
            print("Calculated the mass - will confirm it's 856,710 dL")
            assert output == "856,710", f"Expected 856,710 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformLTodLConversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_l_to_hl_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform LTohL Conversion1"):
        try:
            print("Will calculate the volume in hL")
            output = unit_converter_page.convert_volume("L","332","hL")
            print("Calculated the mass - will confirm it's 3.32 hL")
            assert output == "3.32", f"Expected 3.32 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformLTohLConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_l_to_hl_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform LTohL Conversion2"):
        try:
            print("Will calculate the volume in hL")
            output = unit_converter_page.convert_volume("L","719900","hL")
            print("Calculated the mass - will confirm it's 7,199 hL")
            assert output == "7,199", f"Expected 7,199 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformLTohLConversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_l_to_kl_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform LTokL Conversion1"):
        try:
            print("Will calculate the volume in kL")
            output = unit_converter_page.convert_volume("L","0.26","kL")
            print("Calculated the mass - will confirm it's 0.00026 kL")
            assert output == "0.00026", f"Expected 0.00026 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformLTokLConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_l_to_kl_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform LTokL Conversion2"):
        try:
            print("Will calculate the volume in kL")
            output = unit_converter_page.convert_volume("L","88.605","kL")
            print("Calculated the mass - will confirm it's 0.088605 kL")
            assert output == "0.088605", f"Expected 0.088605 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformLTokLConversion2")
            raise

############################################################################################
# mL
############################################################################################

@pytest.mark.timeout(175)
def test_perform_ml_to_l_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform mLToL Conversion1"):
        try:
            print("Will calculate the volume in L")
            output = unit_converter_page.convert_volume("mL","9000","L")
            print("Calculated the mass - will confirm it's 9 L")
            assert output == "9", f"Expected 9 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformmLToLConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_ml_to_l_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform mLToL Conversion2"):
        try:
            print("Will calculate the volume in L")
            output = unit_converter_page.convert_volume("mL","666.403","L")
            print("Calculated the mass - will confirm it's 0.6664 L")
            assert output == "0.6664", f"Expected 0.6664 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformmLToLConversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_ml_to_cl_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform mLTocL Conversion1"):
        try:
            print("Will calculate the volume in cL")
            output = unit_converter_page.convert_volume("mL","75","cL")
            print("Calculated the mass - will confirm it's 7.5 cL")
            assert output == "7.5", f"Expected 7.5 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformmLTocLConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_ml_to_cl_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform mLTocL Conversion2"):
        try:
            print("Will calculate the volume in cL")
            output = unit_converter_page.convert_volume("mL","8610000","cL")
            print("Calculated the mass - will confirm it's 861,000 cL")
            assert output == "861,000", f"Expected 861,000 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformmLTocLConversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_ml_to_dl_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform mLTodL Conversion1"):
        try:
            print("Will calculate the volume in dL")
            output = unit_converter_page.convert_volume("mL","52.86","dL")
            print("Calculated the mass - will confirm it's 0.5286 dL")
            assert output == "0.5286", f"Expected 0.5286 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformmLTodLConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_ml_to_dl_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform mLTodL Conversion2"):
        try:
            print("Will calculate the volume in dL")
            output = unit_converter_page.convert_volume("mL","7","dL")
            print("Calculated the mass - will confirm it's 0.07 dL")
            assert output == "0.07", f"Expected 0.07 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformmLTodLConversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_ml_to_hl_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform mLTohL Conversion1"):
        try:
            print("Will calculate the volume in hL")
            output = unit_converter_page.convert_volume("mL","325000","hL")
            print("Calculated the mass - will confirm it's 3.25 hL")
            assert output == "3.25", f"Expected 3.25 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformmLTohLConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_ml_to_hl_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform mLTohL Conversion2"):
        try:
            print("Will calculate the volume in hL")
            output = unit_converter_page.convert_volume("mL","999666333","hL")
            print("Calculated the mass - will confirm it's 9,996.66333 hL")
            assert output == "9,996.66333", f"Expected 9,996.66333 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformmLTohLConversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_ml_to_kl_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform mLTokL Conversion1"):
        try:
            print("Will calculate the volume in kL")
            output = unit_converter_page.convert_volume("mL","178","kL")
            print("Calculated the mass - will confirm it's 0.000178 kL")
            assert output == "0.000178", f"Expected 0.000178 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformmLTokLConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_ml_to_kl_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform mLTokL Conversion2"):
        try:
            print("Will calculate the volume in kL")
            output = unit_converter_page.convert_volume("mL","2059540","kL")
            print("Calculated the mass - will confirm it's 2.05954 kL")
            assert output == "2.05954", f"Expected 2.05954 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformmLTokLConversion2")
            raise

############################################################################################
# cL
############################################################################################

@pytest.mark.timeout(175)
def test_perform_cl_to_l_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform cLToL Conversion1"):
        try:
            print("Will calculate the volume in L")
            output = unit_converter_page.convert_volume("cL","50000","L")
            print("Calculated the mass - will confirm it's 500 L")
            assert output == "500", f"Expected 500 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformcLToLConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_cl_to_l_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform cLToL Conversion2"):
        try:
            print("Will calculate the volume in L")
            output = unit_converter_page.convert_volume("cL","25.25","L")
            print("Calculated the mass - will confirm it's 0.2525 L")
            assert output == "0.2525", f"Expected 0.2525 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformcLToLConversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_cl_to_ml_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform cLTomL Conversion1"):
        try:
            print("Will calculate the volume in mL")
            output = unit_converter_page.convert_volume("cL","666","mL")
            print("Calculated the mass - will confirm it's 6,660 mL")
            assert output == "6,660", f"Expected 6,660 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformcLTomLConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_cl_to_ml_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform cLTomL Conversion2"):
        try:
            print("Will calculate the volume in mL")
            output = unit_converter_page.convert_volume("cL","0.007","mL")
            print("Calculated the mass - will confirm it's 0.07 mL")
            assert output == "0.07", f"Expected 0.07 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformcLTomLConversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_cl_to_dl_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform cLTodL Conversion1"):
        try:
            print("Will calculate the volume in dL")
            output = unit_converter_page.convert_volume("cL","9123","dL")
            print("Calculated the mass - will confirm it's 912.3 dL")
            assert output == "912.3", f"Expected 912.3 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformcLTodLConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_cl_to_dl_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform cLTodL Conversion2"):
        try:
            print("Will calculate the volume in dL")
            output = unit_converter_page.convert_volume("cL","55.204","dL")
            print("Calculated the mass - will confirm it's 5.5204 dL")
            assert output == "5.5204", f"Expected 5.5204 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformcLTodLConversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_cl_to_hl_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform cLTohL Conversion1"):
        try:
            print("Will calculate the volume in hL")
            output = unit_converter_page.convert_volume("cL","3.1114","hL")
            print("Calculated the mass - will confirm it's 0.00031114 hL")
            assert output == "0.00031114", f"Expected 0.00031114 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformcLTohLConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_cl_to_hl_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform cLTohL Conversion2"):
        try:
            print("Will calculate the volume in hL")
            output = unit_converter_page.convert_volume("cL","215000","hL")
            print("Calculated the mass - will confirm it's 21.5 hL")
            assert output == "21.5", f"Expected 21.5 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformcLTohLConversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_cl_to_kl_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform cLTokL Conversion1"):
        try:
            print("Will calculate the volume in kL")
            output = unit_converter_page.convert_volume("cL","800000","kL")
            print("Calculated the mass - will confirm it's 8 kL")
            assert output == "8", f"Expected 8 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformcLTokLConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_cl_to_kl_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform cLTokL Conversion2"):
        try:
            print("Will calculate the volume in kL")
            output = unit_converter_page.convert_volume("cL","125000000","kL")
            print("Calculated the mass - will confirm it's 1,250 kL")
            assert output == "1,250", f"Expected 1,250 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformcLTokLConversion2")
            raise