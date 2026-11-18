
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def login_user(driver):

    login = LoginPage(driver)

    login.open_website()

    login.login("standard_user", "secret_sauce")


# TC08: Verify inventory page and products

def test_inventory_page(driver):

    login_user(driver)

    inventory = InventoryPage(driver)

    names = inventory.get_product_names()

    assert "inventory" in driver.current_url

    assert len(names) > 0


# TC09: Sort products A to Z

def test_sort_products_az(driver):

    login_user(driver)

    inventory = InventoryPage(driver)

    inventory.sort_products("az")

    names = inventory.get_product_names()

    assert names == sorted(names)


# TC10: Sort products Z to A

def test_sort_products_za(driver):

    login_user(driver)

    inventory = InventoryPage(driver)

    inventory.sort_products("za")

    names = inventory.get_product_names()

    assert names == sorted(names, reverse=True)
