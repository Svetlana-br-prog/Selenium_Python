from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/selects1.html"

browser = webdriver.Chrome()
browser.get(link)

try:
    def sum(x, y):
        return str(int(x) + int(y))


    x_element = browser.find_element_by_id("num1")
    x = x_element.text
    x1_element = browser.find_element_by_id("num2")
    x1 = x1_element.text
    browser.find_element_by_id("dropdown").click()
    browser.find_element(By.CSS_SELECTOR, f'option[value="{sum(x,x1)}"]').click()
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()