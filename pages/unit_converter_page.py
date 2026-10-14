from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class UnitConverterPage(BasePage):

    UNIT_CONVERTER_HEADER = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Unit Converter")')
    HOME_ICON_UNIT_CONVERTER = (AppiumBy.XPATH, '//android.widget.TextView[@text="Unit Converter"]')

    NUM0 = (AppiumBy.XPATH,'//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_num_0"]')
    NUM1 = (AppiumBy.XPATH,'//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_num_1"]')
    NUM2 = (AppiumBy.XPATH,'//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_num_2"]')
    NUM3 = (AppiumBy.XPATH,'//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_num_3"]')
    NUM4 = (AppiumBy.XPATH,'//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_num_4"]')
    NUM5 = (AppiumBy.XPATH,'//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_num_5"]')
    NUM6 = (AppiumBy.XPATH,'//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_num_6"]')
    NUM7 = (AppiumBy.XPATH,'//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_num_7"]')
    NUM8 = (AppiumBy.XPATH,'//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_num_8"]')
    NUM9 = (AppiumBy.XPATH,'//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_num_9"]')
    PERIOD = (AppiumBy.XPATH,'//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_point"]')
    CLR_BUTTON = (AppiumBy.XPATH,'//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_ac"]')
    CAL_BUTTON = (AppiumBy.XPATH,'//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_cal"]')
    XCHANGE_BUTTON = (AppiumBy.XPATH,'//android.widget.ImageView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_exchange"]')
    DELETE_IMG = (AppiumBy.XPATH,'//android.widget.ImageView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_delete"]')
    CLEAR_BTN = (AppiumBy.XPATH,'//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_clear"]')


    #RESULT1 = (AppiumBy.XPATH, '//android.widget.EditText[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/et_value" and @text="4.3307"]')
    #RESULT1 = (AppiumBy.XPATH,'//android.widget.EditText[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/et_value"][2]')
    RESULT1 = (AppiumBy.XPATH,'(//android.widget.EditText[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/et_value"])[2]',)
    #RESULT1 = (AppiumBy.XPATH,'//android.widget.EditText[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/et_value" and @text="157.48"]')

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
        print("Will click on the Unit Converter option")
        self.click(self.HOME_ICON_UNIT_CONVERTER)
        assert self.verify_loaded(), "Unit Converter did not load after clicking"
        print("Unit Converter option has been clicked")

    def verify_loaded(self):
        print("Will verify Loan Calculator header is displayed")
        page_title = self.find(self.UNIT_CONVERTER_HEADER).text
        print("Page title: ", page_title)
        return self.exists(self.UNIT_CONVERTER_HEADER), page_title

    def convert_cm_inches(self, number1):
        print("Will convert cm to inches")
        if self.exists(self.DELETE_IMG):
            print("Clearing previous input")
            self.click(self.CLEAR_BTN)

        print(f"Clicked on the Clear button - will enter {number1}")
        self.enter_number(number1)
        print(f"Entered {number1} - will check the inches value")

        result_element = self.find(self.RESULT1)
        return result_element.text


