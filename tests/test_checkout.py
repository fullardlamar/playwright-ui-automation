import os
import sys

from playwright.sync_api import sync_playwright

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.config import USERNAME, PASSWORD, FIRST_NAME, LAST_NAME, POSTAL_CODE


def test_checkout_completion():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        login_page = LoginPage(page)
        inventory_page = InventoryPage(page)
        cart_page = CartPage(page)

        login_page.navigate()
        login_page.login(USERNAME, PASSWORD)

        assert inventory_page.is_inventory_page_loaded()

        inventory_page.add_backpack_to_cart()
        inventory_page.open_cart()

        assert cart_page.is_cart_page_loaded()

        cart_page.click_checkout()
        cart_page.fill_checkout_information(FIRST_NAME, LAST_NAME, POSTAL_CODE)
        cart_page.finish_checkout()

        assert cart_page.is_checkout_complete()

        browser.close()