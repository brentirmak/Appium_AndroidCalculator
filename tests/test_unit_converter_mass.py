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

def test_perform_kg_to_g_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform KgTog Conversion2"):
        try:
            print("Will calculate the mass in g")
            output = unit_converter_page.convert_kg_to_g("0.9")
            print("Calculated the mass - will confirm it's 900 g")
            assert output == "900", f"Expected 900 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformKgTogConversion2")
            raise

def test_perform_kg_to_oz_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform KgToOz Conversion1"):
        try:
            print("Will calculate the mass in oz")
            output = unit_converter_page.convert_kg_to_oz("4")
            print("Calculated the mass - will confirm it's 141.096 oz")
            assert output == "141.096", f"Expected 141.096 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformKgToOzConversion1")
            raise

def test_perform_kg_to_oz_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform KgToOz Conversion2"):
        try:
            print("Will calculate the mass in oz")
            output = unit_converter_page.convert_kg_to_oz("88")
            print("Calculated the mass - will confirm it's 3,104.112 oz")
            assert output == "3,104.112", f"Expected 3,104.112 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformKgToOzConversion2")
            raise

def test_perform_kg_to_t_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform KgToT Conversion1"):
        try:
            print("Will calculate the mass in t")
            output = unit_converter_page.convert_kg_to_t("364855")
            print("Calculated the mass - will confirm it's 364.855 t")
            assert output == "364.855", f"Expected 364.855 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformKgToTConversion1")
            raise

def test_perform_kg_to_t_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform KgToT Conversion2"):
        try:
            print("Will calculate the mass in t")
            output = unit_converter_page.convert_kg_to_t("2500")
            print("Calculated the mass - will confirm it's 2.5 t")
            assert output == "2.5", f"Expected 2.5 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformKgToTConversion2")
            raise

def test_perform_lb_to_kg_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform LbToKg Conversion1"):
        try:
            print("Will calculate the mass in Kg")
            output = unit_converter_page.convert_lb_to_kg("970")
            print("Calculated the mass - will confirm it's 439.9846 kg")
            assert output == "439.9846", f"Expected 439.9846 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformLbToKgConversion1")
            raise

def test_perform_lb_to_kg_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform LbToKg Conversion2"):
        try:
            print("Will calculate the mass in Kg")
            output = unit_converter_page.convert_lb_to_kg("18")
            print("Calculated the mass - will confirm it's 8.16466 kg")
            assert output == "8.16466", f"Expected 8.16466 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformLbToKgConversion2")
            raise

def test_perform_lb_to_mg_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform LbToMg Conversion1"):
        try:
            print("Will calculate the mass in Mg")
            output = unit_converter_page.convert_lb_to_mg("0.085")
            print("Calculated the mass - will confirm it's 38555.35145 mg")
            assert output == "38,555.35145", f"Expected 38,555.35145 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformLbToMgConversion1")
            raise

def test_perform_lb_to_mg_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform LbToMg Conversion2"):
        try:
            print("Will calculate the mass in Mg")
            output = unit_converter_page.convert_lb_to_mg("3.70")
            print("Calculated the mass - will confirm it's 1,678,291.76888 mg")
            assert output == "1,678,291.76888", f"Expected 1,678,291.76888 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformLbToMgConversion2")
            raise

def test_perform_lb_to_g_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform LbToG Conversion1"):
        try:
            print("Will calculate the mass in g")
            output = unit_converter_page.convert_lb_to_g("5")
            print("Calculated the mass - will confirm it's 2,267.96185 g")
            assert output == "2,267.96185", f"Expected 2,267.96185 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformLbToGConversion1")
            raise

def test_perform_lb_to_g_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform LbToG Conversion2"):
        try:
            print("Will calculate the mass in g")
            output = unit_converter_page.convert_lb_to_g("2.05")
            print("Calculated the mass - will confirm it's 929.86436 g")
            assert output == "929.86436", f"Expected 929.86436 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformLbToGConversion2")
            raise

def test_perform_lb_to_oz_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform LbToOz Conversion1"):
        try:
            print("Will calculate the mass in oz")
            output = unit_converter_page.convert_lb_to_oz("0.008")
            print("Calculated the mass - will confirm it's 0.128 oz")
            assert output == "0.128", f"Expected 0.128 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformLbToOzConversion1")
            raise

def test_perform_lb_to_oz_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform LbToOz Conversion2"):
        try:
            print("Will calculate the mass in oz")
            output = unit_converter_page.convert_lb_to_oz("0.00075")
            print("Calculated the mass - will confirm it's 0.012 oz")
            assert output == "0.012", f"Expected 0.012 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformLbToOzConversion2")
            raise

