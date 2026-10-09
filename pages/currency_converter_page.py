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

    SEARCH_CURRENCY_HINT = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/tvInputHint")'
    )
    FOCUSED_EDITTEXT = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.EditText").focused(true)'
    )

    SAVE_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/btn_save")')
    CONFIRM_CURRENCY_SELECTION = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.widget.LinearLayout").instance(1)')
    TO_ARROW = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/iv_arrow").instance(1)')
    NUM1 = (AppiumBy.XPATH,'//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_num_1"]')
    NUM0 = (AppiumBy.XPATH,'//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_num_0"]')
    CONVERTED_TO_FIELD = (AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/rv_list"]/android.view.ViewGroup[2]')
    CONVERSION_RESULT = (AppiumBy.XPATH,'(//android.widget.EditText[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/et_value"])[2]')

    CLEAR_BUTTON = (AppiumBy.XPATH,'//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_ac"]')

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

    def convert_usd_to_yen(self):
        print("Will convert USD to Japanese YEN")

        print("Will select the USD currency option for the 1st field")
        self.click(self.FROM_ARROW)
        print("Clicked on the From Arrow to display the 'Choose Currency' screen")
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.SEARCH_CURRENCY_HINT)).click()

        time.sleep(2)

        field = wait.until(EC.presence_of_element_located(self.FOCUSED_EDITTEXT))
        field.send_keys("USD")

        time.sleep(2)

        print("Entered USD into the 1st field - will confirm currency selection")
        self.click(self.CONFIRM_CURRENCY_SELECTION)
        print("Confirmed currency selection - will now click on the Save button")
        self.click(self.SAVE_BUTTON)
        print("Clicked on the Save button")

        time.sleep(2)

        print("Will select the Japanese Yen currency option for the 2nd field")
        self.click(self.TO_ARROW)
        print("Clicked on the From Arrow to display the 'Choose Currency' screen")
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.SEARCH_CURRENCY_HINT)).click()

        time.sleep(2)

        field = wait.until(EC.presence_of_element_located(self.FOCUSED_EDITTEXT))
        field.send_keys("YEN")

        time.sleep(2)

        print("Entered JPY into the 1st field - will confirm currency selection")
        self.click(self.CONFIRM_CURRENCY_SELECTION)
        print("Confirmed currency selection - will now click on the Save button")
        self.click(self.SAVE_BUTTON)
        print("Clicked on the Save button")

        time.sleep(2)

        print("Will click on the C button to clear")
        self.click(self.CLEAR_BUTTON)
        print("Clicked on the C button")
        print("Will click on the '1' button")
        self.click(self.NUM1)
        print("Clicked on the '1' button - will now click on the '0' button")
        self.click(self.NUM0)
        print("Clicked on the '0' button - will click on the '0' button again")
        self.click(self.NUM0)
        print("Clicked on the '0' button a 2nd time - will click on the Converted to field")
        self.click(self.CONVERTED_TO_FIELD)

        output = self.find(self.CONVERSION_RESULT).text
        print(f"Conversion result: {output}")

        return output


    def convert_gbp_to_trl(self):
        print("Will convert GBP to Turkish Lira")

        print("Will select the GBP currency option for the 1st field")
        self.click(self.FROM_ARROW)
        print("Clicked on the From Arrow to display the 'Choose Currency' screen")
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.SEARCH_CURRENCY_HINT)).click()

        time.sleep(2)

        field = wait.until(EC.presence_of_element_located(self.FOCUSED_EDITTEXT))
        field.send_keys("GBP")

        time.sleep(2)

        print("Entered GBP into the 1st field - will confirm currency selection")
        self.click(self.CONFIRM_CURRENCY_SELECTION)
        print("Confirmed currency selection - will now click on the Save button")
        self.click(self.SAVE_BUTTON)
        print("Clicked on the Save button")

        time.sleep(2)

        print("Will select the Turkish Lira currency option for the 2nd field")
        self.click(self.TO_ARROW)
        print("Clicked on the From Arrow to display the 'Choose Currency' screen")
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.SEARCH_CURRENCY_HINT)).click()

        time.sleep(2)

        field = wait.until(EC.presence_of_element_located(self.FOCUSED_EDITTEXT))
        field.send_keys("TRY")

        time.sleep(2)

        print("Entered TRY into the 1st field - will confirm currency selection")
        self.click(self.CONFIRM_CURRENCY_SELECTION)
        print("Confirmed currency selection - will now click on the Save button")
        self.click(self.SAVE_BUTTON)
        print("Clicked on the Save button")

        time.sleep(2)

        print("Will click on the C button to clear")
        self.click(self.CLEAR_BUTTON)
        print("Clicked on the C button")
        print("Will click on the '1' button")
        self.click(self.NUM1)
        print("Clicked on the '1' button - will now click on the '0' button")
        self.click(self.NUM0)
        print("Clicked on the '0' button - will now click on the '0' button")
        self.click(self.NUM0)
        print("Clicked on the '0' button a 2nd time - will click on the Converted to field")
        self.click(self.CONVERTED_TO_FIELD)

        output = self.find(self.CONVERSION_RESULT).text
        print(f"Conversion result: {output}")

        return output



