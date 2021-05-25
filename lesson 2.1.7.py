from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/get_attribute.html')
    # Найти элемент-картинку, который является изображением сундука с сокровищами.
    image = browser.find_element_by_xpath('//*[@id="treasure"]')
    # Взять у этого элемента значение атрибута valuex, которое является значением x для задачи
    img_int = image.get_attribute('valuex')
    y = calc(img_int)
    # Ввести ответ в текстовое поле
    input1 = browser.find_element_by_xpath('//*[@id="answer"]')
    input1.send_keys(y)
    # Отметить checkbox "I'm the robot"
    option1 = browser.find_element_by_xpath('//*[@id="robotCheckbox"]')
    option1.click()
    # Выбрать radiobutton "Robots rule!"
    option1 = browser.find_element_by_xpath('//*[@id="robotsRule"]')
    option1.click()
    # Нажать на кнопку "Submit"
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
