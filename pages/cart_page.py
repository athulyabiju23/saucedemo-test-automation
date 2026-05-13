from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    """Page object for the shopping cart page."""
    
    URL_FRAGMENT = "cart.html"
    
    # locators
    PAGE_TITLE = (By.CLASS_NAME, "title")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")
    
    def is_loaded(self):
        return self.URL_FRAGMENT in self.current_url()
    
    def get_page_title(self):
        return self.get_text(self.PAGE_TITLE)
    
    def get_item_count(self):
        items = self.driver.find_elements(*self.CART_ITEMS)
        return len(items)
    
    def get_item_names(self):
        items = self.driver.find_elements(*self.ITEM_NAMES)
        return [item.text for item in items]
    
    def click_checkout(self):
        self.click(self.CHECKOUT_BUTTON)
    
    def click_continue_shopping(self):
        self.click(self.CONTINUE_SHOPPING_BUTTON)