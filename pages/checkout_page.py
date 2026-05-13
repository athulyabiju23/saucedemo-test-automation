from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    """Page object for the multi-step checkout flow."""
    
    # locators - step 1 (info)
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
    
    # locators - step 2 (overview)
    SUBTOTAL_LABEL = (By.CLASS_NAME, "summary_subtotal_label")
    FINISH_BUTTON = (By.ID, "finish")
    
    # locators - complete
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")
    BACK_HOME_BUTTON = (By.ID, "back-to-products")
    
    def fill_customer_info(self, first_name, last_name, postal_code):
        self.type_text(self.FIRST_NAME_INPUT, first_name)
        self.type_text(self.LAST_NAME_INPUT, last_name)
        self.type_text(self.POSTAL_CODE_INPUT, postal_code)
    
    def click_continue(self):
        self.click(self.CONTINUE_BUTTON)
    
    def click_finish(self):
        self.click(self.FINISH_BUTTON)
    
    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)
    
    def is_error_displayed(self):
        return self.is_displayed(self.ERROR_MESSAGE)
    
    def get_subtotal_text(self):
        return self.get_text(self.SUBTOTAL_LABEL)
    
    def get_completion_message(self):
        return self.get_text(self.COMPLETE_HEADER)
    
    def is_order_complete(self):
        return "checkout-complete.html" in self.current_url()