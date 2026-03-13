from playwright.sync_api import Page

def test_checkout_navigation(page: Page):
    page.goto("https://www.saucedemo.com/")
    
    # login
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

    # verify inventory page loaded
    assert page.locator(".inventory_list").is_visible()

    # click first item
    page.click(".inventory_item:first-child button")

    # go to cart
    page.click(".shopping_cart_link")

    # verify cart page
    assert page.locator(".cart_list").is_visible()