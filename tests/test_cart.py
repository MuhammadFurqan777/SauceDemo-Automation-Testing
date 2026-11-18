
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


PRODUCT_1 = "Sauce Labs Backpack"
PRODUCT_2 = "Sauce Labs Bike Light"


def login_user(driver):

    login = LoginPage(driver)

    login.open_website()

    login.login("standard_user", "secret_sauce")


# TC11: Add multiple products

def test_add_multiple_products(driver):

    login_user(driver)

    inventory = InventoryPage(driver)

    inventory.add_product(PRODUCT_1)

    inventory.add_product(PRODUCT_2)

    assert inventory.get_cart_badge() == "2"


# TC12: Remove product from inventory

def test_remove_product_from_inventory(driver):

    login_user(driver)

    inventory = InventoryPage(driver)

    inventory.add_product(PRODUCT_1)

    inventory.add_product(PRODUCT_2)

    inventory.remove_product(PRODUCT_1)

    assert inventory.get_cart_badge() == "1"


# TC13: Open shopping cart

def test_open_shopping_cart(driver):

    login_user(driver)

    inventory = InventoryPage(driver)

    inventory.add_product(PRODUCT_1)

    inventory.add_product(PRODUCT_2)

    inventory.open_cart()

    assert "cart" in driver.current_url

    cart = CartPage(driver)

    names = cart.get_product_names()

    assert PRODUCT_1 in names

    assert PRODUCT_2 in names


# TC14: Verify cart product details

def test_verify_cart_product_details(driver):

    login_user(driver)

    inventory = InventoryPage(driver)

    inventory.add_product(PRODUCT_1)

    inventory.open_cart()

    cart = CartPage(driver)

    items = cart.get_cart_items()

    assert len(items) == 1

    item = items[0]

    assert cart.get_product_names()[0] == PRODUCT_1

    assert cart.get_product_price(item).startswith("$")

    assert cart.get_product_quantity(item) == "1"

    assert len(cart.get_product_description(item)) > 0


# TC15: Remove product from cart

def test_remove_product_from_cart(driver):

    login_user(driver)

    inventory = InventoryPage(driver)

    inventory.add_product(PRODUCT_1)

    inventory.open_cart()

    cart = CartPage(driver)

    cart.remove_product(PRODUCT_1)

    assert len(cart.get_cart_items()) == 0


# TC16: Continue shopping

def test_continue_shopping(driver):

    login_user(driver)

    inventory = InventoryPage(driver)

    inventory.add_product(PRODUCT_1)

    inventory.open_cart()

    cart = CartPage(driver)

    cart.continue_shopping()

    assert "inventory" in driver.current_url
