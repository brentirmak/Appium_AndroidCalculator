from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class BasicCalculatorPage(BasePage):

    HOME_ICON_BASIC_CALC = (AppiumBy.XPATH, '//android.widget.TextView[@text="Basic Calculator"]')
    HEADER = (AppiumBy.XPATH, '//android.widget.TextView[@text="Basic Calculator"]')

    DELETE_IMG = (
        AppiumBy.XPATH,
        '//android.widget.ImageView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_delete"]'
    )
    CLEAR_BTN = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_clear"]'
    )

    NUM9 = (AppiumBy.ID, 'calculator.currencyconverter.tipcalculator.unitconverter:id/btn_num9')
    PLUS = (AppiumBy.ID, 'calculator.currencyconverter.tipcalculator.unitconverter:id/btn_plus')
    RESULT_BTN = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_result"]'
    )
    OUTPUT = (AppiumBy.ID, 'calculator.currencyconverter.tipcalculator.unitconverter:id/tvResult')

    def open_from_home(self):
        print("Will click on the Basic Calculator option")
        self.click(self.HOME_ICON_BASIC_CALC)
        assert self.verify_loaded(), "Basic Calculator did not load after clicking"
        print("Basic Calculator option has been clicked")

    def verify_loaded(self):
        print("Will verify that the Basic Calculator header has loaded")
        return self.visible(self.HEADER)

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

