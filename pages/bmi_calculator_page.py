from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BMICalculatorPage(BasePage):
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
    TOTAL_BMI_HEADER = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/bmi_tip_tv")')
    TOTAL_BMI_FIELD = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/bmi_value_tv")')
    BMI_CATEGORY_VALUE = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/bmi_category_tv")')
    BACK_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/btn_back")')

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

    def verify_loaded(self):
        print("Will verify BMI Calculator header is displayed")
        page_title = self.find(self.HEADER).text
        print("Page title: ", page_title)
        return self.exists(self.HEADER), page_title

    def enter_weight_in_kg(self, weight):
        print("Ensuring that kg is selected prior to entering weight")
        self.click(self.WEIGHT_KG_BUTTON)
        print("The kg option is selected - will click on the weight field")
        self.click(self.WEIGHT_FIELD)
        print("Will enter the weight in kg - first clearing the field")
        self.click(self.CLEAR_BUTTON)
        print("Cleared the weight field - will enter value now")
        self.enter_number(weight)
        self.click(self.OK_BUTTON)
        print(f"Entered weight in kg - will verify field contains ", weight)
        weight_value = self.find(self.WEIGHT_FIELD).text
        print("Weight value: ", weight_value)

    def enter_weight_in_lb(self, weight):
        print("Ensuring that lb is selected prior to entering weight")
        self.click(self.WEIGHT_LB_BUTTON)
        print("The lb option is selected - will click on the weight field")
        self.click(self.WEIGHT_FIELD)
        print("Will enter the weight in lb - first clearing the field")
        self.click(self.CLEAR_BUTTON)
        print("Cleared the weight field - will enter value now")
        self.enter_number(weight)
        self.click(self.OK_BUTTON)
        print(f"Entered weight in kg - will verify field contains ", weight)
        weight_value = self.find(self.WEIGHT_FIELD).text
        print("Weight value: ", weight_value)

    def enter_height_in_cm(self,height):
        print("Ensuring that height is selected prior to entering height")
        self.click(self.HEIGHT_CM_BUTTON)
        print("The cm option is selected - will click on the height field")
        self.click(self.HEIGHT_CM_FIELD)
        print("Will enter the height in cm - first clearing the field")
        self.click(self.CLEAR_BUTTON)
        print("Cleared the height field - will enter the value now")
        self.enter_number(height)
        self.click(self.OK_BUTTON)
        print(f"Entered height in cm - will verify field contains ", height)
        height_value = self.find(self.HEIGHT_CM_FIELD).text
        print("Height value: ", height_value)

    def enter_height_in_ft_in(self,ft_height, in_height):
        print("Ensuring that height is selected prior to entering height")
        self.click(self.HEIGHT_FT_IN_BUTTON)
        print("The ft-in option is selected - will click on the height-ft field")
        self.click(self.HEIGHT_FT_FIELD)
        print("Clicked on the height-ft field - first clearing the field")
        self.click(self.CLEAR_BUTTON)
        print("Cleared the field - will enter the ft field now")
        self.enter_number(ft_height)
        self.click(self.OK_BUTTON)
        print("The ft-in option is selected - will click on the height-in field")
        self.click(self.HEIGHT_IN_FIELD)
        print("Clicked on the height-in field - first clearing the field")
        self.click(self.CLEAR_BUTTON)
        print("Cleared the field - will enter the in field now")
        self.enter_number(in_height)
        self.click(self.OK_BUTTON)
        print(f"Entered height in ft-in - will verify field contains ", ft_height, "' ", in_height, "\"")
        height_ft_value = self.find(self.HEIGHT_FT_FIELD).text
        print("Height ft value: ", height_ft_value)
        height_in_value = self.find(self.HEIGHT_IN_FIELD).text
        print("Height in value: ", height_in_value)

    def enter_age(self, age):
        print("Entering the age - will click on the Age field")
        self.click(self.AGE_FIELD)
        print("Clicked on the age field - will clear the field now")
        self.click(self.CLEAR_BUTTON)
        print("Cleared the age field - will enter the value now")
        self.enter_number(age)
        self.click(self.OK_BUTTON)
        print(f"Entered the age - will verify field contains ", age)
        age_value = self.find(self.AGE_FIELD).text
        print("Age value: ", age_value)

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
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.TOTAL_BMI_HEADER)
        )
        print("Clicked on the Calculate button - will capture the BMI Category value")
        element2 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.BMI_CATEGORY_VALUE)
        )
        assert element.is_displayed(), "TOTAL_BMI_HEADER is not displayed"
        assert element2.is_displayed(), "BMI_CATEGORY_VALUE is not displayed"
        bmi_value = self.find(self.TOTAL_BMI_FIELD).text
        bmi_category_value = self.find(self.BMI_CATEGORY_VALUE).text

        return bmi_value, bmi_category_value

    def click_back_button(self):
        print("Will click on the Back button")
        self.click(self.BACK_BUTTON)
        print("Clicked on the Back button")