def test_perform_lb_to_t_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform LbToT Conversion1"):
        try:
            print("Will calculate the mass in t")
            output = unit_converter_page.convert_lb_to_t("689")
            print("Calculated the mass - will confirm it's 0.31253 t")
            assert output == "0.31253", f"Expected 0.31253 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformLbToTConversion1")
            raise

def test_perform_lb_to_t_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform LbToT Conversion2"):
        try:
            print("Will calculate the mass in t")
            output = unit_converter_page.convert_lb_to_t("3620")
            print("Calculated the mass - will confirm it's 1.642 t")
            assert output == "1.642", f"Expected 1.642 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformLbToTConversion2")
            raise

def test_perform_mg_to_kg_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform MgToKg Conversion1"):
        try:
            print("Will calculate the mass in kg")
            output = unit_converter_page.convert_mg_to_kg("1000000")
            print("Calculated the mass - will confirm it's 1 kg")
            assert output == "1", f"Expected 1 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformMgToKgConversion1")
            raise

def test_perform_mg_to_kg_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform MgToKg Conversion2"):
        try:
            print("Will calculate the mass in kg")
            output = unit_converter_page.convert_mg_to_kg("9725000")
            print("Calculated the mass - will confirm it's 9.725 kg")
            assert output == "9.725", f"Expected 9.725 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformMgToKgConversion2")
            raise

def test_perform_mg_to_lb_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform MgToLb Conversion1"):
        try:
            print("Will calculate the mass in lb")
            output = unit_converter_page.convert_mg_to_lb("916247")
            print("Calculated the mass - will confirm it's 2.019979 lb")
            assert output == "2.019979", f"Expected 2.019979 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformMgToLbConversion1")
            raise

def test_perform_mg_to_lb_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform MgToLb Conversion2"):
        try:
            print("Will calculate the mass in lb")
            output = unit_converter_page.convert_mg_to_lb("250000")
            print("Calculated the mass - will confirm it's 0.55116 lb")
            assert output == "0.55116", f"Expected 0.55116 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformMgToLbConversion2")
            raise

def test_perform_mg_to_g_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform MgToG Conversion1"):
        try:
            print("Will calculate the mass in g")
            output = unit_converter_page.convert_mg_to_g("10000")
            print("Calculated the mass - will confirm it's 10 g")
            assert output == "10", f"Expected 10 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformMgToGConversion1")
            raise

def test_perform_mg_to_g_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform MgToG Conversion2"):
        try:
            print("Will calculate the mass in g")
            output = unit_converter_page.convert_mg_to_g("123")
            print("Calculated the mass - will confirm it's 0.123 g")
            assert output == "0.123", f"Expected 0.123 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformMgToGConversion2")
            raise

def test_perform_mg_to_oz_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform MgToOz Conversion1"):
        try:
            print("Will calculate the mass in oz")
            output = unit_converter_page.convert_mg_to_oz("672143")
            print("Calculated the mass - will confirm it's 23.70917 oz")
            assert output == "23.70917", f"Expected 23.70917 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformMgToOzConversion1")
            raise

def test_perform_mg_to_oz_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform MgToOz Conversion2"):
        try:
            print("Will calculate the mass in oz")
            output = unit_converter_page.convert_mg_to_oz("5555")
            print("Calculated the mass - will confirm it's 0.19595 oz")
            assert output == "0.19595", f"Expected 0.19595 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformMgToOzConversion2")
            raise

def test_perform_mg_to_t_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform MgToT Conversion1"):
        try:
            print("Will calculate the mass in t")
            output = unit_converter_page.convert_mg_to_t("975000000")
            print("Calculated the mass - will confirm it's 0.975 t")
            assert output == "0.975", f"Expected 0.975 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformMgToTConversion1")
            raise

def test_perform_mg_to_t_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform MgToT Conversion2"):
        try:
            print("Will calculate the mass in t")
            output = unit_converter_page.convert_mg_to_t("350000")
            print("Calculated the mass - will confirm it's 0.00035 t")
            assert output == "0.00035", f"Expected 0.00035 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformMgToTConversion2")
            raise

def test_perform_g_to_kg_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform GToKg Conversion1"):
        try:
            print("Will calculate the mass in kg")
            output = unit_converter_page.convert_g_to_kg("1000")
            print("Calculated the mass - will confirm it's 1 kg")
            assert output == "1", f"Expected 1 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformGToKgConversion1")
            raise

def test_perform_g_to_kg_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform GToKg Conversion2"):
        try:
            print("Will calculate the mass in kg")
            output = unit_converter_page.convert_g_to_kg("650250")
            print("Calculated the mass - will confirm it's 650.25 kg")
            assert output == "650.25", f"Expected 650.25 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformGToKgConversion2")
            raise

def test_perform_g_to_lb_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform GToLb Conversion1"):
        try:
            print("Will calculate the mass in lb")
            output = unit_converter_page.convert_g_to_lb("940")
            print("Calculated the mass - will confirm it's 2.072345 lb")
            assert output == "2.072345", f"Expected 2.072345 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformGToLbConversion1")
            raise

