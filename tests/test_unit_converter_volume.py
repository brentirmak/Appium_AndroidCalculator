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

############################################################################################
# dL
############################################################################################

@pytest.mark.timeout(175)
def test_perform_dl_to_l_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform dLToL Conversion1"):
        try:
            print("Will calculate the volume in L")
            output = unit_converter_page.convert_volume("dL","0.09","L")
            print("Calculated the mass - will confirm it's 0.009 L")
            assert output == "0.009", f"Expected 0.009 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformdLToLConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_dl_to_l_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform dLToL Conversion2"):
        try:
            print("Will calculate the volume in L")
            output = unit_converter_page.convert_volume("dL","65000","L")
            print("Calculated the mass - will confirm it's 6,500 L")
            assert output == "6,500", f"Expected 6,500 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformdLToLConversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_dl_to_ml_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform dLTomL Conversion1"):
        try:
            print("Will calculate the volume in mL")
            output = unit_converter_page.convert_volume("dL","22.073","mL")
            print("Calculated the mass - will confirm it's 2,207.3 mL")
            assert output == "2,207.3", f"Expected 2,207.3 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformdLTomLConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_dl_to_ml_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform dLTomL Conversion2"):
        try:
            print("Will calculate the volume in mL")
            output = unit_converter_page.convert_volume("dL","555","mL")
            print("Calculated the mass - will confirm it's 55,500 mL")
            assert output == "55,500", f"Expected 55,500 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformdLTomLConversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_dl_to_cl_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform dLTocL Conversion1"):
        try:
            print("Will calculate the volume in cL")
            output = unit_converter_page.convert_volume("dL","9630","cL")
            print("Calculated the mass - will confirm it's 96,300 cL")
            assert output == "96,300", f"Expected 96,300 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformdLTocLConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_dl_to_cl_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform dLTocL Conversion2"):
        try:
            print("Will calculate the volume in cL")
            output = unit_converter_page.convert_volume("dL","77.250","cL")
            print("Calculated the mass - will confirm it's 772.5 cL")
            assert output == "772.5", f"Expected 772.5 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformdLTocLConversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_dl_to_hl_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform dLTohL Conversion1"):
        try:
            print("Will calculate the volume in hL")
            output = unit_converter_page.convert_volume("dL","0.2","hL")
            print("Calculated the mass - will confirm it's 0.0002 hL")
            assert output == "0.0002", f"Expected 0.0002 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformdLTohLConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_dl_to_hl_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform dLTohL Conversion2"):
        try:
            print("Will calculate the volume in hL")
            output = unit_converter_page.convert_volume("dL","10000","hL")
            print("Calculated the mass - will confirm it's 10 hL")
            assert output == "10", f"Expected 10 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformdLTohLConversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_dl_to_kl_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform dLTokL Conversion1"):
        try:
            print("Will calculate the volume in kL")
            output = unit_converter_page.convert_volume("dL","768231","kL")
            print("Calculated the mass - will confirm it's 76.8231 kL")
            assert output == "76.8231", f"Expected 76.8231 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformdLTokLConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_dl_to_kl_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform dLTokL Conversion2"):
        try:
            print("Will calculate the volume in kL")
            output = unit_converter_page.convert_volume("dL","2500","kL")
            print("Calculated the mass - will confirm it's 0.25 kL")
            assert output == "0.25", f"Expected 0.25 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformdLTokLConversion2")
            raise

############################################################################################
# hL
############################################################################################

