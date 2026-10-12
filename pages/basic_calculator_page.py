from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

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
    PLUS = (AppiumBy.ID, 'calculator.currencyconverter.tipcalculator.unitconverter:id/btn_plus')
    MINUS = (AppiumBy.ID, 'calculator.currencyconverter.tipcalculator.unitconverter:id/btn_reduce')
    DELETE_IMG = (AppiumBy.XPATH,'//android.widget.ImageView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_delete"]')
    CLEAR_BTN = (AppiumBy.XPATH,'//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_clear"]')
    RESULT_BTN = (AppiumBy.XPATH,'//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_result"]')
    OUTPUT = (AppiumBy.ID, 'calculator.currencyconverter.tipcalculator.unitconverter:id/tvResult')

    def enter_number(self, number):
        digits = {
            "0": self.NUM0, "1": self.NUM1, "2": self.NUM2,
            "3": self.NUM3, "4": self.NUM4, "5": self.NUM5,
            "6": self.NUM6, "7": self.NUM7, "8": self.NUM8,
            "9": self.NUM9,
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

    def calculate_9_plus_9(self):
        print("Preparing calculator")

        if self.exists(self.DELETE_IMG):
            print("Clearing previous input")
            self.click(self.CLEAR_BTN)

        print("Clicked on the Clear button - will click on the '9' button")
        self.click(self.NUM9)
        print("Clicked on the '9' button - will click on the '+' button")
        self.click(self.PLUS)
        print("Clicked on the '+' button - will click on the '9' button")
        self.click(self.NUM9)
        print("Clicked on '9' button - will click on the '=' button")
        self.click(self.RESULT_BTN)
        print("Clicked on the '=' button - will return the result")

        return self.find(self.OUTPUT).text

