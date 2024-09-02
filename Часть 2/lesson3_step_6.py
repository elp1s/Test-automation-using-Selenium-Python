""""
Задание: переход на новую вкладку
    Сценарий для реализации выглядит так:

    1) Открыть страницу http://suninjuly.github.io/redirect_accept.html
    2) Нажать на кнопку
    3) Переключиться на новую вкладку
    4) Пройти капчу для робота и получить число-ответ
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


# Открываем страницу
link = 'http://suninjuly.github.io/redirect_accept.html'

browser = webdriver.Chrome()
browser.get(link)

# Нажимаем на кнопку Submit
browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# Переключаемся на новую вкладку
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

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