def test_perform_g_to_lb_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform GToLb Conversion2"):
        try:
            print("Will calculate the mass in lb")
            output = unit_converter_page.convert_g_to_lb("38100.55")
            print("Calculated the mass - will confirm it's 83.99733 lb")
            assert output == "83.99733", f"Expected 83.99733 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformGToLbConversion2")
            raise

def test_perform_g_to_mg_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform GToMg Conversion1"):
        try:
            print("Will calculate the mass in mg")
            output = unit_converter_page.convert_g_to_mg("970295")
            print("Calculated the mass - will confirm it's 970,295,000 mg")
            assert output == "970,295,000", f"Expected 970,295,000 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformGToMgConversion1")
            raise

def test_perform_g_to_mg_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform GToMg Conversion2"):
        try:
            print("Will calculate the mass in mg")
            output = unit_converter_page.convert_g_to_mg("0.33")
            print("Calculated the mass - will confirm it's 330 mg")
            assert output == "330", f"Expected 330 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformGToMgConversion2")
            raise

def test_perform_g_to_oz_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform GToOz Conversion1"):
        try:
            print("Will calculate the mass in oz")
            output = unit_converter_page.convert_g_to_oz("742")
            print("Calculated the mass - will confirm it's 26.17331 oz")
            assert output == "26.17331", f"Expected 26.17331 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformGToOzConversion1")
            raise

def test_perform_g_to_oz_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform GToOz Conversion2"):
        try:
            print("Will calculate the mass in oz")
            output = unit_converter_page.convert_g_to_oz("0.25")
            print("Calculated the mass - will confirm it's 0.0088185 oz")
            assert output == "0.0088185", f"Expected 0.0088185 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformGToOzConversion2")
            raise

def test_perform_g_to_t_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform GToT Conversion1"):
        try:
            print("Will calculate the mass in t")
            output = unit_converter_page.convert_g_to_t("35000000")
            print("Calculated the mass - will confirm it's 35 t")
            assert output == "35", f"Expected 35 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformGToOzConversion1")
            raise

def test_perform_g_to_t_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform GToT Conversion2"):
        try:
            print("Will calculate the mass in t")
            output = unit_converter_page.convert_g_to_t("275000")
            print("Calculated the mass - will confirm it's 0.275 t")
            assert output == "0.275", f"Expected 0.275 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformGToOzConversion2")
            raise

def test_perform_oz_to_kg_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform OzToKg Conversion1"):
        try:
            print("Will calculate the mass in kg")
            output = unit_converter_page.convert_oz_to_kg("3625")
            print("Calculated the mass - will confirm it's 102.76691 kg")
            assert output == "102.76691", f"Expected 102.76691 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformOzToKgConversion1")
            raise

def test_perform_oz_to_kg_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform OzToKg Conversion2"):
        try:
            print("Will calculate the mass in kg")
            output = unit_converter_page.convert_oz_to_kg("490")
            print("Calculated the mass - will confirm it's 13.89125 kg")
            assert output == "13.89125", f"Expected 13.89125 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformOzToKgConversion2")
            raise

def test_perform_oz_to_lb_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform OzToLb Conversion1"):
        try:
            print("Will calculate the mass in lb")
            output = unit_converter_page.convert_oz_to_lb("905")
            print("Calculated the mass - will confirm it's 56.56244 lb")
            assert output == "56.56244", f"Expected 56.56244 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformOzToLbConversion1")
            raise

def test_perform_oz_to_lb_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform OzToLb Conversion2"):
        try:
            print("Will calculate the mass in lb")
            output = unit_converter_page.convert_oz_to_lb("3891.33")
            print("Calculated the mass - will confirm it's 243.20786 lb")
            assert output == "243.20786", f"Expected 243.20786 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformOzToLbConversion2")
            raise

def test_perform_oz_to_mg_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform OzToMg Conversion1"):
        try:
            print("Will calculate the mass in mg")
            output = unit_converter_page.convert_oz_to_mg("0.55")
            print("Calculated the mass - will confirm it's 15,592.2209 mg")
            assert output == "15,592.2209", f"Expected 15,592.2209 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformOzToMgConversion1")
            raise

def test_perform_oz_to_mg_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform OzToMg Conversion2"):
        try:
            print("Will calculate the mass in mg")
            output = unit_converter_page.convert_oz_to_mg("0.0095")
            print("Calculated the mass - will confirm it's 269.32018 mg")
            assert output == "269.32018", f"Expected 269.32018 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformOzToMgConversion2")
            raise

