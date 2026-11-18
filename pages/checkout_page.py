
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(driver, 10)

    def enter_information(self, first_name, last_name, postal_code):

        self.wait.until(
            EC.visibility_of_element_located(
                (By.ID, "first-name")
            )
        )

        self.driver.find_element(
            By.ID, "first-name"
        ).send_keys(first_name)

        self.driver.find_element(
            By.ID, "last-name"
        ).send_keys(last_name)

        self.driver.find_element(
            By.ID, "postal-code"
        ).send_keys(postal_code)

        self.driver.find_element(
            By.ID, "continue"
        ).click()

    def get_error_message(self):

        error = self.wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "[data-test='error']")
            )
        )

        return error.text

    def get_subtotal(self):

        return self.driver.find_element(
            By.CLASS_NAME, "summary_subtotal_label"
        ).text

    def get_tax(self):

        return self.driver.find_element(
            By.CLASS_NAME, "summary_tax_label"
        ).text

    def get_total(self):

        return self.driver.find_element(
            By.CLASS_NAME, "summary_total_label"
        ).text

    def finish_order(self):

        self.driver.find_element(
            By.ID, "finish"
        ).click()

    def get_confirmation_message(self):

        return self.wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "complete-header")
            )
        ).text

    def back_home(self):

        self.driver.find_element(
            By.ID, "back-to-products"
        ).click()
