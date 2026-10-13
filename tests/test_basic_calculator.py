import pytest
from pages.home_page import HomePage
from pages.basic_calculator_page import BasicCalculatorPage
from utils.helpers import appium_transaction, capture_error_snapshot

@pytest.mark.timeout(300)
def test_access_basic_calculator(driver):
    home = HomePage(driver)
    calc = BasicCalculatorPage(driver)

    with appium_transaction("Access Basic Calculator"):
        if not home.load_landing_page():
            print("Not at Home screen")

        try:
            calc.open_from_home()
            is_displayed, page_title = calc.verify_loaded()

            assert is_displayed, "Basic Calculator header is not displayed"
            assert page_title == "Basic Calculator", f"Expected page title 'Basic Calculator' but found '{page_title}'"

        except Exception:
            capture_error_snapshot(driver, "AccessBasicCalculator")
            raise

@pytest.mark.timeout(175)
def test_perform_addition1(driver):
    calc = BasicCalculatorPage(driver)

    with appium_transaction("Perform Addition1"):
        try:
            if not calc.verify_loaded():
                calc.open_from_home()
            calc.clear_input()
            output = calc.calculate_addition(30,50)
            assert output == "= 80", f"Expected 80 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformAddition1")
            raise

@pytest.mark.timeout(175)
def test_perform_addition2(driver):
    calc = BasicCalculatorPage(driver)

    with appium_transaction("Perform Addition2"):
        try:
            if not calc.verify_loaded():
                calc.open_from_home()
            calc.clear_input()
            output = calc.calculate_addition(12345,6789)
            assert output == "= 19,134", f"Expected 19,134 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformAddition2")
            raise

@pytest.mark.timeout(175)
def test_perform_subtraction1(driver):
    calc = BasicCalculatorPage(driver)

    with appium_transaction("Perform Subtraction1"):
        try:
            if not calc.verify_loaded():
                calc.open_from_home()
            calc.clear_input()
            output = calc.calculate_subtraction(10,3)
            assert output == "= 7", f"Expected 7 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformSubtraction1")
            raise

@pytest.mark.timeout(175)
def test_perform_subtraction2(driver):
    calc = BasicCalculatorPage(driver)

    with appium_transaction("Perform Subtraction2"):
        try:
            if not calc.verify_loaded():
                calc.open_from_home()
            calc.clear_input()
            output = calc.calculate_subtraction(583,71)
            assert output == "= 512", f"Expected 512 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformSubtraction2")
            raise

@pytest.mark.timeout(175)
def test_perform_subtraction3(driver):
    calc = BasicCalculatorPage(driver)

    with appium_transaction("Perform Subtraction3"):
        try:
            if not calc.verify_loaded():
                calc.open_from_home()
            calc.clear_input()
            output = calc.calculate_subtraction(100,150)
            assert output == "= -50", f"Expected -50 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformSubtraction3")
            raise

@pytest.mark.timeout(175)
def test_perform_division1(driver):
    calc = BasicCalculatorPage(driver)

    with appium_transaction("Perform Division1"):
        try:
            if not calc.verify_loaded():
                calc.open_from_home()
            calc.clear_input()
            output = calc.calculate_division(75,25)
            assert output == "= 3", f"Expected 3 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformDivision1")
            raise

@pytest.mark.timeout(175)
def test_perform_division2(driver):
    calc = BasicCalculatorPage(driver)

    with appium_transaction("Perform Division2"):
        try:
            if not calc.verify_loaded():
                calc.open_from_home()
            calc.clear_input()
            output = calc.calculate_division(289,13)
            assert output == "= 22.23077", f"Expected 22.23077 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformDivision2")
            raise

@pytest.mark.timeout(175)
def test_perform_multiplication1(driver):
    calc = BasicCalculatorPage(driver)

    with appium_transaction("Perform Multiplication1"):
        try:
            if not calc.verify_loaded():
                calc.open_from_home()
            calc.clear_input()
            output = calc.calculate_multiplication(12500,20)
            assert output == "= 250,000", f"Expected 250,000 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformMultiplication1")
            raise

@pytest.mark.timeout(175)
def test_perform_multiplication2(driver):
    calc = BasicCalculatorPage(driver)

    with appium_transaction("Perform Multiplication2"):
        try:
            if not calc.verify_loaded():
                calc.open_from_home()
            calc.clear_input()
            output = calc.calculate_multiplication(12,2)
            assert output == "= 24", f"Expected 24 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformMultiplication2")
            raise

