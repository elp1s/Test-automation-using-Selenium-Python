from part4_lesson3_step3.pages.product_page import ProductPage
import pytest


@pytest.fixture(scope="function")
def browser():
    from selenium import webdriver
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()

    # Получение названия товара и его цены до добавления в корзину
    product_name = page.get_product_name()
    product_price = page.get_product_price()

    page.add_product_to_basket()

    # Проверка корректности сообщений
    page.should_see_success_message_with_product_name(product_name)
    page.should_see_basket_total_equal_to_product_price(product_price)
