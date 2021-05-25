from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/selects1.html')
    num1 = browser.find_element_by_xpath('//*[@id="num1"]').text
    num2 = browser.find_element_by_xpath('//*[@id="num2"]').text
    select = Select(browser.find_element_by_tag_name("select"))
    num_sum = int(num1) + int(num2)
    select.select_by_visible_text(str(num_sum))
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    time.sleep(5)
    browser.quit()
