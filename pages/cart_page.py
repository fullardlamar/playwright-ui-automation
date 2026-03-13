class CartPage:

    def __init__(self, page):
        self.page = page
        self.cart_list = ".cart_list"

    def is_cart_page_loaded(self):
        return self.page.locator(self.cart_list).is_visible()