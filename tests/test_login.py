import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
import time

class TestLogin:
    """Login functionality tests for saucedemo.com"""
    
    def test_successful_login_with_valid_credentials(self, driver):
        login_page = LoginPage(driver)
        login_page.load()
        #time.sleep(5)
        login_page.login("standard_user", "secret_sauce")
        #time.sleep(5)
        inventory_page = InventoryPage(driver)
        assert inventory_page.is_loaded(), "Inventory page did not load after login"
        assert inventory_page.get_page_title() == "Products"
    
    def test_login_fails_with_locked_user(self, driver):
        login_page = LoginPage(driver)
        login_page.load()
        #time.sleep(5)
        login_page.login("locked_out_user", "secret_sauce")
        #time.sleep(5)
        
        assert login_page.is_error_displayed(), "Expected error message for locked user"
        error_text = login_page.get_error_message()
        assert "locked out" in error_text.lower(), f"Unexpected error: {error_text}"
    
    def test_login_fails_with_wrong_password(self, driver):
        login_page = LoginPage(driver)
        login_page.load()
        #time.sleep(5)
        login_page.login("standard_user", "wrong_password_123")
        #time.sleep(5)
        assert login_page.is_error_displayed(), "Expected error message for wrong password"
        error_text = login_page.get_error_message()
        assert "username and password do not match" in error_text.lower()
    
    def test_login_fails_with_empty_credentials(self, driver):
        login_page = LoginPage(driver)
        login_page.load()
        #time.sleep(5)
        login_page.click_login()  # click login without entering anything
        #time.sleep(5)
        assert login_page.is_error_displayed(), "Expected error for empty credentials"
        error_text = login_page.get_error_message()
        assert "username is required" in error_text.lower()
    
    @pytest.mark.parametrize("username,password,expected_error", [
        ("", "secret_sauce", "username is required"),
        ("standard_user", "", "password is required"),
        ("invalid_user", "invalid_pass", "username and password do not match"),
    ])
    def test_login_negative_scenarios(self, driver, username, password, expected_error):
        login_page = LoginPage(driver)
        login_page.load()
        #time.sleep(5)
        login_page.login(username, password) if password else login_page.enter_username(username)
        if not password:
            login_page.click_login()
        #time.sleep(5)
        assert login_page.is_error_displayed()
        assert expected_error in login_page.get_error_message().lower()