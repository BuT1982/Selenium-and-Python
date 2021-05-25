from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/math.html')
    x_element = browser.find_element(By.XPATH, '//*[@id="input_value"]').text
    y = calc(x_element)
    input1 = browser.find_element(By.XPATH, '//*[@id="answer"]')
    input1.send_keys(y)

    option1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
    option1.click()

    option1 = browser.find_element_by_css_selector("[for='robotsRule']")
    option1.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    time.sleep(10)
    browser.quit()
