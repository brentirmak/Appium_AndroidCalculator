from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class CurrencyConverterPage(BasePage):
    CURRENCY_CONVERTER_MENU_OPTION = (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/tv_title" and @text="Currency Converter"]')
    CURRENCY_CONVERTER_HEADER = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Currency Converter")')
    FROM_ARROW = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/iv_arrow").instance(0)')
    CHOOSE_CURRENCY_HEADER = (AppiumBy.XPATH,'//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/tv_title" and @text="Choose currency"]')
    SEARCH_CURRENCY_HINT = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/tvInputHint")')
    FOCUSED_EDITTEXT = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.widget.EditText").focused(true)')
    SAVE_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/btn_save")')
    CONFIRM_CURRENCY_SELECTION = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.widget.LinearLayout").instance(1)')
    TO_ARROW = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/iv_arrow").instance(1)')
    NUM9 = (AppiumBy.XPATH,'//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_num_9"]')
    NUM8 = (AppiumBy.XPATH,'//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_num_8"]')
    NUM7 = (AppiumBy.XPATH,'//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_num_7"]')
    NUM6 = (AppiumBy.XPATH,'//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_num_6"]')
    NUM5 = (AppiumBy.XPATH,'//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_num_5"]')
    NUM4 = (AppiumBy.XPATH,'//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_num_4"]')
    NUM3 = (AppiumBy.XPATH,'//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_num_3"]')
    NUM2 = (AppiumBy.XPATH,'//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_num_2"]')
    NUM1 = (AppiumBy.XPATH,'//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_num_1"]')
    NUM0 = (AppiumBy.XPATH,'//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_num_0"]')
    CONVERTED_TO_FIELD = (AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/rv_list"]/android.view.ViewGroup[2]')
    CONVERSION_RESULT = (AppiumBy.XPATH,'(//android.widget.EditText[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/et_value"])[2]')
    CLEAR_BUTTON = (AppiumBy.XPATH,'//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_ac"]')
    NO_SEARCH_RESULT = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/tv_no_result")')
    CLOSE_ICON = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/iv_close")')

    def open_from_home(self):
        print("Will click on the Currency Converter option")
        self.click(self.CURRENCY_CONVERTER_MENU_OPTION)
        assert self.verify_loaded(), "Currency Converter did not load after clicking"
        print("Currency Converter option has been clicked")

    def verify_loaded(self):
        print("Will verify BMI Calculator header is displayed")
        page_title = self.find(self.CURRENCY_CONVERTER_HEADER).text
        print("Page title: ", page_title)
        return self.exists(self.CURRENCY_CONVERTER_HEADER), page_title

    def enter_number(self, number):
        digits = {
            "0": self.NUM0, "1": self.NUM1, "2": self.NUM2,
            "3": self.NUM3, "4": self.NUM4, "5": self.NUM5,
            "6": self.NUM6, "7": self.NUM7, "8": self.NUM8,
            "9": self.NUM9,
        }
        for digit in str(number):
            print(f"Will click on '{digit}'")
            self.click(digits[digit])
            print(f"Clicked on '{digit}'")

    def convert_currency(self, currency_from, currency_from_value, currency_to):
        print(f"Will convert {currency_from} to {currency_to}")

        print(f"Will select the {currency_from} currency option for the 1st field")
        self.click(self.FROM_ARROW)
        print("Clicked on the From Arrow to display the 'Choose Currency' screen")
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.SEARCH_CURRENCY_HINT)).click()

        time.sleep(2)

        field = wait.until(EC.presence_of_element_located(self.FOCUSED_EDITTEXT))
        field.send_keys(currency_from)

        time.sleep(2)

        try:
            print(f"Entered {currency_from} into the 1st field - will confirm currency selection")
            self.click(self.CONFIRM_CURRENCY_SELECTION)
            print("Confirmed currency selection - will now click on the Save button")
            self.click(self.SAVE_BUTTON)
            print("Clicked on the Save button")
        except:
            no_search_result = self.driver.find_element(*self.NO_SEARCH_RESULT)
            if no_search_result.is_displayed():
                self.driver.find_element(*self.CLOSE_ICON).click()
                print("No Search Result message displayed. Close icon clicked.")

        time.sleep(2)

        print(f"Will select the {currency_to} currency option for the 2nd field")
        self.click(self.TO_ARROW)
        print("Clicked on the From Arrow to display the 'Choose Currency' screen")
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.SEARCH_CURRENCY_HINT)).click()

        time.sleep(2)

        field = wait.until(EC.presence_of_element_located(self.FOCUSED_EDITTEXT))
        field.send_keys(currency_to)

        time.sleep(2)

        try:
            print(f"Entered {currency_to} into the 2nd field - will confirm currency selection")
            self.click(self.CONFIRM_CURRENCY_SELECTION)
            print("Confirmed currency selection - will now click on the Save button")
            self.click(self.SAVE_BUTTON)
            print("Clicked on the Save button")
        except:
            no_search_result = self.driver.find_element(*self.NO_SEARCH_RESULT)
            if no_search_result.is_displayed():
                self.driver.find_element(*self.CLOSE_ICON).click()
                print("No Search Result message displayed. Close icon clicked.")

        time.sleep(2)

        print("Will click on the C button to clear")
        self.click(self.CLEAR_BUTTON)
        print("Clicked on the C button")

        self.enter_number(currency_from_value)

        print("Entered the value for the Converted From field - will click on the Converted to field")
        self.click(self.CONVERTED_TO_FIELD)

        output = self.find(self.CONVERSION_RESULT).text
        print(f"Conversion result: {output}")

        return output


