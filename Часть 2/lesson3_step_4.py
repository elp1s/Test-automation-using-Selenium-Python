""""
Задание: принимаем alert
    В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:

    1) Открыть страницу http://suninjuly.github.io/alert_accept.html
    2) Нажать на кнопку
    3) Принять confirm
    4) На новой странице решить капчу для роботов, чтобы получить число с ответом
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


# Открываем страницу
link = 'http://suninjuly.github.io/alert_accept.html'

browser = webdriver.Chrome()
browser.get(link)

# Нажимаем на кнопку Submit
browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# Принять confirm
alert = browser.switch_to.alert
alert.accept()

# Считываем значение для переменной x
x = int(browser.find_element(By.CSS_SELECTOR, '#input_value').text)
y = calc(x)

# Вводим ответ в текстовое поле
browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)

# Нажимаем на кнопку Submit
browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# успеваем скопировать код за 30 секунд
time.sleep(30)

# Закрываем браузер после выполнения
browser.quit()
