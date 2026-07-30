from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class UnitConverterPage(BasePage):

    UNIT_CONVERTER_HEADER = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Unit Converter")')
    HOME_ICON_UNIT_CONVERTER = (AppiumBy.XPATH, '//android.widget.TextView[@text="Unit Converter"]')
    NUM1 = (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_num_1"]')
    RESULT1 = (AppiumBy.XPATH, '//android.widget.EditText[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/et_value" and @text="4.3307"]')

    def open_from_home(self):
        print("Will click on the Unit Converter option")
        self.click(self.HOME_ICON_UNIT_CONVERTER)
        assert self.verify_loaded(), "Unit Converter did not load after clicking"
        print("Unit Converter option has been clicked")

    def verify_loaded(self):
        print("Will verify that the Unit Converter header has loaded")
        return self.visible(self.UNIT_CONVERTER_HEADER)

    def convert_cm_inches(self):
        print("Will convert cm to inches")

        print("Will click on the '1' button")
        self.click(self.NUM1)
        print("Clicked on the '1' button - will click on it again")
        self.click(self.NUM1)
        print("Clicked on the '1' button a 2nd time - will check the result")
        print(self.find(self.RESULT1).text)

        return self.find(self.RESULT1).text


