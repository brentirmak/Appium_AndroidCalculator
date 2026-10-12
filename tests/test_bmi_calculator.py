import pytest
import time
from pages.side_menu_page import SideMenuPage
from pages.home_page import HomePage
from pages.bmi_calculator_page import BMICalculatorPage
from utils.helpers import appium_transaction, capture_error_snapshot

@pytest.mark.timeout(300)
def test_access_bmi_calculator(driver):
    side_menu = SideMenuPage(driver)
    bmi_calculator_page = BMICalculatorPage(driver)
    home = HomePage(driver)

    with appium_transaction("Access BMI Calculator"):
        print("Checking to see if we're at Home screen")
        if not home.load_landing_page():
            print("Not at Home screen")
        try:
            print("Will click on the side menu item for BMI Calculator")
            side_menu.click_bmi_calculator()
            is_displayed, page_title = bmi_calculator_page.verify_loaded()

            assert is_displayed, "BMI Calculator header is not displayed"
            assert page_title == "BMI Calculator", f"Expected page title 'BMI Calculator' but found '{page_title}'"
        except Exception:
            capture_error_snapshot(driver, "Access BMI Calculator")
            raise

@pytest.mark.timeout(175)
def test_perform_bmi_calculation1(driver):
    bmi_calculator = BMICalculatorPage(driver)

    with appium_transaction("Perform BMI Calculation1"):
        try:
            bmi_calculator.enter_weight_in_kg(125)
            bmi_calculator.enter_height_in_cm(190)
            bmi_calculator.enter_age(38)
            bmi_calculator.select_gender("Male")
            bmi_value, bmi_category_value = bmi_calculator.click_calculate_button()
            assert ("34.63" in bmi_value) or ("34.63" in bmi_value), f"Expected 34.63 but got {bmi_value}"
            assert ("Obese Class I" in bmi_category_value) or ("Obese Class I" in bmi_category_value), f"Expected Obese Class I but got {bmi_category_value}"
        except Exception:
            capture_error_snapshot(driver, "PerformBMICalculation1")
            raise

@pytest.mark.timeout(175)
def test_perform_bmi_calculation2(driver):
    bmi_calculator = BMICalculatorPage(driver)

    with appium_transaction("Perform BMI Calculation2"):
        try:
            bmi_calculator.click_back_button()
            bmi_calculator.enter_weight_in_kg(54)
            bmi_calculator.enter_height_in_cm(167)
            bmi_calculator.enter_age(21)
            bmi_calculator.select_gender("Female")
            bmi_value, bmi_category_value = bmi_calculator.click_calculate_button()
            assert ("19.36" in bmi_value) or ("19.36" in bmi_value), f"Expected 19.36 but got {bmi_value}"
            assert ("Normal" in bmi_category_value) or ("Normal" in bmi_category_value), f"Expected Normal but got {bmi_category_value}"

        except Exception:
            capture_error_snapshot(driver, "PerformBMICalculation2")
            raise

@pytest.mark.timeout(175)
def test_perform_bmi_calculation3(driver):
    bmi_calculator = BMICalculatorPage(driver)

    with appium_transaction("Perform BMI Calculation3"):
        try:
            bmi_calculator.click_back_button()
            bmi_calculator.enter_weight_in_kg(91)
            bmi_calculator.enter_height_in_cm(157)
            bmi_calculator.enter_age(23)
            bmi_calculator.select_gender("Female")
            bmi_value, bmi_category_value = bmi_calculator.click_calculate_button()
            assert ("36.92" in bmi_value) or ("36.92" in bmi_value), f"Expected 36.92 but got {bmi_value}"
            assert ("Obese Class II" in bmi_category_value) or ("Obese Class II" in bmi_category_value), f"Expected Obese Class II but got {bmi_category_value}"

        except Exception:
            capture_error_snapshot(driver, "PerformBMICalculation3")
            raise

    @pytest.mark.timeout(175)
    def test_perform_bmi_calculation4(driver):
        bmi_calculator = BMICalculatorPage(driver)

        with appium_transaction("Perform BMI Calculation4"):
            try:
                bmi_calculator.click_back_button()
                bmi_calculator.enter_weight_in_kg(65)
                bmi_calculator.enter_height_in_cm(195)
                bmi_calculator.enter_age(25)
                bmi_calculator.select_gender("Male")
                bmi_value, bmi_category_value = bmi_calculator.click_calculate_button()
                assert ("17.09" in bmi_value) or ("17.09" in bmi_value), f"Expected 17.09 but got {bmi_value}"
                assert ("Underweight" in bmi_category_value) or ("Underweight" in bmi_category_value), f"Expected Underweight but got {bmi_category_value}"

            except Exception:
                capture_error_snapshot(driver, "PerformBMICalculation4")
                raise