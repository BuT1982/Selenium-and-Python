from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/redirect_accept.html')

    button = browser.find_element_by_css_selector('button.btn')
    button.click()

    # запомнаем имя текущей вкладки и новой
    first_window = browser.window_handles[0]
    new_window = browser.window_handles[1]

    # переходим на новую вкладку
    browser.switch_to.window(new_window)

    # Находим значение переменной X
    x_element = browser.find_element_by_id('input_value').text
    y = calc(x_element)

    # Вводим значение функции от X
    imputX = browser.find_element_by_id('answer')
    imputX.send_keys(y)

    button = browser.find_element_by_css_selector('button.btn')
    button.click()

finally:
    time.sleep(5)
    browser.quit()
