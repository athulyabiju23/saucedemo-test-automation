from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
class BasePage:
    """Parent class for all page objects. Holds common methods."""
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def open_url(self, url):
        self.driver.get(url)
    #time.sleep(5)
    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))
    #
    # time.sleep(5)
    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
    #time.sleep(5)
    def type_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
    #time.sleep(5)
    def get_text(self, locator):
        return self.find_element(locator).text
    #time.sleep(5)
    def is_displayed(self, locator):
        try:
            return self.find_element(locator).is_displayed()
        except:
            return False
    #time.sleep(5)
    def current_url(self):
        return self.driver.current_url
    