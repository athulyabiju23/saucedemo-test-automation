from selenium.webdriver.common.by import By


def test_successful_login(driver):
    # navigate to saucedemo
    driver.get("https://www.saucedemo.com/")
    
    # find username and password fields
    username_field = driver.find_element(By.ID, "user-name")
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")
    
    # enter credentials
    username_field.send_keys("standard_user")
    password_field.send_keys("secret_sauce")
    
    # click login
    login_button.click()
    
    # verify we landed on the inventory page
    assert "inventory.html" in driver.current_url
    
    # verify the products header is visible
    products_header = driver.find_element(By.CLASS_NAME, "title")
    assert products_header.text == "Products"