from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class DateCalculatorPage(BasePage):
    HOME_ICON_DATE_CALCULATOR = (AppiumBy.XPATH, '//android.widget.TextView[@text="Date Calculator"]')
    DATE_CALCULATOR_HEADER = (AppiumBy.XPATH,'//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/tv_title"]')
    FROM_DATE_FIELD = (AppiumBy.ID,'calculator.currencyconverter.tipcalculator.unitconverter:id/btn_pick_start_date')
    DURATION_FIELD = (AppiumBy.ID,'calculator.currencyconverter.tipcalculator.unitconverter:id/et_duration')
    TO_DATE_FIELD = (AppiumBy.ID,'calculator.currencyconverter.tipcalculator.unitconverter:id/btn_pick_end_date')
    FROM_TO_POPUP_HEADER = (AppiumBy.ID,'calculator.currencyconverter.tipcalculator.unitconverter:id/tv_title')
    SAVE_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/btn_save")')
    FROM_TO_TAB = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("From/To")')
    FROM_LABEL = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/tv_from")')
    DURATION_PLUS_ICON = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/btn_duration_add")')
    DURATION_MINUS_ICON = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/btn_duration_subtract")')
    CLEAR_ICON = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/btn_ac")')
    BUTTON6_ICON = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/btn_num_6")')
    BUTTON0_ICON = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/btn_num_0")')
    OK_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/btn_ok")')
    RESULT_FIELD = (AppiumBy.ID, 'calculator.currencyconverter.tipcalculator.unitconverter:id/tv_result_date')

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

    def verify_fields(self):
        print("Will verify fields")
        self.find(self.FROM_DATE_FIELD)
        print("Verified FROM DATE field")
        self.find(self.DURATION_FIELD)
        print("Verified DURATION field")
        self.find(self.TO_DATE_FIELD)
        print("Verified TO DATE field")

        return True

    def calculate_date_difference(self):
        print("Will calculate the date difference")
        print("Setting from field (a month out) from today")
        self.click(self.FROM_DATE_FIELD)
        print("Will verify that the From Popup was displayed")
        self.find(self.FROM_TO_POPUP_HEADER)
        print("Verified the From Popup was displayed - for From field, will select a month out from today")
        self.select_a_month_out()
        print("Selected a month out - will click on Save button")
        self.click(self.SAVE_BUTTON)
        print("Clicked on the Save button - will now select the To field")
        self.click(self.TO_DATE_FIELD)
        print("Will verify that the To Popup was displayed")
        self.find(self.FROM_TO_POPUP_HEADER)
        print("Verified the From Popup was displayed - for To field, will select 2 months out from today")
        self.select_two_months_out()
        print("Selected 2 months out - will click on Save button")
        self.click(self.SAVE_BUTTON)
        duration_value = self.find(self.DURATION_FIELD).text
        print("Duration: ", duration_value)

        return duration_value

    def calculate_to_date(self):
        print("Will calculate the To date field")
        print("Will click on From/To tab")
        self.click(self.FROM_TO_TAB)
        print("Clicked on From/To tab - will verify the From label")
        self.find(self.FROM_LABEL)
        print("From label found - will click on the '+' icon")
        self.click(self.DURATION_PLUS_ICON)
        print("Clicked on the '+' icon - will click on the 'C' to clear")
        self.click(self.CLEAR_ICON)
        print("Clicked on the Clear icon - will now enter '60' in the Days field")
        self.click(self.BUTTON6_ICON)
        self.click(self.BUTTON0_ICON)
        print("Entered 60 in the Duration field - will click on OK button to calculate")
        self.click(self.OK_BUTTON)
        print("Clicked on the OK button")
        result = self.find(self.RESULT_FIELD).text
        print("Result: ", result)

        return result

    def select_a_month_out(self):
        self.driver.execute_script("mobile: clickGesture", {"x": 260, "y": 1885})

    def select_two_months_out(self):
        self.driver.execute_script("mobile: clickGesture", {"x": 275, "y": 2050})


