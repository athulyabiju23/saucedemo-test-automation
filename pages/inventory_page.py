from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time

class InventoryPage(BasePage):
    """Page object for the saucedemo inventory (products) page."""
    
    URL_FRAGMENT = "inventory.html"
    
    PAGE_TITLE = (By.CLASS_NAME, "title")
    PRODUCT_CARDS = (By.CLASS_NAME, "inventory_item")
    SHOPPING_CART = (By.CLASS_NAME, "shopping_cart_link")
    
    def is_loaded(self):
        return self.URL_FRAGMENT in self.current_url()
    
    def get_page_title(self):
        return self.get_text(self.PAGE_TITLE)
    
    def get_product_count(self):
        elements = self.driver.find_elements(*self.PRODUCT_CARDS)
        return len(elements)