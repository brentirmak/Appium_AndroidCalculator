from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type(self, locator, text):
        self.find(locator).send_keys(text)

    def exists(self, locator):
        try:
            self.find(locator)
            return True
        except Exception:
            return False

    def safe_click(self, locator):
        try:
            self.click(locator)
            return True
        except Exception:
            return False