@pytest.mark.timeout(175)
def test_perform_hl_to_l_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform hLToL Conversion1"):
        try:
            print("Will calculate the volume in L")
            output = unit_converter_page.convert_volume("hL","95","L")
            print("Calculated the mass - will confirm it's 9,500 L")
            assert output == "9,500", f"Expected 9,500 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformhLToLConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_hl_to_l_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform hLToL Conversion2"):
        try:
            print("Will calculate the volume in L")
            output = unit_converter_page.convert_volume("hL","0.89","L")
            print("Calculated the mass - will confirm it's 89 L")
            assert output == "89", f"Expected 89 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformhLToLConversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_hl_to_ml_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform hLTomL Conversion1"):
        try:
            print("Will calculate the volume in mL")
            output = unit_converter_page.convert_volume("hL","741","mL")
            print("Calculated the mass - will confirm it's 74,100,000 mL")
            assert output == "74,100,000", f"Expected 74,100,000 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformhLTomLConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_hl_to_ml_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform hLTomL Conversion2"):
        try:
            print("Will calculate the volume in mL")
            output = unit_converter_page.convert_volume("hL","0.305","mL")
            print("Calculated the mass - will confirm it's 30,500 mL")
            assert output == "30,500", f"Expected 30,500 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformhLTomLConversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_hl_to_cl_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform hLTocL Conversion1"):
        try:
            print("Will calculate the volume in cL")
            output = unit_converter_page.convert_volume("hL","0.02","cL")
            print("Calculated the mass - will confirm it's 200 cL")
            assert output == "200", f"Expected 200 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformhLTocLConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_hl_to_cl_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform hLTocL Conversion2"):
        try:
            print("Will calculate the volume in cL")
            output = unit_converter_page.convert_volume("hL","6815","cL")
            print("Calculated the mass - will confirm it's 68,150,000 cL")
            assert output == "68,150,000", f"Expected 68,150,000 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformhLTocLConversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_hl_to_dl_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform hLTodL Conversion1"):
        try:
            print("Will calculate the volume in dL")
            output = unit_converter_page.convert_volume("hL","0.69","dL")
            print("Calculated the mass - will confirm it's 690 dL")
            assert output == "690", f"Expected 690 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformhLTodLConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_hl_to_dl_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform hLTodL Conversion2"):
        try:
            print("Will calculate the volume in dL")
            output = unit_converter_page.convert_volume("hL","2500","dL")
            print("Calculated the mass - will confirm it's 2,500,000 dL")
            assert output == "2,500,000", f"Expected 2,500,000 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformhLTodLConversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_hl_to_kl_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform hLTokL Conversion1"):
        try:
            print("Will calculate the volume in kL")
            output = unit_converter_page.convert_volume("hL","777","kL")
            print("Calculated the mass - will confirm it's 77.7 kL")
            assert output == "77.7", f"Expected 77.7 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformhLTokLConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_hl_to_kl_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform hLTokL Conversion2"):
        try:
            print("Will calculate the volume in kL")
            output = unit_converter_page.convert_volume("hL","0.004","kL")
            print("Calculated the mass - will confirm it's 0.0004 kL")
            assert output == "0.0004", f"Expected 0.0004 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformhLTokLConversion2")
            raise

############################################################################################
# kL
############################################################################################

@pytest.mark.timeout(175)
def test_perform_kl_to_l_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform kLToL Conversion1"):
        try:
            print("Will calculate the volume in L")
            output = unit_converter_page.convert_volume("kL","10","L")
            print("Calculated the mass - will confirm it's 10,000 L")
            assert output == "10,000", f"Expected 10,000 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformkLToLConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_kl_to_l_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform kLToL Conversion2"):
        try:
            print("Will calculate the volume in L")
            output = unit_converter_page.convert_volume("kL","3.5","L")
            print("Calculated the mass - will confirm it's 3,500 L")
            assert output == "3,500", f"Expected 3,500 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformkLToLConversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_kl_to_ml_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform kLTomL Conversion1"):
        try:
            print("Will calculate the volume in mL")
            output = unit_converter_page.convert_volume("kL","0.64","mL")
            print("Calculated the mass - will confirm it's 640,000 mL")
            assert output == "640,000", f"Expected 640,000 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformkLTomLConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_kl_to_ml_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform kLTomL Conversion2"):
        try:
            print("Will calculate the volume in mL")
            output = unit_converter_page.convert_volume("kL","4.5","mL")
            print("Calculated the mass - will confirm it's 4,500,000 mL")
            assert output == "4,500,000", f"Expected 4,500,000 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformkLTomLConversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_kl_to_cl_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform kLTocL Conversion1"):
        try:
            print("Will calculate the volume in cL")
            output = unit_converter_page.convert_volume("kL","0.009","cL")
            print("Calculated the mass - will confirm it's 900 cL")
            assert output == "900", f"Expected 900 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformkLTocLConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_kl_to_cl_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform kLTocL Conversion2"):
        try:
            print("Will calculate the volume in cL")
            output = unit_converter_page.convert_volume("kL","5.005","cL")
            print("Calculated the mass - will confirm it's 500,500 cL")
            assert output == "500,500", f"Expected 500,500 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformkLTocLConversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_kl_to_dl_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform kLTodL Conversion1"):
        try:
            print("Will calculate the volume in dL")
            output = unit_converter_page.convert_volume("kL","975","dL")
            print("Calculated the mass - will confirm it's 9,750,000 dL")
            assert output == "9,750,000", f"Expected 9,750,000 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformkLTodLConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_kl_to_dl_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform kLTodL Conversion2"):
        try:
            print("Will calculate the volume in dL")
            output = unit_converter_page.convert_volume("kL","0.0008","dL")
            print("Calculated the mass - will confirm it's 8 dL")
            assert output == "8", f"Expected 8 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformkLTodLConversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_kl_to_hl_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform kLTohL Conversion1"):
        try:
            print("Will calculate the volume in hL")
            output = unit_converter_page.convert_volume("kL","35","hL")
            print("Calculated the mass - will confirm it's 350 hL")
            assert output == "350", f"Expected 350 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformkLTohLConversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_kl_to_hl_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform kLTohL Conversion2"):
        try:
            print("Will calculate the volume in hL")
            output = unit_converter_page.convert_volume("kL","0.6","hL")
            print("Calculated the mass - will confirm it's 6 hL")
            assert output == "6", f"Expected 6 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformkLTohLConversion2")
            raise