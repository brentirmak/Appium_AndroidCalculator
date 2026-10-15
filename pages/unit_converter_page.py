from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
import time

class UnitConverterPage(BasePage):

    UNIT_CONVERTER_HEADER = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Unit Converter")')
    HOME_ICON_UNIT_CONVERTER = (AppiumBy.XPATH, '//android.widget.TextView[@text="Unit Converter"]')

    CONVERT_FROM_ARROW = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/iv_arrow").instance(0)')
    CONVERT_TO_ARROW = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/iv_arrow").instance(1)')

    FROM_FIELD = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/et_value").instance(0)')
    TO_FIELD = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/et_value").instance(1)')

    TITLE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/tv_title")')

    CM_UNIT = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/root").instance(0)')
    IN_UNIT = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/root").instance(1)')
    M_UNIT = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/root").instance(2)')
    KM_UNIT = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/root").instance(3)')
    MI_UNIT = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/root").instance(4)')
    YD_UNIT = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/root").instance(5)')
    FT_UNIT = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/root").instance(5)')

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
    PERIOD = (AppiumBy.XPATH,'//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_num_dot"]')
    CLR_BUTTON = (AppiumBy.XPATH,'//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_ac"]')
    CAL_BUTTON = (AppiumBy.XPATH,'//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_cal"]')
    XCHANGE_BUTTON = (AppiumBy.XPATH,'//android.widget.ImageView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_exchange"]')
    DELETE_IMG = (AppiumBy.XPATH,'//android.widget.ImageView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_delete"]')
    CLEAR_BTN = (AppiumBy.XPATH,'//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_ac"]')

    RESULT1 = (AppiumBy.XPATH,'(//android.widget.EditText[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/et_value"])[2]',)

    def enter_number(self, number):
        digits = {
            "0": self.NUM0, "1": self.NUM1, "2": self.NUM2,
            "3": self.NUM3, "4": self.NUM4, "5": self.NUM5,
            "6": self.NUM6, "7": self.NUM7, "8": self.NUM8,
            "9": self.NUM9, ".": self.PERIOD,
        }
        for digit in str(number):
            print(f"Will click on '{digit}'")
            self.click(digits[digit])
            print(f"Clicked on '{digit}'")

    def open_from_home(self):
        print("Will click on the Unit Converter option")
        self.click(self.HOME_ICON_UNIT_CONVERTER)
        assert self.verify_loaded(), "Unit Converter did not load after clicking"
        print("Unit Converter option has been clicked")

    def verify_loaded(self):
        print("Will verify Loan Calculator header is displayed")
        page_title = self.find(self.UNIT_CONVERTER_HEADER).text
        print("Page title: ", page_title)
        return self.exists(self.UNIT_CONVERTER_HEADER), page_title

    def select_from_unit(self, unit):
        print("Will select the from unit")
        self.click(self.CONVERT_FROM_ARROW)
        print("Will verify that the title is 'Choose Unit'")
        page_title = self.find(self.TITLE).text
        if page_title == "Choose Unit":
            print("We are on the 'Choose Unit' page")
            if unit == "cm":
                print("Will click on the cm option")
                self.click(self.CM_UNIT)
                print("Clicked on the cm option")
            if unit == "inches":
                print("Will click on the inches option")
                self.click(self.IN_UNIT)
                print("Clicked on the inches option")
            if unit == "meter":
                print("Will click on the meter option")
                self.click(self.M_UNIT)
                print("Clicked on the meter option")
            if unit == "kilometer":
                print("Will click on the kilometer option")
                self.click(self.KM_UNIT)
                print("Clicked on the kilometer option")
            if unit == "mile":
                print("Will click on the mile option")
                self.click(self.MI_UNIT)
                print("Clicked on the mile option")
            if unit == "yd":
                print("Will click on the yard option")
                self.click(self.YD_UNIT)
                print("Clicked on the yard option")
            if unit == "ft":
                print("Will click on the foot option")
                self.click(self.FT_UNIT)
                print("Clicked on the foot option")
        else:
            print("We are NOT on the 'Choose Unit' page")

    def select_to_unit(self, unit):
        print("Will select the to unit")
        self.click(self.CONVERT_TO_ARROW)
        print("Will verify that the title is 'Choose Unit'")
        page_title = self.find(self.TITLE).text
        if page_title == "Choose Unit":
            print("We are on the 'Choose Unit' page")
            if unit == "cm":
                print("Will click on the cm option")
                self.click(self.CM_UNIT)
                print("Clicked on the cm option")
            if unit == "inches":
                print("Will click on the inches option")
                self.click(self.IN_UNIT)
                print("Clicked on the inches option")
            if unit == "meter":
                print("Will click on the meter option")
                self.click(self.M_UNIT)
                print("Clicked on the meter option")
            if unit == "kilometer":
                print("Will click on the kilometer option")
                self.click(self.KM_UNIT)
                print("Clicked on the kilometer option")
            if unit == "mile":
                print("Will click on the mile option")
                self.click(self.MI_UNIT)
                print("Clicked on the mile option")
            if unit == "yd":
                print("Will click on the yard option")
                self.click(self.YD_UNIT)
                print("Clicked on the yard option")
            if unit == "ft":
                print("Will click on the foot option")
                self.click(self.FT_UNIT)
                print("Clicked on the foot option")
        else:
            print("We are NOT on the 'Choose Unit' page")

    def convert_cm_to_inches(self, number1):
        print("Will convert cm to inches")
        print("Clearing previous input")
        self.click(self.CLEAR_BTN)

        print("Clicked on the Clear button - will make sure 'cm' is selected for the from field")
        self.select_from_unit('cm')
        print("Selected 'cm' for the from field - will select 'inches' for the to field")
        self.select_to_unit('inches')
        print(f"Selected inches for the to field - will enter {number1} into the cm field")
        self.click(self.FROM_FIELD)
        self.enter_number(number1)
        print(f"Entered {number1} into the cm field - will check the inches value")

        result_element = self.find(self.RESULT1)
        return result_element.text

    def convert_cm_to_meter(self, number1):
        print("Will convert cm to meters")
        print("Clearing previous input")
        self.click(self.CLEAR_BTN)

        print("Clicked on the Clear button - will make sure 'cm' is selected for the from field")
        self.select_from_unit('cm')
        print("Selected 'cm' for the from field - will select 'meters' for the to field")
        self.select_to_unit('meter')
        print(f"Selected meters for the to field - will enter {number1} into the cm field")
        self.click(self.FROM_FIELD)
        self.enter_number(number1)
        print(f"Entered {number1} into the cm field - will check the meters value")

        result_element = self.find(self.RESULT1)
        return result_element.text

    def convert_cm_to_km(self, number1):
        print("Will convert cm to km")
        print("Clearing previous input")
        self.click(self.CLEAR_BTN)

        print("Clicked on the Clear button - will make sure 'cm' is selected for the from field")
        self.select_from_unit('cm')
        print("Selected 'cm' for the from field - will select 'km' for the to field")
        self.select_to_unit('kilometer')
        print(f"Selected kilometers for the to field - will enter {number1} into the cm field")
        self.click(self.FROM_FIELD)
        self.enter_number(number1)
        print(f"Entered {number1} into the cm field - will check the kms value")

        result_element = self.find(self.RESULT1)
        return result_element.text

    def convert_cm_to_mile(self, number1):
        print("Will convert cm to mile")
        print("Clearing previous input")
        self.click(self.CLEAR_BTN)

        print("Clicked on the Clear button - will make sure 'cm' is selected for the from field")
        self.select_from_unit('cm')
        print("Selected 'cm' for the from field - will select 'mile' for the to field")
        self.select_to_unit('mile')
        print(f"Selected kilometers for the to field - will enter {number1} into the cm field")
        self.click(self.FROM_FIELD)
        self.enter_number(number1)
        print(f"Entered {number1} into the cm field - will check the mile(s) value")

        result_element = self.find(self.RESULT1)
        return result_element.text

    def convert_inch_to_cm(self, number1):
        print("Will convert inch to cm")
        print("Clearing previous input")
        self.click(self.CLEAR_BTN)

        print("Clicked on the Clear button - will make sure 'inch' is selected for the from field")
        self.select_from_unit('inches')
        print("Selected 'inch' for the from field - will select 'cm' for the to field")
        self.select_to_unit('cm')
        print(f"Selected cm for the to field - will enter {number1} into the inches field")
        self.click(self.FROM_FIELD)
        self.enter_number(number1)
        print(f"Entered {number1} into the inch field - will check the cm value")

        result_element = self.find(self.RESULT1)
        return result_element.text

    def convert_inch_to_meter(self, number1):
        print("Will convert inch to m")
        print("Clearing previous input")
        self.click(self.CLEAR_BTN)

        print("Clicked on the Clear button - will make sure 'inch' is selected for the from field")
        self.select_from_unit('inches')
        print("Selected 'inch' for the from field - will select 'm' for the to field")
        self.select_to_unit('meter')
        print(f"Selected meter for the to field - will enter {number1} into the inches field")
        self.click(self.FROM_FIELD)
        self.enter_number(number1)
        print(f"Entered {number1} into the inch field - will check the m value")

        result_element = self.find(self.RESULT1)
        return result_element.text

    def convert_inch_to_kilometer(self, number1):
        print("Will convert inch to km")
        print("Clearing previous input")
        self.click(self.CLEAR_BTN)

        print("Clicked on the Clear button - will make sure 'inch' is selected for the from field")
        self.select_from_unit('inches')
        print("Selected 'inch' for the from field - will select 'm' for the to field")
        self.select_to_unit('kilometer')
        print(f"Selected kilometer for the to field - will enter {number1} into the inches field")
        self.click(self.FROM_FIELD)
        self.enter_number(number1)
        print(f"Entered {number1} into the inch field - will check the km value")

        result_element = self.find(self.RESULT1)
        return result_element.text

    def convert_meter_to_cm(self, number1):
        print("Will convert meter to cm")
        print("Clearing previous input")
        self.click(self.CLEAR_BTN)

        print("Clicked on the Clear button - will make sure 'meter' is selected for the from field")
        self.select_from_unit('meter')
        print("Selected 'meter' for the from field - will select 'cm' for the to field")
        self.select_to_unit('cm')
        print(f"Selected cm for the to field - will enter {number1} into the meter field")
        self.click(self.FROM_FIELD)
        self.enter_number(number1)
        print(f"Entered {number1} into the meter field - will check the cm value")

        result_element = self.find(self.RESULT1)
        return result_element.text

    def convert_meter_to_inch(self, number1):
        print("Will convert meter to inch")
        print("Clearing previous input")
        self.click(self.CLEAR_BTN)

        print("Clicked on the Clear button - will make sure 'meter' is selected for the from field")
        self.select_from_unit('meter')
        print("Selected 'meter' for the from field - will select 'inch' for the to field")
        self.select_to_unit('inches')
        print(f"Selected inch for the to field - will enter {number1} into the meter field")
        self.click(self.FROM_FIELD)
        self.enter_number(number1)
        print(f"Entered {number1} into the meter field - will check the inch value")

        result_element = self.find(self.RESULT1)
        return result_element.text

    def convert_meter_to_km(self, number1):
        print("Will convert meter to km")
        print("Clearing previous input")
        self.click(self.CLEAR_BTN)

        print("Clicked on the Clear button - will make sure 'meter' is selected for the from field")
        self.select_from_unit('meter')
        print("Selected 'meter' for the from field - will select 'km' for the to field")
        self.select_to_unit('kilometer')
        print(f"Selected km for the to field - will enter {number1} into the meter field")
        self.click(self.FROM_FIELD)
        self.enter_number(number1)
        print(f"Entered {number1} into the meter field - will check the km value")

        result_element = self.find(self.RESULT1)
        return result_element.text

    def convert_meter_to_mile(self, number1):
        print("Will convert meter to mile")
        print("Clearing previous input")
        self.click(self.CLEAR_BTN)

        print("Clicked on the Clear button - will make sure 'meter' is selected for the from field")
        self.select_from_unit('meter')
        print("Selected 'meter' for the from field - will select 'mile' for the to field")
        self.select_to_unit('mile')
        print(f"Selected km for the to field - will enter {number1} into the meter field")
        self.click(self.FROM_FIELD)
        self.enter_number(number1)
        print(f"Entered {number1} into the meter field - will check the mile value")

        result_element = self.find(self.RESULT1)
        return result_element.text

    def convert_meter_to_yard(self, number1):
        print("Will convert meter to yard")
        print("Clearing previous input")
        self.click(self.CLEAR_BTN)

        print("Clicked on the Clear button - will make sure 'meter' is selected for the from field")
        self.select_from_unit('meter')
        print("Selected 'meter' for the from field - will select 'yard' for the to field")
        self.select_to_unit('yd')
        print(f"Selected km for the to field - will enter {number1} into the meter field")
        self.click(self.FROM_FIELD)
        self.enter_number(number1)
        print(f"Entered {number1} into the meter field - will check the yard value")

        result_element = self.find(self.RESULT1)
        return result_element.text