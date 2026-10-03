from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
from playwright.sync_api import expect
import time

class LoanCalculatorPage(BasePage):

    HOME_ICON_LOAN_CALC = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Loan Calculator")')
    # Loan
    HEADER = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/tv_title")')
    # expect(self.HEADER).to_have_text("Loan")
    # Repayment Method
    REPAYMENT_METHOD_FIELD = (AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/btn_pick_payment")')

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
    CLEAR_BUTTON = (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_ac"]')
    OK_BUTTON = (AppiumBy.XPATH, '//android.widget.ImageView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_ok"]')
    SAVE_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/btn_save")')

    # Loan Principle
    LOAN_PRINCIPLE_FIELD = (AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/et_loan_principal")')
    # Interest
    INTEREST_FIELD = (AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/et_loan_interest")')
    # Term
    TERM_FIELD = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/btn_pick_month")')

    # Total Interest
    TOTAL_INTEREST = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/tv_result_total_interest")')

    def open_from_home(self):
        print("Will click on the Loan Calculator option")
        self.click(self.HOME_ICON_LOAN_CALC)
        assert self.verify_loaded(), "Loan Calculator did not load after clicking"
        print("Loan Calculator option has been clicked")

    def verify_loaded(self):
        print("Will verify that the Loan Calculator header has loaded")
        return self.visible(self.HEADER)

    def enter_loan_principal(self):
        print("Will enter loan principal")
        self.click(self.LOAN_PRINCIPLE_FIELD)
        self.click(self.NUM1)
        self.click(self.NUM0)
        self.click(self.NUM0)

    def enter_interest(self):
        print("Will enter the interest")
        self.click(self.INTEREST_FIELD)
        self.click(self.NUM5)

    def enter_term(self):
        print("Will enter the term")
        self.click(self.TERM_FIELD)
        self.click(self.SAVE_BUTTON)

    def calculate_equal_principal_payment_repayment_loan(self):
        print("Will calculate the repayment loan")
        print("Will enter the loan principle")
        self.enter_loan_principal()
        print("Entered the loan principle - will now enter the interest")
        self.enter_interest()
        print("Entered the interest - will enter the term")
        self.enter_term()

        return self.find(self.TOTAL_INTEREST).text
