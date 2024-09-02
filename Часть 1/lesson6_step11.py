from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/registration2.html"


browser = webdriver.Chrome()
browser.get(link)

browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']").send_keys("Имя")
browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']").send_keys("Фамилия")
browser.find_element(By.XPATH, "//input[@placeholder='Input your email']").send_keys("email@example.com")

button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
button.click()


# успеваем скопировать код за 30 секунд
time.sleep(30)
# закрываем браузер после всех манипуляций
browser.quit()


