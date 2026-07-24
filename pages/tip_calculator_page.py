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
        if self.safe_click(self.CLEAR_MORE):
            self.safe_click(self.CLEAR_RECYCLE)
            self.safe_click(self.CLEAR_SAVE)

    def verify_loaded(self):
        return self.exists(self.HEADER)

    def calculate_tip(self, bill: str, tip: str):
        self.find(self.HEADER)

        self.click(self.BILL_FIELD)
        self.type(self.BILL_FIELD, bill)

        tip_el = self.find(self.TIP_FIELD)
        tip_el.clear()
        self.click(self.TIP_FIELD)
        self.type(self.TIP_FIELD, tip)

        self.click(self.EQUAL_BTN)
        return self.find(self.OUTPUT).text

