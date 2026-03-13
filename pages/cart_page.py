class CartPage:

    def __init__(self, page):
        self.page = page
        self.cart_list = ".cart_list"
        self.checkout_button = "#checkout"
        self.first_name_input = "#first-name"
        self.last_name_input = "#last-name"
        self.postal_code_input = "#postal-code"
        self.continue_button = "#continue"
        self.finish_button = "#finish"
        self.complete_header = ".complete-header"

    def is_cart_page_loaded(self):
        return self.page.locator(self.cart_list).is_visible()

    def click_checkout(self):
        self.page.click(self.checkout_button)

    def fill_checkout_information(self, first_name, last_name, postal_code):
        self.page.fill(self.first_name_input, first_name)
        self.page.fill(self.last_name_input, last_name)
        self.page.fill(self.postal_code_input, postal_code)
        self.page.click(self.continue_button)

    def finish_checkout(self):
        self.page.click(self.finish_button)

    def is_checkout_complete(self):
        return self.page.locator(self.complete_header).is_visible()