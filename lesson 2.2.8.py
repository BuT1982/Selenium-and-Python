from selenium import webdriver
import time
import os

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/file_input.html')
    imput_first_name = browser.find_element_by_name('firstname')
    imput_first_name.send_keys('Den')
    imput_last_name = browser.find_element_by_name('lastname')
    imput_last_name.send_keys('Morozov')
    imput_email = browser.find_element_by_name('email')
    imput_email.send_keys('den@moro.com')

    # Загрузить файл
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = 'lesson 2.2.8.py'
    file_path = os.path.join(current_dir, file_name)

    # Находим кнопку "Выберите фаил"
    upload = browser.find_element_by_id('file')
    upload.send_keys(file_path)

    # Нажать на кнопку "Submit"
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
