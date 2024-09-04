from selenium.webdriver.common.by import By
from .base_page import BasePage


class ProductPage(BasePage):
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success .alertinner strong")
    BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner p .price_color")

    def add_product_to_basket(self):
        add_button = self.browser.find_element(*self.ADD_TO_BASKET_BUTTON)
        add_button.click()
        self.solve_quiz_and_get_code()

    def get_product_name(self):
        return self.browser.find_element(*self.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*self.PRODUCT_PRICE).text

    def should_see_success_message_with_product_name(self, product_name):
        success_message = self.browser.find_element(*self.SUCCESS_MESSAGE).text
        assert product_name == success_message, f"Expected product name '{product_name}' but got '{success_message}'"

    def should_see_basket_total_equal_to_product_price(self, product_price):
        basket_total = self.browser.find_element(*self.BASKET_TOTAL).text
        assert product_price == basket_total, f"Expected basket total '{product_price}' but got '{basket_total}'"
