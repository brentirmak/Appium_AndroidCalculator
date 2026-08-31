from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class CurrencyConverterPage(BasePage):
    CURRENCY_CONVERTER_MENU_OPTION = (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/tv_title" and @text="Currency Converter"]')
    CURRENCY_CONVERTER_HEADER = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Currency Converter")')
    FROM_ARROW = (AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/rv_list"]/android.view.ViewGroup[1]/android.widget.ImageView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/iv_arrow"]')
    CHOOSE_CURRENCY_HEADER = (AppiumBy.XPATH,'//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/tv_title" and @text="Choose currency"]')
    USD_CURRENCY_OPTION = (AppiumBy.XPATH,'//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/tv_unit" and @text="USD"]')

    SAVE_BUTTON = (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_save"]')
    TO_ARROW = (AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/rv_list"]/android.view.ViewGroup[2]/android.widget.ImageView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/iv_arrow"]')
    JP_YEN_CURRENCY_OPTION = (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/tv_name" and @text="Japanese Yen"]')

    NUM1 = (AppiumBy.XPATH,'//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_num_1"]')
    NUM0 = (AppiumBy.XPATH,'//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_num_0"]')
    CONVERTED_TO_FIELD = (AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/rv_list"]/android.view.ViewGroup[2]')
    CONVERSION_RESULT = (AppiumBy.XPATH,'(//android.widget.EditText[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/et_value"])[2]')
                                        
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

        #print(self.find(self.CONVERSION_RESULT).text)

        #return self.find(self.CONVERSION_RESULT).text
        return output


