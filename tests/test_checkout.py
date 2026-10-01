# from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


from data.test_data import (
    FIRST_NAME,
    LAST_NAME,
    POSTAL_CODE
)

def test_complete_checkout(logged_in_driver):

     # login_page = LoginPage(driver)
     # login_page.login("standard_user","secret_sauce")
     
     # print("FIRST_NAME:", FIRST_NAME)
     # print("LAST_NAME:", LAST_NAME)
     # print("POSTAL_CODE:", POSTAL_CODE)


     inventory_page = InventoryPage(logged_in_driver)
     inventory_page.add_backpack_to_cart()

     cart_page = CartPage(logged_in_driver)
     cart_page.open_cart()

     checkout_page = CheckoutPage(logged_in_driver)
     checkout_page.click_checkout()

     checkout_page.enter_customer_details(FIRST_NAME, LAST_NAME, POSTAL_CODE)
     checkout_page.click_continue()
     checkout_page.click_finish()
     confirmation = checkout_page.get_confirmation_message()
     assert confirmation == "Thank you for your order!"
    
