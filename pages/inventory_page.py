
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(driver, 10)

    def get_product_names(self):

        self.wait.until(
            EC.presence_of_all_elements_located(
                (By.CLASS_NAME, "inventory_item_name")
            )
        )

        products = self.driver.find_elements(
            By.CLASS_NAME, "inventory_item_name"
        )

        return [product.text for product in products]

    def sort_products(self, option):

        dropdown = self.wait.until(
            EC.element_to_be_clickable(
                (By.CLASS_NAME, "product_sort_container")
            )
        )

        Select(dropdown).select_by_value(option)

    def add_product(self, product_name):

        product = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH,
                 f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']")
            )
        )

        button = product.find_element(
            By.CSS_SELECTOR, "button.btn_inventory"
        )

        button.click()

    def remove_product(self, product_name):

        product = self.driver.find_element(
            By.XPATH,
            f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']"
        )

        product.find_element(
            By.CSS_SELECTOR, "button.btn_inventory"
        ).click()

    def get_cart_badge(self):

        badges = self.driver.find_elements(
            By.CLASS_NAME, "shopping_cart_badge"
        )

        if badges:
            return badges[0].text

        return "0"

    def open_cart(self):

        self.driver.find_element(
            By.CLASS_NAME, "shopping_cart_link"
        ).click()
