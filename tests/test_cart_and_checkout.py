import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


class TestCartAndCheckout:
    """Tests for adding items to cart and completing checkout."""
    
    def _login_as_standard_user(self, driver):
        """Helper to log in. Reused across all tests in this class."""
        login_page = LoginPage(driver)
        login_page.load()
        login_page.login("standard_user", "secret_sauce")
        return InventoryPage(driver)
    
    def test_add_single_item_to_cart(self, driver):
        inventory_page = self._login_as_standard_user(driver)
        
        assert inventory_page.is_loaded()
        assert inventory_page.get_cart_count() == 0, "Cart should start empty"
        
        inventory_page.add_product_to_cart("Sauce Labs Backpack")
        
        assert inventory_page.get_cart_count() == 1, "Cart should have 1 item after adding"
    
    def test_add_multiple_items_to_cart(self, driver):
        inventory_page = self._login_as_standard_user(driver)
        
        inventory_page.add_product_to_cart("Sauce Labs Backpack")
        inventory_page.add_product_to_cart("Sauce Labs Bike Light")
        inventory_page.add_product_to_cart("Sauce Labs Bolt T-Shirt")
        
        assert inventory_page.get_cart_count() == 3
    
    def test_remove_item_from_cart(self, driver):
        inventory_page = self._login_as_standard_user(driver)
        
        inventory_page.add_product_to_cart("Sauce Labs Backpack")
        inventory_page.add_product_to_cart("Sauce Labs Bike Light")
        assert inventory_page.get_cart_count() == 2
        
        inventory_page.remove_product_from_cart("Sauce Labs Backpack")
        
        assert inventory_page.get_cart_count() == 1
    
    def test_cart_page_shows_added_items(self, driver):
        inventory_page = self._login_as_standard_user(driver)
        
        inventory_page.add_product_to_cart("Sauce Labs Backpack")
        inventory_page.add_product_to_cart("Sauce Labs Bike Light")
        inventory_page.go_to_cart()
        
        cart_page = CartPage(driver)
        assert cart_page.is_loaded(), "Cart page did not load"
        assert cart_page.get_item_count() == 2
        
        item_names = cart_page.get_item_names()
        assert "Sauce Labs Backpack" in item_names
        assert "Sauce Labs Bike Light" in item_names
    
    def test_complete_checkout_flow(self, driver):
        inventory_page = self._login_as_standard_user(driver)
        
        # add a product
        inventory_page.add_product_to_cart("Sauce Labs Backpack")
        inventory_page.go_to_cart()
        
        # go to checkout
        cart_page = CartPage(driver)
        cart_page.click_checkout()
        
        # fill customer info
        checkout_page = CheckoutPage(driver)
        checkout_page.fill_customer_info("Test", "User", "02115")
        checkout_page.click_continue()
        
        # finish order
        checkout_page.click_finish()
        
        # verify completion
        assert checkout_page.is_order_complete()
        assert "Thank you" in checkout_page.get_completion_message()
    
    def test_checkout_requires_first_name(self, driver):
        inventory_page = self._login_as_standard_user(driver)
        inventory_page.add_product_to_cart("Sauce Labs Backpack")
        inventory_page.go_to_cart()
        
        cart_page = CartPage(driver)
        cart_page.click_checkout()
        
        checkout_page = CheckoutPage(driver)
        # try to continue without filling anything
        checkout_page.click_continue()
        
        assert checkout_page.is_error_displayed()
        assert "First Name is required" in checkout_page.get_error_message()