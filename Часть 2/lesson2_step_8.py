"""
Задание: загрузка файла
    Напишите скрипт, который будет выполнять следующий сценарий:

    1) Открыть страницу http://suninjuly.github.io/file_input.html
    2) Заполнить текстовые поля: имя, фамилия, email
    3) Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
    4) Нажать кнопку "Submit"
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

# Загружаем файл
with open("selenium.txt", "w") as file:
    pass

mydir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(mydir, "selenium.txt")

# Открываем браузер
link = 'http://suninjuly.github.io/file_input.html'
browser = webdriver.Chrome()
browser.get(link)

# Заполняем данные
browser.find_element(By.NAME, "firstname").send_keys('Имя')
browser.find_element(By.NAME, "lastname").send_keys("Фамилия")
browser.find_element(By.NAME, "email").send_keys("email@exp.com")
browser.find_element(By.XPATH, "//input[@id='file']").send_keys(file_path)


# Нажимаем кнопку "Submit"
browser.find_element(By.CSS_SELECTOR, 'button.btn').click()

# успеваем скопировать код за 30 секунд
time.sleep(10)

# закрываем браузер после всех манипуляций
browser.quit()

os.remove(file_path)
