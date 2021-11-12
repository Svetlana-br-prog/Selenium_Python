from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/math.html"

browser = webdriver.Chrome()
browser.get(link)


try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(calc(x))
    checkbox1 = browser.find_element_by_id("robotCheckbox")
    checkbox1.click()
    radiobutton1 = browser.find_element_by_css_selector("[value='robots']")
    radiobutton1.click()
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()