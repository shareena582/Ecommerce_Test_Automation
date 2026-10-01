import pytest 
from selenium import webdriver
from pages.login_page import LoginPage
import os
# from data.test_data import VALID_USERNAME,VALID_PASSWORD

@pytest.fixture
def driver():

    driver = webdriver.Chrome()
    driver.get("http://www.saucedemo.com")
    yield driver
    driver.quit()

@pytest.fixture
def logged_in_driver(driver):
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    return driver

def pytest_runtest_makereport(item, call):
    if call.when == "call" and call.excinfo is not None:
        driver = item.funcargs.get("driver")
        if driver:
            os.makedirs("screenshots",exist_ok=True)
            test_name = item.name
            driver.save_screenshot(
                f"screenshots/{test_name}.png"
            )