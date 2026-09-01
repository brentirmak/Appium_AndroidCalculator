from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class CurrencyConverterPage(BasePage):
    CURRENCY_CONVERTER_MENU_OPTION = (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/tv_title" and @text="Currency Converter"]')
    CURRENCY_CONVERTER_HEADER = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Currency Converter")')
    FROM_ARROW = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/iv_arrow").instance(0)')
    CHOOSE_CURRENCY_HEADER = (AppiumBy.XPATH,'//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/tv_title" and @text="Choose currency"]')
    USD_CURRENCY_OPTION = (AppiumBy.XPATH,'//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/tv_unit" and @text="USD"]')
    GBP_CURRENCY_OPTION = (AppiumBy.XPATH,'//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/tv_unit" and @text="GBP"]')

    SEARCH_CURRENCY_TEXTFIELD = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/etInput")')
    PICK_CURRENCY = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/root")')
    # new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/btn_save")
    SAVE_BUTTON = (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_save"]')
    TO_ARROW = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/iv_arrow").instance(1)')
    JP_YEN_CURRENCY_OPTION = (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/tv_name" and @text="Japanese Yen"]')
    TR_LIRA_CURRENCY_OPTION = (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/tv_name" and @text="TRY"]')

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
        print("Will verify that the Currency Converter header has loaded")
        return self.visible(self.CURRENCY_CONVERTER_HEADER)

    def convert_usd_to_yen(self):
        print("Will convert USD to Japanese YEN")

        print("Will select the USD currency option for the 1st field")
        self.click(self.FROM_ARROW)
        #self.click(self.USD_CURRENCY_OPTION)
        self.type(self.SEARCH_CURRENCY_TEXTFIELD,"USD")
        self.click(self.PICK_CURRENCY)
        print("Selected USD currency option for the 1st field - will click on the Save button")
        self.click(self.SAVE_BUTTON)
        print("Clicked on the Save button")

        print("Will select the Japanese Yen currency option for the 2nd field")
        self.click(self.TO_ARROW)
        #self.click(self.JP_YEN_CURRENCY_OPTION)
        self.type(self.SEARCH_CURRENCY_TEXTFIELD,"JPY")
        self.click(self.PICK_CURRENCY)
        print("Selected Japanese Yen currency option for the 2nd field - will click on the Save button")
        self.click(self.SAVE_BUTTON)
        print("Clicked on the Save button")

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
        print("Will convert Pound Sterling to Turkish Lira")

        print("Will select the Pound Sterling option for the 1st field")
        self.click(self.FROM_ARROW)
        #self.click(self.GBP_CURRENCY_OPTION)
        self.type(self.SEARCH_CURRENCY_TEXTFIELD,"GBP")
        self.click(self.PICK_CURRENCY)
        print("Selected GBP currency option for the 1st field - will click on the Save button")
        self.click(self.SAVE_BUTTON)
        print("Clicked on the Save button")

        print("Will select the Turkish Lira currency option for the 2nd field")
        self.click(self.TO_ARROW)
        #self.click(self.TR_LIRA_CURRENCY_OPTION)
        self.type(self.SEARCH_CURRENCY_TEXTFIELD,"TRY")
        self.click(self.PICK_CURRENCY)
        print("Selected Turkish Lira currency option for the 2nd field - will click on the Save button")
        self.click(self.SAVE_BUTTON)
        print("Clicked on the Save button")

        print("Will click on the C button to clear")
        self.click(self.CLEAR_BUTTON)
        print("Clicked on the C button")
        print("Will click on the '1' button")
        self.click(self.NUM1)
        print("Clicked on the '1' button - will now click on the '0' button")
        self.click(self.NUM0)
        print("Clicked on the '0' button a 2nd time - will click on the Converted to field")
        self.click(self.CONVERTED_TO_FIELD)

        output = self.find(self.CONVERSION_RESULT).text
        print(f"Conversion result: {output}")

        return output



