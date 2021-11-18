from selenium import webdriver
import time
import math

link = "http://SunInJuly.github.io/execute_script.html"

browser = webdriver.Chrome()
browser.get(link)

try:
    def fun(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(fun(x))
    browser.execute_script("window.scrollBy(0, 150);")
    checkbox1 = browser.find_element_by_id("robotCheckbox").click()
    radiobutton1 = browser.find_element_by_id("robotsRule").click()
    button = browser.find_element_by_tag_name("button").click()
    # чтобы кликнуть на перекрытую кнопку

finally:
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()