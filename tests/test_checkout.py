
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


PRODUCT = "Sauce Labs Backpack"


def open_checkout(driver):

    login = LoginPage(driver)

    login.open_website()

    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)

    inventory.add_product(PRODUCT)

    inventory.open_cart()

    cart = CartPage(driver)

    cart.checkout()

    return CheckoutPage(driver)


# TC17: Open checkout page

def test_open_checkout(driver):

    checkout = open_checkout(driver)

    assert "checkout-step-one" in driver.current_url


# TC18: Checkout with empty form

def test_checkout_empty_form(driver):

    checkout = open_checkout(driver)

    checkout.enter_information("", "", "")

    assert checkout.get_error_message() == (
        "Error: First Name is required"
    )


# TC19: Missing first name

def test_missing_first_name(driver):

    checkout = open_checkout(driver)

    checkout.enter_information("", "Salman", "75500")

    assert checkout.get_error_message() == (
        "Error: First Name is required"
    )


# TC20: Missing last name

def test_missing_last_name(driver):

    checkout = open_checkout(driver)

    checkout.enter_information("Furqan", "", "75500")

    assert checkout.get_error_message() == (
        "Error: Last Name is required"
    )


# TC21: Missing postal code

def test_missing_postal_code(driver):

    checkout = open_checkout(driver)

    checkout.enter_information("Furqan", "Salman", "")

    assert checkout.get_error_message() == (
        "Error: Postal Code is required"
    )


# TC22: Valid checkout information

def test_valid_checkout_information(driver):

    checkout = open_checkout(driver)

    checkout.enter_information(
        "Furqan", "Salman", "75500"
    )

    assert "checkout-step-two" in driver.current_url


# TC23: Verify checkout overview totals

def test_checkout_overview(driver):

    checkout = open_checkout(driver)

    checkout.enter_information(
        "Furqan", "Salman", "75500"
    )

    subtotal_text = checkout.get_subtotal()

    tax_text = checkout.get_tax()

    total_text = checkout.get_total()

    subtotal = float(subtotal_text.split("$")[1])

    tax = float(tax_text.split("$")[1])

    total = float(total_text.split("$")[1])

    assert subtotal > 0

    assert tax > 0

    assert round(subtotal + tax, 2) == total


# TC24: Finish order

def test_finish_order(driver):

    checkout = open_checkout(driver)

    checkout.enter_information(
        "Furqan", "Salman", "75500"
    )

    checkout.finish_order()

    assert checkout.get_confirmation_message() == (
        "Thank you for your order!"
    )


# TC25: Back Home after order completion

def test_back_home(driver):

    checkout = open_checkout(driver)

    checkout.enter_information(
        "Furqan", "Salman", "75500"
    )

    checkout.finish_order()

    checkout.back_home()

    assert "inventory" in driver.current_url


# TC26: Logout

def test_logout(driver):

    login = LoginPage(driver)

    login.open_website()

    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)

    # Open navigation menu

    driver.find_element(
        "id", "react-burger-menu-btn"
    ).click()

    # Click logout

    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By

    logout_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.ID, "logout_sidebar_link")
        )
    )

    logout_button.click()

    assert driver.current_url.rstrip("/") == (
        "https://www.saucedemo.com"
    )
