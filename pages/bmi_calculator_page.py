from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class BMICalculatorPage(BasePage):
    # BMI Calculator (need to add check for the text value)
    HEADER = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/tv_title")')

    WEIGHT_FIELD = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/etWeight")')
    WEIGHT_LB_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/rb_lb")')
    WEIGHT_KG_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/rb_kg")')

    HEIGHT_CM_FIELD = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/etHeightCm")')
    HEIGHT_CM_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/rb_height_cm")')
    HEIGHT_FT_IN_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/rb_height_ft")')
    HEIGHT_FT_FIELD = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/etHeightFt")')
    HEIGHT_IN_FIELD = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/etHeightIn")')

    AGE_FIELD = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/et_age")')

    GENDER_MALE_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/tv_male")')
    GENDER_FEMALE_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/tv_female")')
    CALCULATE_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/btn_cal")')

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
    OK_BUTTON = (AppiumBy.XPATH,'//android.widget.ImageView[@resource-id="calculator.currencyconverter.tipcalculator.unitconverter:id/btn_ok"]')
    CLEAR_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/btn_ac")')

    TOTAL_BMI_FIELD = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/bmi_value_tv")')

    def verify_loaded(self):
        print("Will verify BMI Calculator header is displayed")
        return self.exists(self.HEADER)

    def enter_weight_in_kg(self):
        print("Ensuring that kg is selected prior to entering weight")
        self.click(self.WEIGHT_KG_BUTTON)
        print("The kg option is selected - will click on the weight field")
        self.click(self.WEIGHT_FIELD)
        print("Will enter the weight in kg - first clearing the field")
        self.click(self.CLEAR_BUTTON)
        print("Cleared the weight field - will enter value now")
        self.click(self.NUM1)
        self.click(self.NUM2)
        self.click(self.NUM5)
        self.click(self.OK_BUTTON)
        print("Entered weight in kg - will verify field contains '125'")
        weight_value = self.visible(self.WEIGHT_FIELD).text
        print("Weight value: ", weight_value)

    def enter_height_in_cm(self):
        print("Ensuring that height is selected prior to entering height")
        self.click(self.HEIGHT_CM_BUTTON)
        print("The cm option is selected - will click on the height field")
        self.click(self.HEIGHT_CM_FIELD)
        print("Will enter the height in cm - first clearing the field")
        self.click(self.CLEAR_BUTTON)
        print("Cleared the height field - will enter the value now")
        self.click(self.NUM1)
        self.click(self.NUM9)
        self.click(self.NUM0)
        self.click(self.OK_BUTTON)
        print("Entered height in cm - will verify field contains '190'")
        height_value = self.visible(self.HEIGHT_CM_FIELD).text
        print("Height value: ", height_value)

    def enter_age(self):
        print("Entering the age - will click on the Age field")
        self.click(self.AGE_FIELD)
        print("Clicked on the age field - will clear the field now")
        self.click(self.CLEAR_BUTTON)
        print("Cleared the age field - will enter the value now")
        self.click(self.NUM3)
        self.click(self.NUM8)
        self.click(self.OK_BUTTON)
        print("Entered the age - will verify field contains '38'")
        age_value = self.visible(self.AGE_FIELD).text

    def select_gender(self, gender):
        print("Will select the gender")
        if gender == "Male":
            print("The gender is set to 'Male'")
            self.click(self.GENDER_MALE_BUTTON)
        else:
            print("The gender is set to 'Female'")
            self.click(self.GENDER_FEMALE_BUTTON)

    def click_calculate_button(self):
        print("Will click on the Calculate button")
        self.click(self.CALCULATE_BUTTON)
        print("Clicked on the Calculate button - will capture the BMI value")
        bmi_value = self.visible(self.TOTAL_BMI_FIELD).text





