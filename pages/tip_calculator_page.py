from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class TipCalculatorPage(BasePage):

    HEADER = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/tv_tip_on"]'
    )

    BILL_FIELD = (
        AppiumBy.XPATH,
        '//android.widget.EditText[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/et_bill"]'
    )
    TIP_FIELD = (
        AppiumBy.XPATH,
        '//android.widget.EditText[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/et_tip"]'
    )

    EQUAL_BTN = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_equal"]'
    )
    OUTPUT = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/tv_average_amount_value"]'
    )

    CLEAR_MORE = (
        AppiumBy.XPATH,
        '//android.widget.ImageView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_more"]'
    )
    CLEAR_RECYCLE = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/recycleActions"]'
    )
    CLEAR_SAVE = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_save"]'
    )

    def clear_previous_entries(self):
        print("Will click on the Clear-More button")
        if self.safe_click(self.CLEAR_MORE):
            print("Will click on the Clear-Recycle button")
            self.safe_click(self.CLEAR_RECYCLE)
            print("Will click on the Clear-Save button")
            self.safe_click(self.CLEAR_SAVE)

    def verify_loaded(self):
        print("Will verify Tip Calculator header is displayed")
        return self.exists(self.HEADER)

    def calculate_tip(self, bill: str, tip: str):
        print("Will verify Tip Calculator header")
        self.find(self.HEADER)

        print("Will click on the Bill field")
        self.click(self.BILL_FIELD)
        print("Will enter bill value into the Bill field")
        self.type(self.BILL_FIELD, bill)
        print("Entered the bill value into the Bill field - will click on the Tip field")
        tip_el = self.find(self.TIP_FIELD)
        print("Will clear the Tip field")
        tip_el.clear()
        print("Cleared the tip field - Will click on the Tip field again")
        self.click(self.TIP_FIELD)
        print("Clicked on the Tip field - will enter the tip value")
        self.type(self.TIP_FIELD, tip)
        print("Entered the tip value in to the tip field - will click on the '=' icon")
        self.click(self.EQUAL_BTN)
        print("Clicked on the Equal button - will capture the output")
        return self.find(self.OUTPUT).text

