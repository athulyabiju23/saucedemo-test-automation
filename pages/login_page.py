from selenium.webdriver.common.by import By
from pages.base_page import BasePage

import time
class LoginPage(BasePage):
    """Page object for the saucedemo login page."""
    
    URL = "https://www.saucedemo.com/"
    
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
    
    def load(self):
        self.open_url(self.URL)
    #time.sleep(5)
    def enter_username(self, username):
        self.type_text(self.USERNAME_INPUT, username)
    #time.sleep(5)
    def enter_password(self, password):
        self.type_text(self.PASSWORD_INPUT, password)
    #time.sleep(5)
    def click_login(self):
        self.click(self.LOGIN_BUTTON)
    #time.sleep(5)
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
    #time.sleep(5)
    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)
    #time.sleep(5)
    def is_error_displayed(self):
        return self.is_displayed(self.ERROR_MESSAGE)