@pytest.mark.timeout(175)
def test_perform_multiplication3(driver):
    calc = BasicCalculatorPage(driver)

    with appium_transaction("Perform Multiplication3"):
        try:
            if not calc.verify_loaded():
                calc.open_from_home()
            calc.clear_input()
            output = calc.calculate_multiplication(2.5,2)
            assert output == "= 5", f"Expected 24 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformMultiplication3")
            raise

@pytest.mark.timeout(175)
def test_perform_sin_radians_calculation1(driver):
    calc = BasicCalculatorPage(driver)

    with appium_transaction("Perform Sin Radians Calculation1"):
        try:
            if not calc.verify_loaded():
                calc.open_from_home()
            calc.clear_input()
            calc.select_calculator_type('Scientific')
            output = calc.calculate_sin(5, 'radians')
            assert output == "= -0.95892", f"Expected -0.95892 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformSinRadiansCalculation1")
            raise

@pytest.mark.timeout(175)
def test_perform_sin_radians_calculation2(driver):
    calc = BasicCalculatorPage(driver)

    with appium_transaction("Perform Sin Radians Calculation2"):
        try:
            if not calc.verify_loaded():
                calc.open_from_home()
            calc.clear_input()
            calc.select_calculator_type('Scientific')
            output = calc.calculate_sin(0.5, 'radians')
            assert output == "= 0.47943", f"Expected 0.47943 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformSinRadiansCalculation2")
            raise

@pytest.mark.timeout(175)
def test_perform_sin_degrees_calculation1(driver):
    calc = BasicCalculatorPage(driver)

    with appium_transaction("Perform Sin Degrees Calculation1"):
        try:
            if not calc.verify_loaded():
                calc.open_from_home()
            calc.clear_input()
            calc.select_calculator_type('Scientific')
            output = calc.calculate_sin(37, 'degrees')
            assert output == "= 0.60182", f"Expected 0.60182 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformSinDegreesCalculation1")
            raise

@pytest.mark.timeout(175)
def test_perform_sin_degrees_calculation2(driver):
    calc = BasicCalculatorPage(driver)

    with appium_transaction("Perform Sin Degrees Calculation2"):
        try:
            if not calc.verify_loaded():
                calc.open_from_home()
            calc.clear_input()
            calc.select_calculator_type('Scientific')
            output = calc.calculate_sin(0.75, 'degrees')
            assert output == "= 0.01309", f"Expected 0.01309 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformSinDegreesCalculation2")
            raise

@pytest.mark.timeout(175)
def test_perform_cos_radians_calculation1(driver):
    calc = BasicCalculatorPage(driver)

    with appium_transaction("Perform Cos Radians Calculation1"):
        try:
            if not calc.verify_loaded():
                calc.open_from_home()
            calc.clear_input()
            calc.select_calculator_type('Scientific')
            output = calc.calculate_cos(10, 'radians')
            assert output == "= -0.83907", f"Expected -0.83907 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformCosRadiansCalculation1")
            raise

@pytest.mark.timeout(175)
def test_perform_cos_radians_calculation2(driver):
    calc = BasicCalculatorPage(driver)

    with appium_transaction("Perform Cos Radians Calculation2"):
        try:
            if not calc.verify_loaded():
                calc.open_from_home()
            calc.clear_input()
            calc.select_calculator_type('Scientific')
            output = calc.calculate_cos(0.0405, 'radians')
            assert output == "= 0.99918", f"Expected 0.99918 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformCosRadiansCalculation2")
            raise

@pytest.mark.timeout(175)
def test_perform_cos_degrees_calculation1(driver):
    calc = BasicCalculatorPage(driver)

    with appium_transaction("Perform Cos Degrees Calculation1"):
        try:
            if not calc.verify_loaded():
                calc.open_from_home()
            calc.clear_input()
            calc.select_calculator_type('Scientific')
            output = calc.calculate_cos(22, 'degrees')
            assert output == "= 0.92718", f"Expected 0.92718 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformCosDegreesCalculation1")
            raise

@pytest.mark.timeout(175)
def test_perform_cos_degrees_calculation2(driver):
    calc = BasicCalculatorPage(driver)

    with appium_transaction("Perform Cos Degrees Calculation2"):
        try:
            if not calc.verify_loaded():
                calc.open_from_home()
            calc.clear_input()
            calc.select_calculator_type('Scientific')
            output = calc.calculate_cos(987, 'degrees')
            assert output == "= -0.05234", f"Expected -0.05234 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformCosDegreesCalculation2")
            raise

