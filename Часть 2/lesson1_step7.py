"""
Задание: поиск сокровища с помощью get_attribute
    Ваша программа должна:

    1) Открыть страницу http://suninjuly.github.io/get_attribute.html.
    2) Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
    3) Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
    4) Посчитать математическую функцию от x (сама функция остаётся неизменной).
    5) Ввести ответ в текстовое поле.
    6) Отметить checkbox "I'm the robot".
    7) Выбрать radiobutton "Robots rule!".
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
link = " http://suninjuly.github.io/get_attribute.html"

browser = webdriver.Chrome()
browser.get(link)

# Находим элемент-картинку с сундуком и получаем значение атрибута valuex
treasure = browser.find_element(By.CSS_SELECTOR, "img#treasure")
x = treasure.get_attribute("valuex")

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
