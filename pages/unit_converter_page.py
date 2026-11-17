from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class UnitConverterPage(BasePage):

    UNIT_CONVERTER_HEADER = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Unit Converter")')
    HOME_ICON_UNIT_CONVERTER = (AppiumBy.XPATH, '//android.widget.TextView[@text="Unit Converter"]')
    CONVERT_FROM_ARROW = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/iv_arrow").instance(0)')
    CONVERT_TO_ARROW = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/iv_arrow").instance(1)')
    FROM_FIELD = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/et_value").instance(0)')
    TO_FIELD = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/et_value").instance(1)')
    TITLE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/tv_title")')

    # UNIT DROPDOWN
    CONVERSION_TYPE = (AppiumBy.XPATH,'//android.widget.TextView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/tv_unit_name"]')
    CHOOSE_UNIT_HEADER = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Choose Unit")')
    LENGTH_OPTION = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Length")')
    MASS_OPTION = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Mass")')
    AREA_OPTION = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Area")')
    VOLUME_OPTION = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Volume")')
    TIME_OPTION = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Time")')

    # LENGTH
    CM_UNIT = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/root").instance(0)')
    IN_UNIT = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/root").instance(1)')
    M_UNIT = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/root").instance(2)')
    KM_UNIT = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/root").instance(3)')
    MI_UNIT = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/root").instance(4)')
    YD_UNIT = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/root").instance(5)')
    FT_UNIT = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/root").instance(6)')
    MM_UNIT = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/root").instance(7)')
    DM_UNIT = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/root").instance(8)')

    # MASS
    KG_UNIT = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("kg")')
    LB_UNIT = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("lb")')
    MG_UNIT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("mg")')
    G_UNIT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("g")')
    OZ_UNIT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("oz")')
    TON_UNIT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("t")')

    # AREA
    SQUARE_M_UNIT = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("m²")')
    SQUARE_INCH_UNIT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("in²")')
    SQUARE_FT_UNIT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("ft²")')
    SQUARE_MILE_UNIT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("mi²")')
    SQUARE_YD_UNIT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("yd²")')
    SQUARE_MM_UNIT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("mm²")')
    SQUARE_CM_UNIT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("cm²")')
    SQUARE_DM_UNIT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("dm²")')
    SQUARE_KM_UNIT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("km²")')
    HA_UNIT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("ha")')
    AC_UNIT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("ac")')

    # VOLUME
    L_UNIT = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("L")')
    ML_UNIT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("mL")')
    CL_UNIT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("cL")')
    DL_UNIT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("dL")')
    HL_UNIT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("hL")')
    KL_UNIT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("kL")')

    # TIME
    HR_UNIT = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("h")')
    SEC_UNIT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("s")')
    MS_UNIT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("ms")')
    MICROS_UNIT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("µs")')
    NS_UNIT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("ns")')
    MIN_UNIT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("m")')

    # CALCULATOR KEYS
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

    def click_conversion_type_option(self):
        print("Will click the conversion type menu")
        self.click(self.CONVERSION_TYPE)
        print("Clicked on the Conversion type menu")

    def select_conversion_type_value(self, conversion_type):
        if conversion_type == "Length":
            print(f"Will select the {conversion_type} conversion type")
            self.click(self.LENGTH_OPTION)
            print(f"Clicked on the {conversion_type} option")
        elif conversion_type == "Mass":
            print(f"Will select the {conversion_type} conversion type")
            self.click(self.MASS_OPTION)
            print(f"Clicked on the {conversion_type} option")
        elif conversion_type == "Area":
            print(f"Will select the {conversion_type} conversion type")
            self.click(self.AREA_OPTION)
            print(f"Clicked on the {conversion_type} option")
        elif conversion_type == "Volume":
            print(f"Will select the {conversion_type} conversion type")
            self.click(self.VOLUME_OPTION)
            print(f"Clicked on the {conversion_type} option")
        elif conversion_type == "Time":
            print(f"Will select the {conversion_type} conversion type")
            self.click(self.TIME_OPTION)
            print(f"Clicked on the {conversion_type} option")

    def get_conversion_type(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.CONVERSION_TYPE)
        )
        return element.text

    def select_length_from_unit(self, unit):
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

    def select_length_to_unit(self, unit):
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

    def select_mass_from_unit(self, unit):
        print("Will select the from unit")
        self.click(self.CONVERT_FROM_ARROW)
        print("Will verify that the title is 'Choose Unit'")
        page_title = self.find(self.TITLE).text
        if page_title == "Choose Unit":
            print("We are on the 'Choose Unit' page")
            if unit == "lb":
                print("Will click on the lb option")
                self.click(self.LB_UNIT)
                print("Clicked on the lb option")
            if unit == "mg":
                print("Will click on the mg option")
                self.click(self.MG_UNIT)
                print("Clicked on the mg option")
            if unit == "kg":
                print("Will click on the kg option")
                self.click(self.KG_UNIT)
                print("Clicked on the kg option")
            if unit == "g":
                print("Will click on the g option")
                self.click(self.G_UNIT)
                print("Clicked on the g option")
            if unit == "oz":
                print("Will click on the oz option")
                self.click(self.OZ_UNIT)
                print("Clicked on the oz option")
            if unit == "t":
                print("Will click on the t option")
                self.click(self.TON_UNIT)
                print("Clicked on the t option")
        else:
            print("We are NOT on the 'Choose Unit' page")

    def select_mass_to_unit(self, unit):
        print("Will select the to unit")
        self.click(self.CONVERT_TO_ARROW)
        print("Will verify that the title is 'Choose Unit'")
        page_title = self.find(self.TITLE).text
        if page_title == "Choose Unit":
            print("We are on the 'Choose Unit' page")
            if unit == "kg":
                print("Will click on the kg option")
                self.click(self.KG_UNIT)
                print("Clicked on the kg option")
            if unit == "lb":
                print("Will click on the lb option")
                self.click(self.LB_UNIT)
                print("Clicked on the lb option")
            if unit == "mg":
                print("Will click on the mg option")
                self.click(self.MG_UNIT)
                print("Clicked on the mg option")
            if unit == "g":
                print("Will click on the g option")
                self.click(self.G_UNIT)
                print("Clicked on the g option")
            if unit == "oz":
                print("Will click on the oz option")
                self.click(self.OZ_UNIT)
                print("Clicked on the oz option")
            if unit == "t":
                print("Will click on the t option")
                self.click(self.TON_UNIT)
                print("Clicked on the t option")
        else:
            print("We are NOT on the 'Choose Unit' page")

    def select_area_from_unit(self, unit):
        print("Will select the from unit")
        self.click(self.CONVERT_FROM_ARROW)
        print("Will verify that the title is 'Choose Unit'")
        page_title = self.find(self.TITLE).text
        if page_title == "Choose Unit":
            print("We are on the 'Choose Unit' page")
            if unit == "m²":
                print("Will click on the m² option")
                self.click(self.SQUARE_M_UNIT)
                print("Clicked on the m² option")
            if unit == "in²":
                print("Will click on the in² option")
                self.click(self.SQUARE_INCH_UNIT)
                print("Clicked on the in² option")
            if unit == "ft²":
                print("Will click on the ft² option")
                self.click(self.SQUARE_FT_UNIT)
                print("Clicked on the ft² option")
            if unit == "mi²":
                print("Will click on the mi² option")
                self.click(self.SQUARE_MILE_UNIT)
                print("Clicked on the mi² option")
            if unit == "yd²":
                print("Will click on the yd² option")
                self.click(self.SQUARE_YD_UNIT)
                print("Clicked on the yd² option")
            if unit == "mm²":
                print("Will click on the mm² option")
                self.click(self.SQUARE_MM_UNIT)
                print("Clicked on the mm² option")
        else:
            print("We are NOT on the 'Choose Unit' page")

    def select_area_to_unit(self, unit):
        print("Will select the to unit")
        self.click(self.CONVERT_TO_ARROW)
        print("Will verify that the title is 'Choose Unit'")
        page_title = self.find(self.TITLE).text
        if page_title == "Choose Unit":
            print("We are on the 'Choose Unit' page")
            if unit == "m²":
                print("Will click on the m² option")
                self.click(self.SQUARE_M_UNIT)
                print("Clicked on the m² option")
            if unit == "in²":
                print("Will click on the in² option")
                self.click(self.SQUARE_INCH_UNIT)
                print("Clicked on the in² option")
            if unit == "ft²":
                print("Will click on the ft² option")
                self.click(self.SQUARE_FT_UNIT)
                print("Clicked on the ft² option")
            if unit == "mi²":
                print("Will click on the mi² option")
                self.click(self.SQUARE_MILE_UNIT)
                print("Clicked on the mi² option")
            if unit == "yd²":
                print("Will click on the yd² option")
                self.click(self.SQUARE_YD_UNIT)
                print("Clicked on the yd² option")
            if unit == "mm²":
                print("Will click on the mm² option")
                self.click(self.SQUARE_MM_UNIT)
                print("Clicked on the mm² option")
        else:
            print("We are NOT on the 'Choose Unit' page")

    def select_volume_from_unit(self, unit):
        print("Will select the from unit")
        self.click(self.CONVERT_FROM_ARROW)
        print("Will verify that the title is 'Choose Unit'")
        page_title = self.find(self.TITLE).text
        if page_title == "Choose Unit":
            print("We are on the 'Choose Unit' page")
            if unit == "L":
                print("Will click on the L option")
                self.click(self.L_UNIT)
                print("Clicked on the L option")
            if unit == "mL":
                print("Will click on the mL option")
                self.click(self.ML_UNIT)
                print("Clicked on the mL option")
            if unit == "cL":
                print("Will click on the cL option")
                self.click(self.CL_UNIT)
                print("Clicked on the cL option")
            if unit == "dL":
                print("Will click on the dL option")
                self.click(self.DL_UNIT)
                print("Clicked on the dL option")
            if unit == "hL":
                print("Will click on the hL option")
                self.click(self.HL_UNIT)
                print("Clicked on the hL option")
            if unit == "kL":
                print("Will click on the kL option")
                self.click(self.KL_UNIT)
                print("Clicked on the kL option")
        else:
            print("We are NOT on the 'Choose Unit' page")

    def select_volume_to_unit(self, unit):
        print("Will select the to unit")
        self.click(self.CONVERT_TO_ARROW)
        print("Will verify that the title is 'Choose Unit'")
        page_title = self.find(self.TITLE).text
        if page_title == "Choose Unit":
            print("We are on the 'Choose Unit' page")
            if unit == "L":
                print("Will click on the L option")
                self.click(self.L_UNIT)
                print("Clicked on the L option")
            if unit == "mL":
                print("Will click on the mL option")
                self.click(self.ML_UNIT)
                print("Clicked on the mL option")
            if unit == "cL":
                print("Will click on the cL option")
                self.click(self.CL_UNIT)
                print("Clicked on the cL option")
            if unit == "dL":
                print("Will click on the dL option")
                self.click(self.DL_UNIT)
                print("Clicked on the dL option")
            if unit == "hL":
                print("Will click on the hL option")
                self.click(self.HL_UNIT)
                print("Clicked on the hL option")
            if unit == "kL":
                print("Will click on the kL option")
                self.click(self.KL_UNIT)
                print("Clicked on the kL option")
        else:
            print("We are NOT on the 'Choose Unit' page")

    def select_time_from_unit(self, unit):
        print("Will select the from unit")
        self.click(self.CONVERT_FROM_ARROW)
        print("Will verify that the title is 'Choose Unit'")
        page_title = self.find(self.TITLE).text
        if page_title == "Choose Unit":
            print("We are on the 'Choose Unit' page")
            if unit == "h":
                print("Will click on the h option")
                self.click(self.HR_UNIT)
                print("Clicked on the h option")
            if unit == "s":
                print("Will click on the s option")
                self.click(self.SEC_UNIT)
                print("Clicked on the s option")
            if unit == "ms":
                print("Will click on the ms option")
                self.click(self.MS_UNIT)
                print("Clicked on the ms option")
            if unit == "µs":
                print("Will click on the µs option")
                self.click(self.MICROS_UNIT)
                print("Clicked on the µs option")
            if unit == "ns":
                print("Will click on the ns option")
                self.click(self.NS_UNIT)
                print("Clicked on the ns option")
            if unit == "min":
                print("Will click on the min option")
                self.click(self.MIN_UNIT)
                print("Clicked on the min option")
        else:
            print("We are NOT on the 'Choose Unit' page")

    def select_time_to_unit(self, unit):
        print("Will select the to unit")
        self.click(self.CONVERT_TO_ARROW)
        print("Will verify that the title is 'Choose Unit'")
        page_title = self.find(self.TITLE).text
        if page_title == "Choose Unit":
            print("We are on the 'Choose Unit' page")
            if unit == "h":
                print("Will click on the h option")
                self.click(self.HR_UNIT)
                print("Clicked on the h option")
            if unit == "s":
                print("Will click on the s option")
                self.click(self.SEC_UNIT)
                print("Clicked on the s option")
            if unit == "ms":
                print("Will click on the ms option")
                self.click(self.MS_UNIT)
                print("Clicked on the ms option")
            if unit == "µs":
                print("Will click on the µs option")
                self.click(self.MICROS_UNIT)
                print("Clicked on the µs option")
            if unit == "ns":
                print("Will click on the ns option")
                self.click(self.NS_UNIT)
                print("Clicked on the ns option")
            if unit == "min":
                print("Will click on the min option")
                self.click(self.MIN_UNIT)
                print("Clicked on the min option")
        else:
            print("We are NOT on the 'Choose Unit' page")

    def convert_length(self,length_from, length_from_value, length_to):
        print(f"Will convert {length_from} to {length_to}")
        print("Clearing previous input")
        self.click(self.CLEAR_BTN)

        print(f"Clicked on the Clear button - will make sure {length_from} is selected for the from field")
        self.select_length_from_unit(length_from)
        print(f"Selected {length_from} for the from field - will select {length_to} for the to field")
        self.select_length_to_unit(length_to)
        print(f"Selected inches for the to field - will enter {length_from_value} into the cm field")
        self.click(self.FROM_FIELD)
        self.enter_number(length_from_value)
        print(f"Entered {length_from_value} into the {length_from} field - will check the {length_to} value")

        result_element = self.find(self.RESULT1)
        return result_element.text

    def convert_mass(self, mass_from, mass_from_value, mass_to):
        print(f"Will convert {mass_from} to {mass_to}")
        print("Clearing previous input")
        self.click(self.CLEAR_BTN)

        print(f"Clicked on the Clear button - will make sure {mass_from} is selected for the from field")
        self.select_mass_from_unit(mass_from)
        print(f"Selected {mass_from} for the from field - will select {mass_to} for the to field")
        self.select_mass_to_unit(mass_to)
        print(f"Selected {mass_to} for the to field - will enter {mass_from_value} into the {mass_from} field")
        self.click(self.FROM_FIELD)
        self.enter_number(mass_from_value)
        print(f"Entered {mass_from_value} into the {mass_from} field - will check the {mass_to} value")

        result_element = self.find(self.RESULT1)
        return result_element.text

    def convert_area(self, area_from, area_from_value, area_to):
        print(f"Will convert {area_from} to {area_to}")
        print("Clearing previous input")
        self.click(self.CLEAR_BTN)

        print(f"Clicked on the Clear button - will make sure {area_from} is selected for the from field")
        self.select_area_from_unit(area_from)
        print(f"Selected {area_from} for the from field - will select {area_to} for the to field")
        self.select_area_to_unit(area_to)
        print(f"Selected {area_to} for the to field - will enter {area_from_value} into the {area_from} field")
        self.click(self.FROM_FIELD)
        self.enter_number(area_from_value)
        print(f"Entered {area_from_value} into the {area_from} field - will check the {area_to} value")

        result_element = self.find(self.RESULT1)
        return result_element.text

    def convert_volume(self, volume_from, volume_from_value, volume_to):
        print(f"Will convert {volume_from} to {volume_to}")
        print("Clearing previous input")
        self.click(self.CLEAR_BTN)

        print(f"Clicked on the Clear button - will make sure {volume_from} is selected for the from field")
        self.select_volume_from_unit(volume_from)
        print(f"Selected {volume_from} for the from field - will select {volume_to} for the to field")
        self.select_volume_to_unit(volume_to)
        print(f"Selected {volume_to} for the to field - will enter {volume_from_value} into the {volume_from} field")
        self.click(self.FROM_FIELD)
        self.enter_number(volume_from_value)
        print(f"Entered {volume_from_value} into the {volume_from} field - will check the {volume_to} value")

        result_element = self.find(self.RESULT1)
        return result_element.text

    def convert_time(self, time_from, time_from_value, time_to):
        print(f"Will convert {time_from} to {time_to}")
        print("Clearing previous input")
        self.click(self.CLEAR_BTN)

        print(f"Clicked on the Clear button - will make sure {time_from} is selected for the from field")
        self.select_time_from_unit(time_from)
        print(f"Selected {time_from} for the from field - will select {time_to} for the to field")
        self.select_time_to_unit(time_to)
        print(f"Selected {time_to} for the to field - will enter {time_from_value} into the {time_from} field")
        self.click(self.FROM_FIELD)
        self.enter_number(time_from_value)
        print(f"Entered {time_from_value} into the {time_from} field - will check the {time_to} value")

        result_element = self.find(self.RESULT1)
        return result_element.text