from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/execute_script.html')
    # Находим значение переменной X
    x_element = browser.find_element_by_xpath('//*[@id="input_value"]').text
    y = calc(x_element)
    # Вводим значение функции от x
    imput_X = browser.find_element_by_xpath('//*[@id="answer"]')
    imput_X.send_keys(y)

    # Скроллим страницу вниз до кнопки "Submit"
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    # Или скроллим на 100 пикселей
    # browser.execute_script("window.scrollBy(0, 100);")

    # Выбрать checkbox "I'm the robot"
    checkbox = browser.find_element_by_id('robotCheckbox')
    checkbox.click()

    # Переключить radiobutton "Robots rule!".
    radio_button = browser.find_element_by_id('robotsRule')
    radio_button.click()

    # Нажать на кнопку "Submit"
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
