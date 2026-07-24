from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class HomePage(BasePage):

    HEADER_HOME = (AppiumBy.XPATH, '//android.widget.TextView[@text="Home"]')
    ICON_BASIC_CALC = (AppiumBy.XPATH, '//android.widget.TextView[@text="Basic Calculator"]')

    TEST_AD = (AppiumBy.XPATH, '//android.widget.TextView[@text="Test Ad"] | //android.webkit.WebView')
    DISMISS_BTN = (AppiumBy.XPATH, '//android.view.View[@resource-id="dismiss-button"]')
    CLOSE_BTN = (
        AppiumBy.XPATH,
        '//android.view.View[@resource-id="close-button"]/android.view.View/android.view.View/android.widget.Image'
    )
    CONTINUE_BTN = (AppiumBy.XPATH, '//android.widget.TextView[@text="Continue to app"]')
    CONTINUE_CLOSE_IMG = (AppiumBy.XPATH, '//android.widget.Image')

    def verify_home_loaded(self):
        if self.exists(self.HEADER_HOME) and self.exists(self.ICON_BASIC_CALC):
            return True

        if self.exists(self.TEST_AD):
            if self.safe_click(self.DISMISS_BTN):
                return True

            if self.safe_click(self.CLOSE_BTN):
                return True

            if self.safe_click(self.CONTINUE_BTN):
                self.safe_click(self.CONTINUE_CLOSE_IMG)
                return True

        return False

