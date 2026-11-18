
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(driver, 10)

    def get_cart_items(self):

        return self.driver.find_elements(
            By.CLASS_NAME, "cart_item"
        )

    def get_product_names(self):

        items = self.get_cart_items()

        return [
            item.find_element(
                By.CLASS_NAME, "inventory_item_name"
            ).text
            for item in items
        ]

    def get_product_price(self, item):

        return item.find_element(
            By.CLASS_NAME, "inventory_item_price"
        ).text

    def get_product_quantity(self, item):

        return item.find_element(
            By.CLASS_NAME, "cart_quantity"
        ).text

    def get_product_description(self, item):

        return item.find_element(
            By.CLASS_NAME, "inventory_item_desc"
        ).text

    def remove_product(self, product_name):

        item = self.driver.find_element(
            By.XPATH,
            f"//div[text()='{product_name}']/ancestor::div[@class='cart_item']"
        )

        item.find_element(
            By.TAG_NAME, "button"
        ).click()

    def continue_shopping(self):

        self.driver.find_element(
            By.ID, "continue-shopping"
        ).click()

    def checkout(self):

        self.wait.until(
            EC.element_to_be_clickable(
                (By.ID, "checkout")
            )
        ).click()
