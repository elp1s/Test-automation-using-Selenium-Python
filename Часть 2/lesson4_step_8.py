""""
Задание: ждем нужный текст на странице
    В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:

    1) Открыть страницу http://suninjuly.github.io/explicit_wait2.html
    2) Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
    3) Нажать на кнопку "Book"
    4) Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
Чтобы определить момент, когда цена аренды уменьшится до $100, используйте метод text_to_be_present_in_element из библиотеки expected_conditions.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


# Открываем браузер
link = 'http://suninjuly.github.io/explicit_wait2.html'
browser = webdriver.Chrome()
browser.get(link)

# Ждем, пока цена не станет $100 (ожидание не менее 12 секунд)
WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))

browser.find_element(By.ID, "book").click()

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
