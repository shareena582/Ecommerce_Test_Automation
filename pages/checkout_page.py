from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_checkout(self):
        self.wait.until(EC.element_to_be_clickable((By.ID,"checkout"))).click()

    def enter_customer_details(self, first_name, last_name, postal_code):
        self.wait.until(EC.visibility_of_element_located((By.ID,"first-name"))).send_keys(first_name)
        self.wait.until(EC.visibility_of_element_located((By.ID,"last-name"))).send_keys(last_name)
        self.wait.until(EC.visibility_of_element_located((By.ID,"postal-code"))).send_keys(postal_code)

    def click_continue(self):
        self.wait.until(EC.element_to_be_clickable((By.ID,"continue"))).click()
        print("URL AFTER CONTINUE:", self.driver.current_url)


    def click_finish(self):
        self.wait.until(EC.element_to_be_clickable((By.ID,"finish"))).click()
 

    def get_confirmation_message(self):

        return self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"complete-header"))).text