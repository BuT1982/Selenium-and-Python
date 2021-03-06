from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(15)
    browser.get('http://suninjuly.github.io/explicit_wait2.html')

    # Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    # Нажать на кнопку "Book"
    button = browser.find_element_by_id("book")
    button.click()

    # Находим значение переменной X
    x_element = browser.find_element_by_id('input_value').text
    y = calc(x_element)

    # Вводим значение функции от X
    imputX = browser.find_element_by_id('answer')
    # Скроллим до формочки куда вводить значение Х
    browser.execute_script("return arguments[0].scrollIntoView(true);", imputX)
    imputX.send_keys(y)

    button = browser.find_element_by_id('solve')
    button.click()

finally:
    time.sleep(5)
    browser.quit()
