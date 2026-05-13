from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InventoryPage(BasePage):
    """Page object for the saucedemo inventory (products) page."""
    
    URL_FRAGMENT = "inventory.html"
    
    # locators
    PAGE_TITLE = (By.CLASS_NAME, "title")
    PRODUCT_CARDS = (By.CLASS_NAME, "inventory_item")
    SHOPPING_CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    
    # dynamic locator for "Add to cart" buttons by product name
    @staticmethod
    def add_to_cart_button(product_name):
        # converts "Sauce Labs Backpack" to "add-to-cart-sauce-labs-backpack"
        product_id = "add-to-cart-" + product_name.lower().replace(" ", "-")
        return (By.ID, product_id)
    
    @staticmethod
    def remove_button(product_name):
        product_id = "remove-" + product_name.lower().replace(" ", "-")
        return (By.ID, product_id)
    
    def is_loaded(self):
        return self.URL_FRAGMENT in self.current_url()
    
    def get_page_title(self):
        return self.get_text(self.PAGE_TITLE)
    
    def get_product_count(self):
        elements = self.driver.find_elements(*self.PRODUCT_CARDS)
        return len(elements)
    
    def add_product_to_cart(self, product_name):
        self.click(self.add_to_cart_button(product_name))
    
    def remove_product_from_cart(self, product_name):
        self.click(self.remove_button(product_name))
    
    def get_cart_count(self):
        # if the badge isn't visible, cart is empty
        if not self.is_displayed(self.CART_BADGE):
            return 0
        return int(self.get_text(self.CART_BADGE))
    
    def go_to_cart(self):
        self.click(self.SHOPPING_CART_LINK)