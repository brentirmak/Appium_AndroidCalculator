from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class DiscountCalculatorPage(BasePage):
    DISCOUNT_CALCULATOR_MENU_OPTION = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Discount Calculator")')
    DISCOUNT_CALCULATOR_HEADER = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Discount")')
    TAX_RATE_FIELD = (AppiumBy.XPATH,'//android.widget.EditText[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/et_tax_rate"]')
    ORIGINAL_PRICE_FIELD = (AppiumBy.XPATH,'//android.widget.EditText[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/et_origin_price"]')
    DISCOUNT_PERCENTAGE_FIELD = (AppiumBy.XPATH,'//android.widget.EditText[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/et_discount"]')
    NUM5 = (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_num_5"]')
    NUM1 = (AppiumBy.XPATH,'//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_num_1"]')
    NUM0 = (AppiumBy.XPATH,'//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_num_0"]')
    CLEAR_BUTTON = (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_ac"]')
    EQUAL_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/btn_equal")')
    RESULT_HEADER = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/tv_result_title")')
    AMOUNT_SAVED_HEADER = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/tv_amount")')
    FINAL_PRICE_HEADER = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/tv_total_price")')
    FINAL_AMOUNT_SAVED_VALUE = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/tv_amount_value")')
    FINAL_TAX_VALUE = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/tv_tax_value")')
    FINAL_PRICE_VALUE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/tv_total_price_value")')
    MINI_MENU = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/btn_more")')
    CLEAR_ALL_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/recycleActions")')
    CONFIRM_CLEAR_ALL_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/btn_save")')

    def open_from_home(self):
        print("Will click on the Discount Calculator option")
        self.click(self.DISCOUNT_CALCULATOR_MENU_OPTION)
        assert self.verify_loaded(), "Discount Calculator did not load after clicking"
        print("Discount Calculator option has been clicked")

    def verify_loaded(self):
        print("Will verify that the Discount Calculator header has loaded")
        return self.visible(self.DISCOUNT_CALCULATOR_HEADER)

    def calculate_discount(self, tax, original_price, discount):
        print("Will enter the tax percentage")

        self.click(self.TAX_RATE_FIELD)

        print("---------------------------------")
        tax_str = str(tax)

        for x in tax_str:
            if x == "1":
                self.click(self.NUM1)
            elif x == "5":
                self.click(self.NUM5)
        print("---------------------------------")

        #self.click(self.NUM1)
        #self.click(self.NUM5)
        #self.type(self.TAX_RATE_FIELD, 15)

        print("Entered the tax rate value - now will enter the original price")
        self.click(self.ORIGINAL_PRICE_FIELD)
        #self.click(self.NUM1)
        #self.click(self.NUM0)
        #self.click(self.NUM0)

        print("---------------------------------")
        original_price_str = str(original_price)

        for x in original_price_str:
            if x == "1":
                self.click(self.NUM1)
            elif x == "0":
                self.click(self.NUM0)
        print("---------------------------------")

        #self.type(self.TAX_RATE_FIELD, 100)

        print("Entered the original price - now will enter the discount percentage")
        self.click(self.DISCOUNT_PERCENTAGE_FIELD)
        #self.click(self.NUM5)

        print("---------------------------------")
        discount_str = str(discount)

        for x in discount_str:
            if x == "5":
                self.click(self.NUM5)
            elif x == "0":
                self.click(self.NUM0)
        print("---------------------------------")

        #self.type(self.DISCOUNT_PERCENTAGE_FIELD, 5)

        print("Entered the discount percentage - will now click on the Equal button")
        self.click(self.EQUAL_BUTTON)
        print("Capturing the results...")
        return self.find(self.FINAL_AMOUNT_SAVED_VALUE).text, self.find(self.FINAL_TAX_VALUE).text, self.find(self.FINAL_PRICE_VALUE).text

    def clear_entries(self, timeout=5):
        print("Will clear all the entries - checking for the Mini Menu")
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(self.MINI_MENU)
            )
        except TimeoutException:
            raise TimeoutException("Mini Menu not found - no previous entries to clear")

        print("Clicked on the Mini Menu - will click on the Clear All option")
        self.click(self.MINI_MENU)
        self.click(self.CLEAR_ALL_BUTTON)
        print("Clicked on the Clear All button - will click on the Delete button")
        self.click(self.CONFIRM_CLEAR_ALL_BUTTON)
        print("Clicked on Delete button to Clear All entries")




