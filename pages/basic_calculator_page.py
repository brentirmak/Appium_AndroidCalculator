from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
import time

class BasicCalculatorPage(BasePage):

    HOME_ICON_BASIC_CALC = (AppiumBy.XPATH, '//android.widget.TextView[@text="Basic Calculator"]')
    HEADER = (AppiumBy.XPATH, '//android.widget.TextView[@text="Basic Calculator"]')
    NUM0 = (AppiumBy.XPATH,'//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_num0"]')
    NUM1 = (AppiumBy.XPATH,'//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_num1"]')
    NUM2 = (AppiumBy.XPATH,'//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_num2"]')
    NUM3 = (AppiumBy.XPATH,'//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_num3"]')
    NUM4 = (AppiumBy.XPATH,'//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_num4"]')
    NUM5 = (AppiumBy.XPATH,'//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_num5"]')
    NUM6 = (AppiumBy.XPATH,'//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_num6"]')
    NUM7 = (AppiumBy.XPATH,'//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_num7"]')
    NUM8 = (AppiumBy.XPATH,'//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_num8"]')
    NUM9 = (AppiumBy.XPATH,'//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_num9"]')
    PERIOD = (AppiumBy.XPATH,'//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_point"]')
    PARENTHESES = (AppiumBy.XPATH,'//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_parentheses"]')
    PLUS = (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_plus"]')
    MINUS = (AppiumBy.XPATH, '//android.view.ViewGroup[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_reduce"]')
    DIV = (AppiumBy.XPATH,'//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_div"]')
    MULTIPLY = (AppiumBy.XPATH,'//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_mul"]')
    DELETE_IMG = (AppiumBy.XPATH,'//android.widget.ImageView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_delete"]')
    CLEAR_BTN = (AppiumBy.XPATH,'//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_clear"]')
    RESULT_BTN = (AppiumBy.XPATH,'//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_result"]')
    OUTPUT = (AppiumBy.ID, 'calculator.currencyconverter.tipcalculator.unitconverter:id/tvResult')

    TYPE_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/tvKeyboardType")')
    RAD_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/btn_rad")')
    SIN_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/btnSci21")')
    COS_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/btnSci22")')
    TAN_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/btnSci23")')
    LOG_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/btnSci14")')
    POWER_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/btnSci34")')
    SQUARE_ROOT_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/btnSci33")')

    def enter_number(self, number):
        digits = {
            "0": self.NUM0, "1": self.NUM1, "2": self.NUM2,
            "3": self.NUM3, "4": self.NUM4, "5": self.NUM5,
            "6": self.NUM6, "7": self.NUM7, "8": self.NUM8,
            "9": self.NUM9, ".": self.PERIOD,
        }
        for digit in str(number):
            print(f"Will click on '{digit}'")
            self.click(digits[digit])
            print(f"Clicked on '{digit}'")

    def open_from_home(self):
        print("Will click on the Basic Calculator option")
        self.click(self.HOME_ICON_BASIC_CALC)
        assert self.verify_loaded(), "Basic Calculator did not load after clicking"
        print("Basic Calculator option has been clicked")

    def verify_loaded(self):
        print("Will verify BMI Calculator header is displayed")
        page_title = self.find(self.HEADER).text
        print("Page title: ", page_title)
        return self.exists(self.HEADER), page_title

    def clear_input(self):
        print("Will clear the screen - to accept fresh input")
        self.click(self.CLEAR_BTN)
        print("Clicked on the Clear button")

    def select_calculator_type(self, calculator_type):
        print("Will select the Calculator type/mode")
        calculator_type = self.find(self.TYPE_BUTTON).text
        print("The current type is set to ", calculator_type)

        if calculator_type == "Scientific":
            print("The calculator is already set to Scientific")
        else:
            self.click(self.TYPE_BUTTON)
            print("Clicked on the Type button to set to Scientific")

        print("Will now clear the screen - to accept fresh input")
        self.click(self.CLEAR_BTN)
        print("Clicked on the Clear button")

    def select_calculator_radians(self, radians_flag):
        print("Will select the Calculator degrees vs radians mode")
        calculator_radians_mode = self.find(self.RAD_BUTTON).text
        print("The current type is set to ", calculator_radians_mode)

        if calculator_radians_mode == "Deg" and radians_flag == False:
            print("The calculator is already set to Degrees and radians flag is set to False")
            print("No action to be taken")
        elif calculator_radians_mode == "Deg" and radians_flag == True:
            print("Calculator is set to Degrees and radians flag is set to True")
            print("Will click on the Radians button - will click button to toggle to Radians")
            self.click(self.RAD_BUTTON)
            print("Clicked on the Radians button")
        elif calculator_radians_mode == "Rad" and radians_flag == False:
            print("Calculator is set to Radians and radians flag is set to False")
            print("Will click on the Radians button - will click button to toggle to Degrees")
            self.click(self.RAD_BUTTON)
            print("Clicked on the Radians button")
        elif calculator_radians_mode == "Rad" and radians_flag == True:
            print("The calculator is already set to Radians and radians flag is set to True")
            print("No action to be taken")

    def calculate_addition(self, number1, number2):
        print(f"Will calculate the addition of two numbers ", number1, " and ", number2)
        if self.exists(self.DELETE_IMG):
            print("Clearing previous input")
            self.click(self.CLEAR_BTN)
        print(f"Clicked on the Clear button - will enter {number1}")
        self.enter_number(number1)
        print(f"Entered {number1} - will click on the '+' button")
        self.click(self.PLUS)
        print(f"Clicked on the '+' button - will enter {number2}")
        self.enter_number(number2)
        print(f"Entered {number2} - will click on the '=' button")
        self.click(self.RESULT_BTN)
        print("Clicked on the '=' button - will return the result")

        return self.find(self.OUTPUT).text

    def calculate_subtraction(self, number1, number2):
        print(f"Will calculate the subtraction of two numbers ", number1, " and ", number2)
        if self.exists(self.DELETE_IMG):
            print("Clearing previous input")
            self.click(self.CLEAR_BTN)
        print(f"Clicked on the Clear button - will enter {number1}")
        self.enter_number(number1)
        print(f"Entered {number1} - will click on the '-' button")
        self.click(self.MINUS)
        print(f"Clicked on the '-' button - will enter {number2}")
        self.enter_number(number2)
        print(f"Entered {number2} - will click on the '=' button")
        self.click(self.RESULT_BTN)
        print("Clicked on the '=' button - will return the result")

        return self.find(self.OUTPUT).text

    def calculate_division(self, number1, number2):
        print(f"Will calculate the division of two numbers ", number1, " and ", number2)
        if self.exists(self.DELETE_IMG):
            print("Clearing previous input")
            self.click(self.CLEAR_BTN)
        print(f"Clicked on the Clear button - will enter {number1}")
        self.enter_number(number1)
        print(f"Entered {number1} - will click on the '/' button")
        self.click(self.DIV)
        print(f"Clicked on the '/' button - will enter {number2}")
        self.enter_number(number2)
        print(f"Entered {number2} - will click on the '=' button")
        self.click(self.RESULT_BTN)
        print("Clicked on the '=' button - will return the result")

        return self.find(self.OUTPUT).text

    def calculate_multiplication(self, number1, number2):
        print(f"Will calculate the modulo of two numbers ", number1, " and ", number2)
        if self.exists(self.DELETE_IMG):
            print("Clearing previous input")
            self.click(self.CLEAR_BTN)
        print(f"Clicked on the Clear button - will enter {number1}")
        self.enter_number(number1)
        print(f"Entered {number1} - will click on the 'x' button")
        self.click(self.MULTIPLY)
        print(f"Clicked on the '%' button - will enter {number2}")
        self.enter_number(number2)
        print(f"Entered {number2} - will click on the '=' button")
        self.click(self.RESULT_BTN)
        print("Clicked on the '=' button - will return the result")

        return self.find(self.OUTPUT).text

    def calculate_sin(self, number1, mode):
        print(f"Will calculate the sin of ", number1)
        if self.exists(self.DELETE_IMG):
            print("Clearing previous input")
            self.click(self.CLEAR_BTN)
        if mode == 'radians':
            print("Ensuring that the Radians button is selected")
            self.select_calculator_radians(True)
            print("Radians button is selected")
        else:
            print("Ensuring that the Degrees button is selected")
            self.select_calculator_radians(False)
            print("Degrees button is selected")
        print("Will click on the 'sin' button")
        self.click(self.SIN_BUTTON)
        print(f"Clicked on the Sin button - will enter {number1}")
        self.enter_number(number1)
        print(f"Entered {number1} - will close parenthesis")
        self.click(self.PARENTHESES)
        print("Closed parenthesis - will click on result button")
        self.click(self.RESULT_BTN)
        print("Clicked on the '=' button - will return the result")

        return self.find(self.OUTPUT).text

    def calculate_cos(self, number1, mode):
        print(f"Will calculate the sin of ", number1)
        if self.exists(self.DELETE_IMG):
            print("Clearing previous input")
            self.click(self.CLEAR_BTN)
        if mode == 'radians':
            print("Ensuring that the Radians button is selected")
            self.select_calculator_radians(True)
            print("Radians button is selected")
        else:
            print("Ensuring that the Degrees button is selected")
            self.select_calculator_radians(False)
            print("Degrees button is selected")
        print("Will click on the 'cos' button")
        self.click(self.COS_BUTTON)
        print(f"Clicked on the Cos button - will enter {number1}")
        self.enter_number(number1)
        print(f"Entered {number1} - will close parenthesis")
        self.click(self.PARENTHESES)
        print("Closed parenthesis - will click on result button")
        self.click(self.RESULT_BTN)
        print("Clicked on the '=' button - will return the result")

        return self.find(self.OUTPUT).text

    def calculate_tan(self, number1, mode):
        print(f"Will calculate the sin of ", number1)
        if self.exists(self.DELETE_IMG):
            print("Clearing previous input")
            self.click(self.CLEAR_BTN)
        if mode == 'radians':
            print("Ensuring that the Radians button is selected")
            self.select_calculator_radians(True)
            print("Radians button is selected")
        else:
            print("Ensuring that the Degrees button is selected")
            self.select_calculator_radians(False)
            print("Degrees button is selected")
        print("Will click on the 'cos' button")
        self.click(self.TAN_BUTTON)
        print(f"Clicked on the Cos button - will enter {number1}")
        self.enter_number(number1)
        print(f"Entered {number1} - will close parenthesis")
        self.click(self.PARENTHESES)
        print("Closed parenthesis - will click on result button")
        self.click(self.RESULT_BTN)
        print("Clicked on the '=' button - will return the result")

        return self.find(self.OUTPUT).text

    def calculate_log(self, number1):
        print(f"Will calculate the log of ", number1)
        if self.exists(self.DELETE_IMG):
            print("Clearing previous input")
            self.click(self.CLEAR_BTN)
        print("Will click on the 'log' button")
        self.click(self.LOG_BUTTON)
        print(f"Clicked on the log button - will enter {number1}")
        self.enter_number(number1)
        print(f"Entered {number1} - will close parenthesis")
        self.click(self.PARENTHESES)
        print("Closed parenthesis - will click on result button")
        self.click(self.RESULT_BTN)
        print("Clicked on the '=' button - will return the result")

        return self.find(self.OUTPUT).text

    def calculate_power(self, number1, number2):
        print(f"Will calculate ", number1, " to the power of ", number2)
        if self.exists(self.DELETE_IMG):
            print("Clearing previous input")
            self.click(self.CLEAR_BTN)
        print(f"Clicked on the Clear button - will enter {number1}")
        self.enter_number(number1)
        print(f"Entered {number1} - will click on the '^' button")
        self.click(self.POWER_BUTTON)
        print(f"Clicked on the '^' button - will enter {number2}")
        self.enter_number(number2)
        print(f"Entered {number2} - will close the parenthesis")
        self.click(self.PARENTHESES)
        print("Closed parenthesis - will click on result button")
        self.click(self.RESULT_BTN)
        print("Clicked on the '=' button - will return the result")

        return self.find(self.OUTPUT).text

    def calculate_square_root(self, number1):
        print(f"Will calculate the log of ", number1)
        if self.exists(self.DELETE_IMG):
            print("Clearing previous input")
            self.click(self.CLEAR_BTN)
        print("Will click on the 'square root' button")
        self.click(self.SQUARE_ROOT_BUTTON)
        print(f"Clicked on the log button - will enter {number1}")
        self.enter_number(number1)
        print(f"Entered {number1} - will close parenthesis")
        self.click(self.PARENTHESES)
        print("Closed parenthesis - will click on result button")
        self.click(self.RESULT_BTN)
        print("Clicked on the '=' button - will return the result")

        return self.find(self.OUTPUT).text