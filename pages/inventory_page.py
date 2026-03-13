class InventoryPage:

    def __init__(self, page):
        self.page = page
        self.inventory_list = ".inventory_list"
        self.add_to_cart_backpack = "#add-to-cart-sauce-labs-backpack"
        self.cart_link = ".shopping_cart_link"

    def is_inventory_page_loaded(self):
        return self.page.locator(self.inventory_list).is_visible()

    def add_backpack_to_cart(self):
        self.page.click(self.add_to_cart_backpack)

    def open_cart(self):
        self.page.click(self.cart_link)