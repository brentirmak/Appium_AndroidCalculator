from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
import time

class SideMenuPage(BasePage):

    MENU_BTN = (AppiumBy.ID, 'calculator.currencyconverter.tipcalculator.unitconverter:id/btn_open_side_menu')
    HOME = (AppiumBy.XPATH, '//android.widget.TextView[@text="Home"]')
    TIP_CALC = (AppiumBy.XPATH, '//android.widget.LinearLayout[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_tip"]')
    UNIT_CONV = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Unit Converter").instance(1)')
    CURRENCY_CONVERTER_MENU_OPTION = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Currency Converter").instance(1)')
    #CURRENCY_CONVERTER_MENU_OPTION = (AppiumBy.XPATH,'//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/tv_title" and @text="Currency Converter"]')

    def open_menu(self):
        print("Will click on the side menu")
        self.click(self.MENU_BTN)
        print("Side menu has been opened")

    def go_home(self):
        self.open_menu()
        print("Will click on the Home option")
        self.click(self.HOME)
        print("Clicked on the Home option")

    def go_tip_calculator(self):
        self.open_menu()
        print("Will click on the Tip Calculator option")
        self.click(self.TIP_CALC)
        print("Clicked on the Tip Calculator option")

    def go_unit_converter(self):
        self.open_menu()
        print("Will click on the Unit Conversion option")
        self.click(self.UNIT_CONV)
        print("Clicked on the Unit Conversion option")

    def click_currency_converter(self):
        self.open_menu()
        print("Will click on the Currency Conversion option")
        self.click(self.CURRENCY_CONVERTER_MENU_OPTION)
        print("Clicked on the Currency Conversion option")