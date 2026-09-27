from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import time


class AICalculatorPage(BasePage):

    HOME_AI_CALCULATOR_ICON = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("AI Calculator")')
    TITLE = (AppiumBy.ID,'calculator.currencyconverter.tipcalculator.unitconverter:id/tv_title')
    CHAT_ICON = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("calculator.currencyconverter.tipcalculator.unitconverter:id/btn_iv_chat")')
    CHAT_TEXTFIELD = (AppiumBy.ID,'calculator.currencyconverter.tipcalculator.unitconverter:id/et_chat_input')
    ENTER_ICON = (AppiumBy.ID,'calculator.currencyconverter.tipcalculator.unitconverter:id/btn_send_arrow')
    THREE_FREE_MESSAGES_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("3 Free Messages")')
    REWARD_GRANTED_MSG = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Reward granted")')
    CLOSE_TEST_AD_ICON = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.widget.Image").instance(0)')
    AD_CLOSED_ICON = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().description("Ad closed")')
    ANSWER_HEADER = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Answer")')
    HISTORY_BUTTON = (AppiumBy.ID,'calculator.currencyconverter.tipcalculator.unitconverter:id/btn_history')
    HISTORY_CHECKBOX = (AppiumBy.ID,'calculator.currencyconverter.tipcalculator.unitconverter:id/ivClear')
    HISTORY_RADIOBUTTON = (AppiumBy.ID,'calculator.currencyconverter.tipcalculator.unitconverter:id/hcb_all')
    DELETE_ICON = (AppiumBy.ID,'calculator.currencyconverter.tipcalculator.unitconverter:id/btn_delete')
    DELETE_CHAT_CONFIRMATION_BUTTON = (AppiumBy.ID,'calculator.currencyconverter.tipcalculator.unitconverter:id/btn_save')
    HISTORY_BACK_BUTTON = (AppiumBy.ID,'calculator.currencyconverter.tipcalculator.unitconverter:id/ivClose')
    AI_CHAT_BACK_BUTTON = (AppiumBy.ID,'calculator.currencyconverter.tipcalculator.unitconverter:id/btn_back')
    NO_HISTORY_MSG = (AppiumBy.ID,'calculator.currencyconverter.tipcalculator.unitconverter:id/tv_empty_tip')
    ANSWER_FIELD = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.view.View").instance(3)')
    ANSWER_VALUE = (AppiumBy.XPATH,'//android.view.View[contains(@text, "4")] | //android.widget.TextView[contains(@text, "4")]')
    ANSWER_VALUE2 = (AppiumBy.XPATH,'//android.view.View[contains(@text, "10")] | //android.widget.TextView[contains(@text, "10")]')

    def open_from_home(self):
        print("Will click on the AI Calculator option")
        self.click(self.HOME_AI_CALCULATOR_ICON)
        assert self.verify_loaded(), "AI Calculator did not load after clicking"
        print("AI Calculator option has been clicked")

    def verify_loaded(self):
        print("Will verify that the AI Calculator header has loaded")
        page_header = self.find(self.TITLE).text
        return page_header

    def access_ai_chat_screen(self):
        print("Will click on the Chat icon")
        self.click(self.CHAT_ICON)
        print("Clicked on the Chat icon - will verify AI Chat header")
        page_header = self.find(self.TITLE).text
        assert "AI Chat" in page_header, f"AI Chat header not found. Got: '{page_header}'"

    def click_ai_chat_back_button(self):
        print("Will click on the Chat back button")
        self.click(self.AI_CHAT_BACK_BUTTON)
        print("Clicked on the Chat back button")

    def click_ad_closed_icon(self):
        print("Will click on the Ad Closed icon (blank/black screen)")
        self.click(self.AD_CLOSED_ICON)
        print("Clicked on the Ad Closed icon")

    def click_history_button(self):
        print("Will click on the history button")
        self.click(self.HISTORY_BUTTON)
        print("Clicked on the history button")

    def check_history_checkbox(self):
        print("Will check the history checkbox")
        self.click(self.HISTORY_CHECKBOX)
        print("Clicked on the history checkbox")

    def click_history_radiobutton(self):
        print("Will click on the History radio button")
        self.click(self.HISTORY_RADIOBUTTON)
        print("Clicked on the History radio button")

    def click_delete_icon(self):
        print("Will click on the Delete icon")
        self.click(self.DELETE_ICON)
        print("Clicked ont he Delete icon")

    def click_history_back_icon(self):
        print("Will click on the History back icon")
        self.click(self.HISTORY_BACK_BUTTON)
        print("Clicked on the History back icon")

    def click_delete_chat_confirmation_button(self):
        print("Will click on the Delete Chat confirmation button")
        self.click(self.DELETE_CHAT_CONFIRMATION_BUTTON)
        print("Clicked ont he Delete Chat confirmation button")

    def verify_no_chat_history(self):
        print("Will verify that there's no chat history")
        self.visible(self.NO_HISTORY_MSG)

    def perform_simple_addition(self):
        print("Will perform simple addition")
        self.type(self.CHAT_TEXTFIELD,"2 plus 2")
        print("Entered '2 plus 2' into the chat textfield - will click on the check/submit button")
        self.click(self.ENTER_ICON)
        print("Clicked on the check/submit button - will check for the Answer header")
        self.visible(self.ANSWER_HEADER)
        print("Answer header is visible - will see if the calculation is displayed")
        try:
            print("Will check to see if the 3 Free Messages button is displayed")
            three_free_messages_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.THREE_FREE_MESSAGES_BUTTON)
            )
            three_free_messages_button.click()
            print("3 Free Messages button has been clicked")
            try:
                print("Will click on the Close 1/2 ad icon/button")
                self.click(self.REWARD_GRANTED_MSG)
                print("Clicked on the Close 1/2 ad icon/button")
                print("Will click on the Reward Granted confirmation icon/button")
                self.click(self.CLOSE_TEST_AD_ICON)
                print("Reward granted confirmation icon/button has been clicked")
            except:
                print("1/2 ad was NOT displayed - will proceed to simply close ad")
                self.click_ad_closed_icon()
                print("Clicked on the close ad button")
            print("Will verify that the answer is '4' is displayed")
            value = self.find(self.ANSWER_VALUE).text
            print("Value: ", value)
            print("'4' is displayed")
            return value
        except:
            print("3 Free Messages button NOT displayed")
            print("Will verify that '4' displayed")
            value = self.find(self.ANSWER_VALUE).text
            print("Value: ", value)
            print("'4' is displayed")
            return value

    def perform_simple_subtraction(self):
        print("Will perform simple subtraction")
        #self.type(self.CHAT_TEXTFIELD,"If I have a dozen eggs that are unbroken and a couple break, how many unbroken eggs do I have left")
        self.type(self.CHAT_TEXTFIELD, "12 minus 2")
        print("Entered the egg question into the chat textfield - will click on the check/submit button")
        self.click(self.ENTER_ICON)
        print("Clicked on the check/submit button - will check for the Answer header")
        self.visible(self.ANSWER_HEADER)
        print("Answer header is visible - will see if the calculation is displayed")
        try:
            print("Will check to see if the 3 Free Messages button is displayed")
            three_free_messages_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.THREE_FREE_MESSAGES_BUTTON)
            )
            three_free_messages_button.click()
            print("3 Free Messages button has been clicked")
            try:
                print("Will click on the Close 1/2 ad icon/button")
                self.click(self.REWARD_GRANTED_MSG)
                print("Clicked on the Close 1/2 ad icon/button")
                print("Will click on the Reward Granted confirmation icon/button")
                self.click(self.CLOSE_TEST_AD_ICON)
                print("Reward granted confirmation icon/button has been clicked")
            except:
                print("1/2 ad was NOT displayed - will proceed to simply close ad")
                self.click_ad_closed_icon()
                print("Clicked on the close ad button")
            print("Will verify that the answer is '10' is displayed")
            value = self.find(self.ANSWER_VALUE2).text
            print("Value: ", value)
            print("'10' is displayed")
            return value
        except:
            print("3 Free Messages button NOT displayed")
            print("Will verify that '10' displayed")
            value = self.find(self.ANSWER_VALUE2).text
            print("Value: ", value)
            print("'10' is displayed")
            return value

