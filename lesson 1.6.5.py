from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/find_link_text')
    link = browser.find_element_by_partial_link_text("224592")
    link.click()

    # заполняем форму регистрации
    input1 = browser.find_element(By.XPATH, '/html/body/div/form/div[1]/input')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name('last_name')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name('form-control.city')
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id('country')
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
