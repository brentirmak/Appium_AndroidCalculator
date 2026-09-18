from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class DateCalculatorPage(BasePage):
    #new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/tv_title")

    HOME_ICON_DATE_CALCULATOR = (AppiumBy.XPATH, '//android.widget.TextView[@text="Date Calculator"]')
    #DATE_HEADER = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Date Calculator")')
    DATE_CALCULATOR_HEADER = (AppiumBy.XPATH,'//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/tv_title"]')


    #NUM1 = (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_num_1"]')
    #RESULT1 = (AppiumBy.XPATH, '//android.widget.EditText[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/et_value" and @text="4.3307"]')

    def open_from_home(self):
        print("Will click on the Date Calculator option")
        self.click(self.HOME_ICON_DATE_CALCULATOR)
        assert self.verify_loaded(), "Date Calculator did not load after clicking"
        print("Date Calculator option has been clicked")

    def verify_loaded(self):
        print("Will verify that the Date Calculator header has loaded")
        header_text = self.find(self.DATE_CALCULATOR_HEADER).text
        if header_text == "Date":
            print("Date Calculator header loaded successfully")
            return True
        else:
            print("Failed to load Date Calculator header")
            return False

    '''
    def convert_cm_inches(self):
        print("Will convert cm to inches")

        print("Will click on the '1' button")
        self.click(self.NUM1)
        print("Clicked on the '1' button - will click on it again")
        self.click(self.NUM1)
        print("Clicked on the '1' button a 2nd time - will check the result")
        print(self.find(self.RESULT1).text)

        return self.find(self.RESULT1).text
    '''