def test_perform_oz_to_g_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform OzToG Conversion1"):
        try:
            print("Will calculate the mass in g")
            output = unit_converter_page.convert_oz_to_g("1000")
            print("Calculated the mass - will confirm it's 28,349.49254 g")
            assert output == "28,349.49254", f"Expected 28,349.49254 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformOzToGConversion1")
            raise

def test_perform_oz_to_g_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform OzToG Conversion2"):
        try:
            print("Will calculate the mass in g")
            output = unit_converter_page.convert_oz_to_g("0.8")
            print("Calculated the mass - will confirm it's 22.67959 g")
            assert output == "22.67959", f"Expected 22.67959 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformOzToGConversion2")
            raise

def test_perform_oz_to_t_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform OzToT Conversion1"):
        try:
            print("Will calculate the mass in t")
            output = unit_converter_page.convert_oz_to_t("1000000")
            print("Calculated the mass - will confirm it's 28.34949 t")
            assert output == "28.34949", f"Expected 28.34949 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformOzToTConversion1")
            raise

def test_perform_oz_to_t_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform OzToT Conversion2"):
        try:
            print("Will calculate the mass in t")
            output = unit_converter_page.convert_oz_to_t("25000")
            print("Calculated the mass - will confirm it's 0.70874 t")
            assert output == "0.70874", f"Expected 0.70874 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformOzToTConversion2")
            raise

def test_perform_t_to_kg_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform TToKg Conversion1"):
        try:
            print("Will calculate the mass in kg")
            output = unit_converter_page.convert_t_to_kg("1.5")
            print("Calculated the mass - will confirm it's 1,500 kg")
            assert output == "1,500", f"Expected 1,500 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformTToKgConversion1")
            raise

def test_perform_t_to_kg_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform TToKg Conversion2"):
        try:
            print("Will calculate the mass in kg")
            output = unit_converter_page.convert_t_to_kg("0.65")
            print("Calculated the mass - will confirm it's 650 kg")
            assert output == "650", f"Expected 650 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformTToKgConversion2")
            raise

def test_perform_t_to_lb_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform TToLb Conversion1"):
        try:
            print("Will calculate the mass in lb")
            output = unit_converter_page.convert_t_to_lb("0.03")
            print("Calculated the mass - will confirm it's 66.13868 lb")
            assert output == "66.13868", f"Expected 66.13868 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformTToLbConversion1")
            raise

def test_perform_t_to_lb_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform TToLb Conversion2"):
        try:
            print("Will calculate the mass in lb")
            output = unit_converter_page.convert_t_to_lb("22.8")
            print("Calculated the mass - will confirm it's 50,265.39578 lb")
            assert output == "50,265.39578", f"Expected 50,265.39578 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformTToLbConversion2")
            raise

def test_perform_t_to_mg_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform TToMg Conversion1"):
        try:
            print("Will calculate the mass in mg")
            output = unit_converter_page.convert_t_to_mg("0.009")
            print("Calculated the mass - will confirm it's 9,000,000 mg")
            assert output == "9,000,000", f"Expected 9,000,000 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformTToMgConversion1")
            raise

def test_perform_t_to_mg_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform TToMg Conversion2"):
        try:
            print("Will calculate the mass in mg")
            output = unit_converter_page.convert_t_to_mg("0.00065")
            print("Calculated the mass - will confirm it's 650,000 mg")
            assert output == "650,000", f"Expected 650,000 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformTToMgConversion2")
            raise

def test_perform_t_to_g_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform TToG Conversion1"):
        try:
            print("Will calculate the mass in g")
            output = unit_converter_page.convert_t_to_g("0.289")
            print("Calculated the mass - will confirm it's 289,000 g")
            assert output == "289,000", f"Expected 289,000 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformTToGConversion1")
            raise

def test_perform_t_to_g_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform TToG Conversion2"):
        try:
            print("Will calculate the mass in g")
            output = unit_converter_page.convert_t_to_g("6.4")
            print("Calculated the mass - will confirm it's 6,400,000 g")
            assert output == "6,400,000", f"Expected 6,400,000 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformTToGConversion2")
            raise

def test_perform_t_to_oz_conversion1(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform TToOz Conversion1"):
        try:
            print("Will calculate the mass in oz")
            output = unit_converter_page.convert_t_to_oz("50")
            print("Calculated the mass - will confirm it's 1,763,700 oz")
            assert output == "1,763,700", f"Expected 1,763,700 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformTToOzConversion1")
            raise

def test_perform_t_to_oz_conversion2(driver):
    unit_converter_page = UnitConverterPage(driver)

    with appium_transaction("Perform TToOz Conversion2"):
        try:
            print("Will calculate the mass in oz")
            output = unit_converter_page.convert_t_to_oz("0.115")
            print("Calculated the mass - will confirm it's 4,056.51 oz")
            assert output == "4,056.51", f"Expected 4,056.51 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformTToOzConversion2")
            raise