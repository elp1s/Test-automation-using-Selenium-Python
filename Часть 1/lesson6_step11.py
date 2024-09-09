"""
Задание:
    1) Тест успешно проходит на странице http://suninjuly.github.io/registration1.html
    2) Тест падает с ошибкой NoSuchElementException http://suninjuly.github.io/registration2.html
    3) Используемые селекторы должны быть уникальны
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Код, который заполняет обязательные поля
    browser.find_element_by_css_selector('div.first_block input.first').send_keys('Sergey')
    browser.find_element_by_css_selector('div.first_block input.second').send_keys('Konoplev')
    browser.find_element_by_css_selector('div.first_block input.third').send_keys('fgbdb@mail.ru')

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
