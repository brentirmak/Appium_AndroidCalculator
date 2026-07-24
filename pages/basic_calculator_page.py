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
        self.click(self.HOME_ICON_BASIC_CALC)

    def verify_loaded(self):
        return self.exists(self.HEADER)

    def calculate_9_plus_9(self):
        self.find(self.DELETE_IMG)
        self.click(self.CLEAR_BTN)

        self.click(self.NUM9)
        self.click(self.PLUS)
        self.click(self.NUM9)
        self.click(self.RESULT_BTN)

        return self.find(self.OUTPUT).text

