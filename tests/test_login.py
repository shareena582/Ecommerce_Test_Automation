import pytest
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from data.test_data import(
    VALID_USERNAME,VALID_PASSWORD
)




def test_valid_login(driver):

    login_page = LoginPage(driver)
    login_page.login(VALID_USERNAME, VALID_PASSWORD)

    assert "inventory" in driver.current_url

@pytest.mark.parametrize(
        "username, password",
        [
            ("wrong_user", "wrong_password"),
            ("standard_user", "wrong_password"),
            ("wrong_user","secret_sauce"),
        ]
)

def test_invalid_login(driver,username,password):

    login_page = LoginPage(driver)
    login_page.login(username,password)

    error = driver.find_element(By.CSS_SELECTOR,"h3[data-test='error']")

    assert error.text == (
        "Epic sadface: Username and password do not match any user in this service"
    )

# def test_add_product_to_cart(driver):

#     login_page = LoginPage(driver)
#     login_page.login("standard_user","secret_sauce")

#     inventory_page = InventoryPage(driver)
#     inventory_page.add_backpack_to_cart()
#     cart_count = inventory_page.get_cart_count()
#     assert cart_count == "1"


# def test_verify_cart(driver):
    
#     login_page = LoginPage(driver)
#     login_page.login("standard_user","secret_sauce")

#     inventory_page = InventoryPage(driver)
#     inventory_page.add_backpack_to_cart()

#     cart_page = CartPage(driver)
#     cart_page.open_cart()

#     product_name = cart_page.get_product_name()

#     assert product_name == "Sauce Labs Backpack"
  

# def test_complete_checkout(driver):

  
#     login_page = LoginPage(driver)
#     login_page.login("standard_user","secret_sauce")

#     inventory_page = InventoryPage(driver)
#     inventory_page.add_backpack_to_cart()
    
#     cart_page = CartPage(driver)
#     cart_page.open_cart()

#     checkout_page = CheckoutPage(driver)
#     checkout_page.click_checkout()

#     checkout_page.enter_customer_details("shareena", "Tester", "00000")

#     checkout_page.click_continue()
    
#     checkout_page.click_finish()
    
#     confirmation = checkout_page.get_confirmation_message()
#     assert confirmation == "Thank you for your order!"
    





