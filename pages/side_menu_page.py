from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class SideMenuPage(BasePage):

    MENU_BTN = (AppiumBy.ID, 'calculator.currencyconverter.tipcalculator.unitconverter:id/btn_open_side_menu')
    HOME = (AppiumBy.XPATH, '//android.widget.TextView[@text="Home"]')
    TIP_CALC = (AppiumBy.XPATH, '//android.widget.TextView[@text="Tip Calculator"]')

    def open_menu(self):
        self.click(self.MENU_BTN)

    def go_home(self):
        self.open_menu()
        self.click(self.HOME)

    def go_tip_calculator(self):
        self.open_menu()
        self.click(self.TIP_CALC)
