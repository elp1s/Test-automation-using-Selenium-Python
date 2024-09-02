"""
Задание: работа с выпадающим списком
    Напишите код, который реализует следующий сценарий:

    1) Открыть страницу https://suninjuly.github.io/selects1.html
    2) Посчитать сумму заданных чисел
    3) Выбрать в выпадающем списке значение равное расчитанной сумме
    4) Нажать кнопку "Submit"
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Открываем страницу
link = 'https://suninjuly.github.io/selects1.html'

browser = webdriver.Chrome()
browser.get(link)

# Находим элементы с числами
num_1 = int(browser.find_element(By.CSS_SELECTOR, "#num1").text)
num_2 = int(browser.find_element(By.CSS_SELECTOR, "#num2").text)

# Считаем сумму заданных чисел
sum_result = num_1 + num_2

# Выбираем значение из выпадающего списка
select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_visible_text(str(sum_result))

# Нажимаем на кнопку
submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# успеваем скопировать код за 30 секунд
time.sleep(30)

# закрываем браузер после всех манипуляций
browser.quit()
