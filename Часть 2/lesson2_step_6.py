"""
Задание на execute_script
    Вам потребуется написать код, чтобы:

    1) Открыть страницу https://SunInJuly.github.io/execute_script.html.
    2) Считать значение для переменной x.
    3) Посчитать математическую функцию от x.
    4) Проскроллить страницу вниз.
    5) Ввести ответ в текстовое поле.
    6) Выбрать checkbox "I'm the robot".
    7) Переключить radiobutton "Robots rule!".
    8) Нажать на кнопку "Submit".
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


# Вычисляем математическую функцию от x
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


# Открываем страницу
link = 'https://SunInJuly.github.io/execute_script.html'

browser = webdriver.Chrome()
browser.get(link)

# Считываем значение для переменной x
x = int(browser.find_element(By.CSS_SELECTOR, '#input_value').text)

y = calc(x)

# Прокручиваем страницу вниз
browser.execute_script("window.scrollBy(0, 100);")

# Вводим ответ в текстовое поле
input_field = browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)

# Отмечаем checkbox "I'm the robot"
checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()

# Выбираем radiobutton "Robots rule!"
radiobutton = browser.find_element(By.CSS_SELECTOR, "#robotsRule").click()

# Нажимаем на кнопку Submit
submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# успеваем скопировать код за 30 секунд
time.sleep(30)

# Закрываем браузер после выполнения
browser.quit()
