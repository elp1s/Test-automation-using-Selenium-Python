"""
Задание: кликаем по checkboxes и radiobuttons (капча для роботов)
    Ваша программа должна выполнить следующие шаги:

    1) Открыть страницу https://suninjuly.github.io/math.html.
    2) Считать значение для переменной x.
    3) Посчитать математическую функцию от x (код для этого приведён ниже).
    4) Ввести ответ в текстовое поле.
    5) Отметить checkbox "I'm the robot".
    6) Выбрать radiobutton "Robots rule!".
    7) Нажать на кнопку Submit.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


# Вычисляем математическую функцию от x
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


# Открываем страницу
link = "https://suninjuly.github.io/math.html"

browser = webdriver.Chrome()
browser.get(link)

# Считываем значение для переменной x
x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
x = x_element.text

y = calc(x)

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
# закрываем браузер после всех манипуляций
browser.quit()
