import logging
import os

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import (
    NoSuchElementException,
    StaleElementReferenceException,
    TimeoutException,
    WebDriverException,
)
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage

log = logging.getLogger(__name__)

# --------------------------------------------------------------------------
# Timeouts: one place to tune. Everything doubles automatically under Jenkins.
# Override with env vars in the Jenkins job if needed.
# --------------------------------------------------------------------------
IS_CI = bool(os.getenv("JENKINS_URL"))
CI_FACTOR = 2 if IS_CI else 1
UI_TIMEOUT = int(os.getenv("UI_TIMEOUT", "15")) * CI_FACTOR
AD_TIMEOUT = int(os.getenv("AD_TIMEOUT", "10")) * CI_FACTOR
# AI answers depend on network + backend latency, so they get the longest wait
AI_RESPONSE_TIMEOUT = int(os.getenv("AI_RESPONSE_TIMEOUT", "45")) * CI_FACTOR

HEADER_AI_SCAN = "AI Scan"
HEADER_AI_CHAT = "AI Chat"

PKG = "calculator.currencyconverter.tipcalculator.unitconverter"


class AICalculatorPage(BasePage):

    HOME_AI_CALCULATOR_ICON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("AI Calculator")')
    TITLE = (AppiumBy.ID, f'{PKG}:id/tv_title')
    CHAT_ICON = (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().resourceId("{PKG}:id/btn_iv_chat")')
    CHAT_TEXTFIELD = (AppiumBy.ID, f'{PKG}:id/et_chat_input')
    ENTER_ICON = (AppiumBy.ID, f'{PKG}:id/btn_send_arrow')
    THREE_FREE_MESSAGES_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("3 Free Messages")')
    REWARD_GRANTED_MSG = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Reward granted")')
    CLOSE_TEST_AD_ICON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Image").instance(0)')
    AD_CLOSED_ICON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Ad closed")')
    ANSWER_HEADER = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Answer")')
    HISTORY_BUTTON = (AppiumBy.ID, f'{PKG}:id/btn_history')
    HISTORY_CHECKBOX = (AppiumBy.ID, f'{PKG}:id/ivClear')
    HISTORY_RADIOBUTTON = (AppiumBy.ID, f'{PKG}:id/hcb_all')
    DELETE_ICON = (AppiumBy.ID, f'{PKG}:id/btn_delete')
    DELETE_CHAT_CONFIRMATION_BUTTON = (AppiumBy.ID, f'{PKG}:id/btn_save')
    HISTORY_BACK_BUTTON = (AppiumBy.ID, f'{PKG}:id/ivClose')
    AI_CHAT_BACK_BUTTON = (AppiumBy.ID, f'{PKG}:id/btn_back')
    NO_HISTORY_MSG = (AppiumBy.ID, f'{PKG}:id/tv_empty_tip')

    # ------------------------------------------------------------------
    # Header helpers (TITLE id is shared by several screens, so always check text)
    # ------------------------------------------------------------------
    def _header_text(self):
        try:
            return self.driver.find_element(*self.TITLE).text or ""
        except (NoSuchElementException, StaleElementReferenceException):
            return ""

    def _wait_for_header(self, expected, timeout=None):
        try:
            self._waiter(timeout or UI_TIMEOUT).until(lambda d: expected in self._header_text())
        except TimeoutException:
            raise AssertionError(
                f"Header containing '{expected}' not found. Got: '{self._header_text()}'"
            )
        return self._header_text()

    def is_on_ai_scan_screen(self, timeout=2):
        try:
            self._waiter(timeout).until(lambda d: HEADER_AI_SCAN in self._header_text())
            return True
        except TimeoutException:
            return False

    # ------------------------------------------------------------------
    # Navigation
    # ------------------------------------------------------------------
    def open_from_home(self):
        log.info("Clicking the AI Calculator option on Home")
        self.click(self.HOME_AI_CALCULATOR_ICON)
        header = self._wait_for_header(HEADER_AI_SCAN)
        log.info("AI Calculator loaded (header: %s)", header)

    def verify_loaded(self):
        """Wait for the AI Scan screen and return its header text (raises AssertionError if it never loads)."""
        return self._wait_for_header(HEADER_AI_SCAN)

    def ensure_on_ai_scan_screen(self, max_steps=5):
        """
        State-aware navigation: get to the AI Scan screen from wherever the previous
        test left the app (home, chat, history overlay). Makes tests order-independent.
        """
        for _ in range(max_steps):
            if self.is_on_ai_scan_screen(timeout=2):
                return
            if self.visible(self.HOME_AI_CALCULATOR_ICON, timeout=1):
                self.open_from_home()
                return
            if self.visible(self.HISTORY_BACK_BUTTON, timeout=1):
                self.click_history_back_icon()
                continue
            if HEADER_AI_CHAT in self._header_text():
                self.click_ai_chat_back_button()
                continue
            log.warning("Unknown screen - sending system Back")
            self.driver.back()
        raise AssertionError("Could not navigate to the AI Scan screen")

    def access_ai_chat_screen(self):
        log.info("Clicking the Chat icon")
        self.click(self.CHAT_ICON)
        header = self._wait_for_header(HEADER_AI_CHAT)
        self.wait_visible(self.CHAT_TEXTFIELD, UI_TIMEOUT)
        log.info("AI Chat screen loaded (header: %s)", header)

    def click_ai_chat_back_button(self):
        log.info("Clicking the Chat back button")
        self.hide_keyboard_if_shown()  # an open keyboard can swallow the tap
        for attempt in (1, 2):
            self.click(self.AI_CHAT_BACK_BUTTON)
            try:
                # Post-condition: we actually left the chat screen
                self._waiter(UI_TIMEOUT).until(lambda d: HEADER_AI_CHAT not in self._header_text())
                return
            except TimeoutException:
                log.warning("Still on AI Chat after back click (attempt %d)", attempt)
        raise AssertionError("Still on the AI Chat screen after clicking back twice")

    # ------------------------------------------------------------------
    # Ads
    # ------------------------------------------------------------------
    def click_ad_closed_icon(self):
        log.info("Clicking the 'Ad closed' icon (blank/black screen)")
        self.click(self.AD_CLOSED_ICON)

    def _handle_reward_ad_if_present(self):
        """Click '3 Free Messages' and close the ad, but only if the prompt actually appears."""
        try:
            button = self._waiter(AD_TIMEOUT).until(EC.element_to_be_clickable(self.THREE_FREE_MESSAGES_BUTTON))
        except TimeoutException:
            log.info("'3 Free Messages' button not displayed - no ad flow needed")
            return False

        button.click()
        log.info("'3 Free Messages' clicked - dismissing ad")
        try:
            self.click(self.REWARD_GRANTED_MSG)
            self.click(self.CLOSE_TEST_AD_ICON)
        except Exception as exc:  # ad UI is third-party and varies run to run; fall back to plain close
            log.info("Reward-style ad not shown (%s) - closing as a plain ad", type(exc).__name__)
            self.click_ad_closed_icon()
        return True

    # ------------------------------------------------------------------
    # Chat history
    # ------------------------------------------------------------------
    def click_history_button(self):
        log.info("Clicking the history button")
        self.click(self.HISTORY_BUTTON)

    def check_history_checkbox(self):
        log.info("Clicking the history checkbox")
        self.click(self.HISTORY_CHECKBOX)

    def click_history_radiobutton(self):
        log.info("Clicking the history radio button")
        self.click(self.HISTORY_RADIOBUTTON)

    def click_delete_icon(self):
        log.info("Clicking the Delete icon")
        self.click(self.DELETE_ICON)

    def click_delete_chat_confirmation_button(self):
        log.info("Clicking the Delete Chat confirmation button")
        self.click(self.DELETE_CHAT_CONFIRMATION_BUTTON)
        self.wait_invisible(self.DELETE_CHAT_CONFIRMATION_BUTTON, UI_TIMEOUT)

    def click_history_back_icon(self):
        log.info("Clicking the History back icon")
        self.click(self.HISTORY_BACK_BUTTON)
        self.wait_invisible(self.HISTORY_BACK_BUTTON, UI_TIMEOUT)

    def verify_no_chat_history(self):
        log.info("Verifying there is no chat history")
        self.wait_visible(self.NO_HISTORY_MSG, UI_TIMEOUT)

    def clear_chat_history(self):
        """
        Open history and delete everything if there is anything to delete.
        Decides explicitly (empty state vs. deletable history) instead of a bare
        try/except, so real failures in the delete flow are no longer swallowed.
        """
        self.click_history_button()
        self.wait_for_any([self.NO_HISTORY_MSG, self.HISTORY_CHECKBOX], UI_TIMEOUT)

        if self.visible(self.NO_HISTORY_MSG, timeout=1):
            log.info("No chat history present - nothing to delete")
        else:
            self.check_history_checkbox()
            self.click_history_radiobutton()
            self.click_delete_icon()
            self.click_delete_chat_confirmation_button()
            self.verify_no_chat_history()
            log.info("Chat history deleted")

        self.click_history_back_icon()

    # ------------------------------------------------------------------
    # Chat calculations
    # ------------------------------------------------------------------
    @staticmethod
    def _answer_locator(expected):
        return (
            AppiumBy.XPATH,
            f'//android.view.View[contains(@text, "{expected}")] | '
            f'//android.widget.TextView[contains(@text, "{expected}")]',
        )

    def _wait_for_answer_text(self, expected):
        locator = self._answer_locator(expected)

        def _read(driver):
            text = driver.find_element(*locator).text
            return text or False

        return self._waiter(UI_TIMEOUT).until(_read)

    def _ask_and_get_answer(self, prompt, expected):
        self.type(self.CHAT_TEXTFIELD, prompt)
        log.info("Entered '%s' - submitting", prompt)
        self.click(self.ENTER_ICON)

        # AI backend latency is the biggest variable here, so this wait is the longest
        self.wait_visible(self.ANSWER_HEADER, AI_RESPONSE_TIMEOUT)
        log.info("Answer header visible")

        self._handle_reward_ad_if_present()

        value = self._wait_for_answer_text(expected)
        log.info("Answer displayed: %s", value)
        return value

    def perform_simple_addition(self):
        return self._ask_and_get_answer("2 plus 2", "4")

    def perform_simple_subtraction(self):
        return self._ask_and_get_answer("12 minus 2", "10")