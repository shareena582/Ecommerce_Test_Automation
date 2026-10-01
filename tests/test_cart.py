# from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

def test_add_product_to_cart(logged_in_driver):

    # login_page = LoginPage(driver)
    # login_page.login("standard_user", "secret_sauce")
                     
    inventory_page = InventoryPage(logged_in_driver)
    inventory_page.add_backpack_to_cart()
    cart_count = inventory_page.get_cart_count()
    assert cart_count == "1"


def test_verify_cart(logged_in_driver):

    # login_page = LoginPage(logged_in_driver)
    # login_page.login("standard_user", "secret_sauce")
                         
    inventory_page = InventoryPage(logged_in_driver)
    inventory_page.add_backpack_to_cart()

    cart_page = CartPage(logged_in_driver)
    cart_page.open_cart()
    
    product_name = cart_page.get_product_name()
    assert product_name == "Sauce Labs Backpack"

