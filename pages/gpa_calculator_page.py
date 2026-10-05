from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class GPACalculatorPage(BasePage):
    HEADER = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/tv_title")')
    ADD_A_SUBJECT_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/btn_add_course")')
    SUBJECT_NAME_FIELD = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/et_subject")')
    CREDITS_FIELD = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/et_credit")')
    GRADES_FIELD = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/et_grade")')
    CANCEL_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/btn_cancel")')
    ADD_OK_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/btn_add")')
    DELETE_ICON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/btn_clear")')
    TRASH_ICON = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/btn_delete")')
    DELETE_CONFIRM_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/btn_save")')

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

    TOP_COURSE_ENTRY = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/tv_course_name")')
    TOP_RECORD = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/iv_check_box").instance(0)')

    NO_DATA_LABEL = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/tv_empty_tip")')

    def click_add_a_subject_button(self):
        print("Will click on the Add a Subject button")
        self.click(self.ADD_A_SUBJECT_BUTTON)
        print("Clicked on the Add a Subject button")

    def verify_loaded(self):
        print("Will verify GPA Calculator header is displayed")
        return self.exists(self.HEADER)

    def verify_top_course_entry(self):
        print("Will verify that there's a course entry")
        return self.exists(self.TOP_COURSE_ENTRY)

    def verify_no_data(self):
        print("Will verify that there's no data under GPA Calculator")
        return self.exists(self.NO_DATA_LABEL)

    def enter_subject_details(self):
        print("Will enter subject details - clicking on Subject Name field")
        self.click(self.SUBJECT_NAME_FIELD)
        print("Clicked on the Subject Name field - will enter Math into the field")
        self.type(self.SUBJECT_NAME_FIELD,'MATH')
        print("Entered the subject name - will enter the Credits")
        self.click(self.CREDITS_FIELD)
        self.click(self.NUM1)
        self.click(self.NUM0)
        print("Entered 10 - will now click on the OK button")
        self.click(self.OK_BUTTON)
        print("Will now enter the Grade")
        self.click(self.GRADES_FIELD)
        self.click(self.NUM1)
        self.click(self.NUM0)
        self.click(self.NUM0)
        print("Entered 100 - will now click on the OK button")
        self.click(self.OK_BUTTON)
        self.click(self.ADD_OK_BUTTON)
        print("Clicked on the OK button to add the Subject")

    def delete_top_subject(self):
        print("This segment will delete the top subject")
        print("Will click on the Delete icon to go to Delete section")
        self.click(self.DELETE_ICON)
        print("Clicked on the Delete icon - will now select the top record")
        self.click(self.TOP_RECORD)
        print("Clicked on the top record - will now click on the Trash icon")
        self.click(self.TRASH_ICON)
        print("Clicked on the Trash icon - will confirm deletion")
        self.click(self.DELETE_CONFIRM_BUTTON)
        print("Confirmed the deletion of record")
        self.verify_no_data()
        print("Verified that there's no data under GPA Calculator")





