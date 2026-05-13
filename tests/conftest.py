import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(5)
    
    yield driver
    
    # pause for 2 seconds before closing so you can see the final state
    time.sleep(2)
    driver.quit()


@pytest.fixture
def slow_driver(driver):
    """A driver that pauses between actions so you can see what's happening."""
    # monkey-patch the driver to add delays
    original_find = driver.find_element
    
    def slow_find(*args, **kwargs):
        time.sleep(1)  # pause 1 second before finding
        return original_find(*args, **kwargs)
    
    driver.find_element = slow_find
    yield driver