@pytest.mark.timeout(175)
def test_perform_tan_radians_calculation1(driver):
    calc = BasicCalculatorPage(driver)

    with appium_transaction("Perform Tan Radians Calculation1"):
        try:
            if not calc.verify_loaded():
                calc.open_from_home()
            calc.clear_input()
            calc.select_calculator_type('Scientific')
            output = calc.calculate_tan(5555, 'radians')
            assert output == "= 0.78284", f"Expected 0.78284 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformTanRadiansCalculation1")
            raise

@pytest.mark.timeout(175)
def test_perform_tan_radians_calculation2(driver):
    calc = BasicCalculatorPage(driver)

    with appium_transaction("Perform Tan Radians Calculation2"):
        try:
            if not calc.verify_loaded():
                calc.open_from_home()
            calc.clear_input()
            calc.select_calculator_type('Scientific')
            output = calc.calculate_tan(0.33, 'radians')
            assert output == "= 0.34252", f"Expected 0.34252 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformTanRadiansCalculation2")
            raise

@pytest.mark.timeout(175)
def test_perform_tan_degrees_calculation1(driver):
    calc = BasicCalculatorPage(driver)

    with appium_transaction("Perform Tan Degrees Calculation1"):
        try:
            if not calc.verify_loaded():
                calc.open_from_home()
            calc.clear_input()
            calc.select_calculator_type('Scientific')
            output = calc.calculate_tan(250, 'degrees')
            assert output == "= 2.74748", f"Expected 2.74748 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformTanDegreesCalculation1")
            raise

@pytest.mark.timeout(175)
def test_perform_tan_degrees_calculation2(driver):
    calc = BasicCalculatorPage(driver)

    with appium_transaction("Perform Tan Degrees Calculation2"):
        try:
            if not calc.verify_loaded():
                calc.open_from_home()
            calc.clear_input()
            calc.select_calculator_type('Scientific')
            output = calc.calculate_tan(11, 'degrees')
            assert output == "= 0.19438", f"Expected 0.19438 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformTanDegreesCalculation2")
            raise

@pytest.mark.timeout(175)
def test_perform_log_calculation1(driver):
    calc = BasicCalculatorPage(driver)

    with appium_transaction("Perform Log Calculation1"):
        try:
            if not calc.verify_loaded():
                calc.open_from_home()
            calc.clear_input()
            output = calc.calculate_log(10)
            assert output == "= 1", f"Expected 1 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformLogCalculation1")
            raise

@pytest.mark.timeout(175)
def test_perform_log_calculation2(driver):
    calc = BasicCalculatorPage(driver)

    with appium_transaction("Perform Log Calculation2"):
        try:
            if not calc.verify_loaded():
                calc.open_from_home()
            calc.clear_input()
            output = calc.calculate_log(100)
            assert output == "= 2", f"Expected 2 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformLogCalculation2")
            raise

@pytest.mark.timeout(175)
def test_perform_power_calculation1(driver):
    calc = BasicCalculatorPage(driver)

    with appium_transaction("Perform Power Calculation1"):
        try:
            if not calc.verify_loaded():
                calc.open_from_home()
            calc.clear_input()
            output = calc.calculate_power(2,3)
            assert output == "= 8", f"Expected 8 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformPowerCalculation1")
            raise

@pytest.mark.timeout(175)
def test_perform_square_root_calculation1(driver):
    calc = BasicCalculatorPage(driver)

    with appium_transaction("Perform SquareRoot Calculation1"):
        try:
            if not calc.verify_loaded():
                calc.open_from_home()
            calc.clear_input()
            output = calc.calculate_square_root(360)
            assert output == "= 18.97367", f"Expected 18.97367 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformSquareRootCalculation1")
            raise

@pytest.mark.timeout(175)
def test_perform_square_cube_root_calculation1(driver):
    calc = BasicCalculatorPage(driver)

    with appium_transaction("Perform CubeRoot Calculation1"):
        try:
            if not calc.verify_loaded():
                calc.open_from_home()
            calc.clear_input()
            output = calc.calculate_cube_root(8)
            assert output == "= 2", f"Expected 2 but got {output}"
        except Exception:
            capture_error_snapshot(driver, "PerformCubeRootCalculation1")
            raise