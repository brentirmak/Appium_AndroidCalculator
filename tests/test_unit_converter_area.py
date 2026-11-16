'''
11/15/26 - 61 transactions
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

@pytest.mark.timeout(175)
def test_perform_square_m_to_square_mi_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform m²_to_mi² Conversion1"):
        try:
            print("Will calculate the area in mi²")
            output = unit_converter_page.convert_area("m²","9000000","mi²")
            print("Calculated the area - will confirm it's 3.47492 mi²")
            assert output == "3.47492", f"Expected 3.47492 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "Perform_m²_to_mi²_Conversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_square_m_to_square_mi_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform m²_to_mi² Conversion2"):
        try:
            print("Will calculate the area in mi²")
            output = unit_converter_page.convert_area("m²","6650","mi²")
            print("Calculated the area - will confirm it's 0.0025676 mi²")
            assert output == "0.0025676", f"Expected 0.0025676 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "Perform_m²_to_mi²_Conversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_square_m_to_square_yd_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform m²_to_yd² Conversion1"):
        try:
            print("Will calculate the area in yd²")
            output = unit_converter_page.convert_area("m²","20","yd²")
            print("Calculated the area - will confirm it's 23.9198 yd²")
            assert output == "23.9198", f"Expected 23.9198 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "Perform_m²_to_yd²_Conversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_square_m_to_square_yd_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform m²_to_yd² Conversion2"):
        try:
            print("Will calculate the area in yd²")
            output = unit_converter_page.convert_area("m²","68145","yd²")
            print("Calculated the area - will confirm it's 81,500.74171 yd²")
            assert output == "81,500.74171", f"Expected 81,500.74171 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "Perform_m²_to_yd²_Conversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_square_m_to_square_mm_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform m²_to_mm² Conversion1"):
        try:
            print("Will calculate the area in mm²")
            output = unit_converter_page.convert_area("m²","0.49","mm²")
            print("Calculated the area - will confirm it's 490,000 mm²")
            assert output == "490,000", f"Expected 490,000 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "Perform_m²_to_mm²_Conversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_square_m_to_square_mm_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform m²_to_mm² Conversion2"):
        try:
            print("Will calculate the area in mm²")
            output = unit_converter_page.convert_area("m²","850","mm²")
            print("Calculated the area - will confirm it's 850,000,000 mm²")
            assert output == "850,000,000", f"Expected 850,000,000 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "Perform_m²_to_mm²_Conversion2")
            raise

############################################################################################
# in²
############################################################################################

@pytest.mark.timeout(175)
def test_perform_square_in_to_square_m_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform in²_to_m² Conversion1"):
        try:
            print("Will calculate the area in m²")
            output = unit_converter_page.convert_area("in²","3600","m²")
            print("Calculated the area - will confirm it's 2.32258 m²")
            assert output == "2.32258", f"Expected 2.32258 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "Perform_in²_to_m²_Conversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_square_in_to_square_m_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform in²_to_m² Conversion2"):
        try:
            print("Will calculate the area in m²")
            output = unit_converter_page.convert_area("in²","99.75","m²")
            print("Calculated the area - will confirm it's 0.064355 m²")
            assert output == "0.064355", f"Expected 0.064355 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "Perform_in²_to_m²_Conversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_square_in_to_square_ft_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform in²_to_ft² Conversion1"):
        try:
            print("Will calculate the area in ft²")
            output = unit_converter_page.convert_area("in²","367.11","ft²")
            print("Calculated the area - will confirm it's 2.54938 ft²")
            assert output == "2.54938", f"Expected 2.54938 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "Perform_in²_to_ft²_Conversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_square_in_to_square_ft_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform in²_to_ft² Conversion2"):
        try:
            print("Will calculate the area in ft²")
            output = unit_converter_page.convert_area("in²","8500","ft²")
            print("Calculated the area - will confirm it's 59.027896 ft²")
            assert output == "59.027896", f"Expected 59.027896 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "Perform_in²_to_ft²_Conversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_square_in_to_square_mi_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform in²_to_mi² Conversion1"):
        try:
            print("Will calculate the area in mi²")
            output = unit_converter_page.convert_area("in²","777111200","mi²")
            print("Calculated the area - will confirm it's 0.19358 mi²")
            assert output == "0.19358", f"Expected 0.19358 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "Perform_in²_to_mi²_Conversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_square_in_to_square_mi_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform in²_to_mi² Conversion2"):
        try:
            print("Will calculate the area in mi²")
            output = unit_converter_page.convert_area("in²","10000000000","mi²")
            print("Calculated the area - will confirm it's 2.49098 mi²")
            assert output == "2.49098", f"Expected 2.49098 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "Perform_in²_to_mi²_Conversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_square_in_to_square_mi_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform in²_to_mi² Conversion1"):
        try:
            print("Will calculate the area in mi²")
            output = unit_converter_page.convert_area("in²","777111200","mi²")
            print("Calculated the area - will confirm it's 0.19358 mi²")
            assert output == "0.19358", f"Expected 0.19358 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "Perform_in²_to_mi²_Conversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_square_in_to_square_yd_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform in²_to_yd² Conversion1"):
        try:
            print("Will calculate the area in yd²")
            output = unit_converter_page.convert_area("in²","500","yd²")
            print("Calculated the area - will confirm it's 0.3858 yd²")
            assert output == "0.3858", f"Expected 0.3858 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "Perform_in²_to_yd²_Conversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_square_in_to_square_yd_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform in²_to_yd² Conversion2"):
        try:
            print("Will calculate the area in yd²")
            output = unit_converter_page.convert_area("in²","4630","yd²")
            print("Calculated the area - will confirm it's 3.57254 yd²")
            assert output == "3.57254", f"Expected 3.57254 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "Perform_in²_to_yd²_Conversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_square_in_to_square_mm_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform in²_to_mm² Conversion1"):
        try:
            print("Will calculate the area in mm²")
            output = unit_converter_page.convert_area("in²","2.7","mm²")
            print("Calculated the area - will confirm it's 1,741.93548 mm²")
            assert output == "1,741.93548", f"Expected 1,741.93548 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "Perform_in²_to_mm²_Conversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_square_in_to_square_mm_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform in²_to_mm² Conversion2"):
        try:
            print("Will calculate the area in mm²")
            output = unit_converter_page.convert_area("in²","133","mm²")
            print("Calculated the area - will confirm it's 85,806.45161 mm²")
            assert output == "85,806.45161", f"Expected 85,806.45161 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "Perform_in²_to_mm²_Conversion2")
            raise

############################################################################################
# ft²
############################################################################################

@pytest.mark.timeout(175)
def test_perform_square_ft_to_square_m_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform ft²_to_m² Conversion1"):
        try:
            print("Will calculate the area in m²")
            output = unit_converter_page.convert_area("ft²","5","m²")
            print("Calculated the area - will confirm it's 0.46452 m²")
            assert output == "0.46452", f"Expected 0.46452 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "Perform_ft²_to_m²_Conversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_square_ft_to_square_m_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform ft²_to_m² Conversion2"):
        try:
            print("Will calculate the area in m²")
            output = unit_converter_page.convert_area("ft²","29834","m²")
            print("Calculated the area - will confirm it's 2,771.6693 m²")
            assert output == "2,771.6693", f"Expected 2,771.6693 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "Perform_ft²_to_m²_Conversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_square_ft_to_square_in_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform ft²_to_in² Conversion1"):
        try:
            print("Will calculate the area in in²")
            output = unit_converter_page.convert_area("ft²","0.81","in²")
            print("Calculated the area - will confirm it's 116.63977 in²")
            assert output == "116.63977", f"Expected 116.63977 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "Perform_ft²_to_in²_Conversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_square_ft_to_square_in_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform ft²_to_in² Conversion2"):
        try:
            print("Will calculate the area in in²")
            output = unit_converter_page.convert_area("ft²","66","in²")
            print("Calculated the area - will confirm it's 9,503.98099 in²")
            assert output == "9,503.98099", f"Expected 9,503.98099 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "Perform_ft²_to_in²_Conversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_square_ft_to_square_mi_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform ft²_to_mi² Conversion1"):
        try:
            print("Will calculate the area in mi²")
            output = unit_converter_page.convert_area("ft²","1004400","mi²")
            print("Calculated the area - will confirm it's 0.036028 mi²")
            assert output == "0.036028", f"Expected 0.036028 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "Perform_ft²_to_mi²_Conversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_square_ft_to_square_mi_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform ft²_to_mi² Conversion2"):
        try:
            print("Will calculate the area in mi²")
            output = unit_converter_page.convert_area("ft²","33000000","mi²")
            print("Calculated the area - will confirm it's 1.18371 mi²")
            assert output == "1.18371", f"Expected 1.18371 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "Perform_ft²_to_mi²_Conversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_square_ft_to_square_yd_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform ft²_to_yd² Conversion1"):
        try:
            print("Will calculate the area in yd²")
            output = unit_converter_page.convert_area("ft²","0.68","yd²")
            print("Calculated the area - will confirm it's 0.075556 yd²")
            assert output == "0.075556", f"Expected 0.075556 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "Perform_ft²_to_yd²_Conversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_square_ft_to_square_yd_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform ft²_to_yd² Conversion2"):
        try:
            print("Will calculate the area in yd²")
            output = unit_converter_page.convert_area("ft²","324","yd²")
            print("Calculated the area - will confirm it's 36 yd²")
            assert output == "36", f"Expected 36 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "Perform_ft²_to_yd²_Conversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_square_ft_to_square_mm_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform ft²_to_mm² Conversion1"):
        try:
            print("Will calculate the area in mm²")
            output = unit_converter_page.convert_area("ft²","2.5","mm²")
            print("Calculated the area - will confirm it's 232,257.6 mm²")
            assert output == "232,257.6", f"Expected 232,257.6 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "Perform_ft²_to_mm²_Conversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_square_ft_to_square_mm_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform ft²_to_mm² Conversion2"):
        try:
            print("Will calculate the area in mm²")
            output = unit_converter_page.convert_area("ft²","0.07","mm²")
            print("Calculated the area - will confirm it's 6,503.2128 mm²")
            assert output == "6,503.2128", f"Expected 6,503.2128 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "Perform_ft²_to_mm²_Conversion2")
            raise

############################################################################################
# mi²
############################################################################################

@pytest.mark.timeout(175)
def test_perform_square_mi_to_square_m_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform mi²_to_m² Conversion1"):
        try:
            print("Will calculate the area in m²")
            output = unit_converter_page.convert_area("mi²","0.005","m²")
            print("Calculated the area - will confirm it's 12,949.94055 m²")
            assert output == "12,949.94055", f"Expected 12,949.94055 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "Perform_mi²_to_m²_Conversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_square_mi_to_square_m_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform mi²_to_m² Conversion2"):
        try:
            print("Will calculate the area in m²")
            output = unit_converter_page.convert_area("mi²","0.0008","m²")
            print("Calculated the area - will confirm it's 2,071.99049 m²")
            assert output == "2,071.99049", f"Expected 2,071.99049 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "Perform_mi²_to_m²_Conversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_square_mi_to_square_in_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform mi²_to_in² Conversion1"):
        try:
            print("Will calculate the area in in²")
            output = unit_converter_page.convert_area("mi²","0.000001","in²")
            print("Calculated the area - will confirm it's 4,014.48157 in²")
            assert output == "4,014.48157", f"Expected 4,014.48157 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "Perform_mi²_to_in²_Conversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_square_mi_to_square_in_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform mi²_to_in² Conversion2"):
        try:
            print("Will calculate the area in in²")
            output = unit_converter_page.convert_area("mi²","0.000000008","in²")
            print("Calculated the area - will confirm it's 32.11585 in²")
            assert output == "32.11585", f"Expected 32.11585 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "Perform_mi²_to_in²_Conversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_square_mi_to_square_ft_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform mi²_to_ft² Conversion1"):
        try:
            print("Will calculate the area in ft²")
            output = unit_converter_page.convert_area("mi²","0.01","ft²")
            print("Calculated the area - will confirm it's 278,784 ft²")
            assert output == "278,784", f"Expected 278,784 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "Perform_mi²_to_ft²_Conversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_square_mi_to_square_ft_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform mi²_to_ft² Conversion2"):
        try:
            print("Will calculate the area in ft²")
            output = unit_converter_page.convert_area("mi²","2","ft²")
            print("Calculated the area - will confirm it's 55,756,799.99923 ft²")
            assert output == "55,756,799.99923", f"Expected 55,756,799.99923 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "Perform_mi²_to_ft²_Conversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_square_mi_to_square_yd_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform mi²_to_yd² Conversion1"):
        try:
            print("Will calculate the area in yd²")
            output = unit_converter_page.convert_area("mi²","0.009","yd²")
            print("Calculated the area - will confirm it's 27,878.4 yd²")
            assert output == "27,878.4", f"Expected 27,878.4 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "Perform_mi²_to_yd²_Conversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_square_mi_to_square_yd_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform mi²_to_yd² Conversion2"):
        try:
            print("Will calculate the area in yd²")
            output = unit_converter_page.convert_area("mi²","9.2","yd²")
            print("Calculated the area - will confirm it's 28,497,919.9996 yd²")
            assert output == "28,497,919.9996", f"Expected 28,497,919.9996 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "Perform_mi²_to_yd²_Conversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_square_mi_to_square_mm_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform mi²_to_mm² Conversion1"):
        try:
            print("Will calculate the area in mm²")
            output = unit_converter_page.convert_area("mi²","0.00002","mm²")
            print("Calculated the area - will confirm it's 51,799,762.206 mm²")
            assert output == "51,799,762.206", f"Expected 51,799,762.206 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "Perform_mi²_to_mm²_Conversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_square_mi_to_square_mm_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform mi²_to_mm² Conversion2"):
        try:
            print("Will calculate the area in mm²")
            output = unit_converter_page.convert_area("mi²","0.00002","mm²")
            print("Calculated the area - will confirm it's 51,799,762.206 mm²")
            assert output == "51,799,762.206", f"Expected 51,799,762.206 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "Perform_mi²_to_mm²_Conversion2")
            raise

############################################################################################
# yd²
############################################################################################

@pytest.mark.timeout(175)
def test_perform_square_yd_to_square_m_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform yd²_to_m² Conversion1"):
        try:
            print("Will calculate the area in m²")
            output = unit_converter_page.convert_area("yd²","35","m²")
            print("Calculated the area - will confirm it's 29.26446 m²")
            assert output == "29.26446", f"Expected 29.26446 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "Perform_yd²_to_m²_Conversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_square_yd_to_square_m_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform yd²_to_m² Conversion2"):
        try:
            print("Will calculate the area in m²")
            output = unit_converter_page.convert_area("yd²","99.005","m²")
            print("Calculated the area - will confirm it's 82.78079 m²")
            assert output == "82.78079", f"Expected 82.78079 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "Perform_yd²_to_m²_Conversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_square_yd_to_square_in_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform yd²_to_in² Conversion1"):
        try:
            print("Will calculate the area in in²")
            output = unit_converter_page.convert_area("yd²","3","in²")
            print("Calculated the area - will confirm it's 3,887.99222 in²")
            assert output == "3,887.99222", f"Expected 3,887.99222 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "Perform_yd²_to_in²_Conversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_square_yd_to_square_in_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform yd²_to_in² Conversion2"):
        try:
            print("Will calculate the area in in²")
            output = unit_converter_page.convert_area("yd²","88.66","in²")
            print("Calculated the area - will confirm it's 114,903.13019 in²")
            assert output == "114,903.13019", f"Expected 114,903.13019 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "Perform_yd²_to_in²_Conversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_square_yd_to_square_ft_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform yd²_to_ft² Conversion1"):
        try:
            print("Will calculate the area in ft²")
            output = unit_converter_page.convert_area("yd²","420","ft²")
            print("Calculated the area - will confirm it's 3,780 ft²")
            assert output == "3,780", f"Expected 3,780 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "Perform_yd²_to_ft²_Conversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_square_yd_to_square_ft_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform yd²_to_ft² Conversion2"):
        try:
            print("Will calculate the area in ft²")
            output = unit_converter_page.convert_area("yd²","201689","ft²")
            print("Calculated the area - will confirm it's 1,815,201 ft²")
            assert output == "1,815,201", f"Expected 1,815,201 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "Perform_yd²_to_ft²_Conversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_square_yd_to_square_mi_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform yd²_to_mi² Conversion1"):
        try:
            print("Will calculate the area in mi²")
            output = unit_converter_page.convert_area("yd²","7500000","mi²")
            print("Calculated the area - will confirm it's 2.42123 mi²")
            assert output == "2.42123", f"Expected 2.42123 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "Perform_yd²_to_mi²_Conversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_square_yd_to_square_mi_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform yd²_to_mi² Conversion2"):
        try:
            print("Will calculate the area in mi²")
            output = unit_converter_page.convert_area("yd²","825000","mi²")
            print("Calculated the area - will confirm it's 0.26634 mi²")
            assert output == "0.26634", f"Expected 0.26634 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "Perform_yd²_to_mi²_Conversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_square_yd_to_square_mm_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform yd²_to_mm² Conversion1"):
        try:
            print("Will calculate the area in mm²")
            output = unit_converter_page.convert_area("yd²","100","mm²")
            print("Calculated the area - will confirm it's 83,612,736 mm²")
            assert output == "83,612,736", f"Expected 83,612,736 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "Perform_yd²_to_mm²_Conversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_square_yd_to_square_mm_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform yd²_to_mm² Conversion2"):
        try:
            print("Will calculate the area in mm²")
            output = unit_converter_page.convert_area("yd²","0.004","mm²")
            print("Calculated the area - will confirm it's 3,344.50944 mm²")
            assert output == "3,344.50944", f"Expected 3,344.50944 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "Perform_yd²_to_mm²_Conversion2")
            raise

############################################################################################
# mm²
############################################################################################

@pytest.mark.timeout(175)
def test_perform_square_mm_to_square_m_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform mm²_to_m² Conversion1"):
        try:
            print("Will calculate the area in m²")
            output = unit_converter_page.convert_area("mm²","6500","m²")
            print("Calculated the area - will confirm it's 0.0065 m²")
            assert output == "0.0065", f"Expected 0.0065 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "Perform_mm²_to_m²_Conversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_square_mm_to_square_m_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform mm²_to_m² Conversion2"):
        try:
            print("Will calculate the area in m²")
            output = unit_converter_page.convert_area("mm²","2257500","m²")
            print("Calculated the area - will confirm it's 2.2575 m²")
            assert output == "2.2575", f"Expected 2.2575 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "Perform_mm²_to_m²_Conversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_square_mm_to_square_in_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform mm²_to_in² Conversion1"):
        try:
            print("Will calculate the area in in²")
            output = unit_converter_page.convert_area("mm²","85","in²")
            print("Calculated the area - will confirm it's 0.13175 in²")
            assert output == "0.13175", f"Expected 0.13175 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "Perform_mm²_to_in²_Conversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_square_mm_to_square_in_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform mm²_to_in² Conversion2"):
        try:
            print("Will calculate the area in in²")
            output = unit_converter_page.convert_area("mm²","777000","in²")
            print("Calculated the area - will confirm it's 1,204.35 in²")
            assert output == "1,204.35", f"Expected 1,204.35 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "Perform_mm²_to_in²_Conversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_square_mm_to_square_ft_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform mm²_to_ft² Conversion1"):
        try:
            print("Will calculate the area in ft²")
            output = unit_converter_page.convert_area("mm²","130055","ft²")
            print("Calculated the area - will confirm it's 1.3999 ft²")
            assert output == "1.3999", f"Expected 1.3999 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "Perform_mm²_to_ft²_Conversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_square_mm_to_square_ft_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform mm²_to_ft² Conversion2"):
        try:
            print("Will calculate the area in ft²")
            output = unit_converter_page.convert_area("mm²","47000000","ft²")
            print("Calculated the area - will confirm it's 505.90379 ft²")
            assert output == "505.90379", f"Expected 505.90379 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "Perform_mm²_to_ft²_Conversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_square_mm_to_square_mi_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform mm²_to_mi² Conversion1"):
        try:
            print("Will calculate the area in mi²")
            output = unit_converter_page.convert_area("mm²","1000000000","mi²")
            print("Calculated the area - will confirm it's 0.0003861 mi²")
            assert output == "0.0003861", f"Expected 0.0003861 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "Perform_mm²_to_mi²_Conversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_square_mm_to_square_mi_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform mm²_to_mi² Conversion2"):
        try:
            print("Will calculate the area in mi²")
            output = unit_converter_page.convert_area("mm²","525000000000","mi²")
            print("Calculated the area - will confirm it's 0.2027 mi²")
            assert output == "0.2027", f"Expected 0.2027 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "Perform_mm²_to_mi²_Conversion2")
            raise

@pytest.mark.timeout(175)
def test_perform_square_mm_to_square_yd_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform mm²_to_yd² Conversion1"):
        try:
            print("Will calculate the area in yd²")
            output = unit_converter_page.convert_area("mm²","99550","yd²")
            print("Calculated the area - will confirm it's 0.11906 yd²")
            assert output == "0.11906", f"Expected 0.11906 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "Perform_mm²_to_yd²_Conversion1")
            raise

@pytest.mark.timeout(175)
def test_perform_square_mm_to_square_yd_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform mm²_to_yd² Conversion2"):
        try:
            print("Will calculate the area in yd²")
            output = unit_converter_page.convert_area("mm²","4447770","yd²")
            print("Calculated the area - will confirm it's 5.31949 yd²")
            assert output == "5.31949", f"Expected 5.31949 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "Perform_mm²_to_yd²_Conversion2")
            raise