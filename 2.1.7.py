from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    value = browser.find_element_by_id('treasure')
    v = value.get_attribute("valuex")
    input_field = browser.find_element_by_id('answer')
    input_field.send_keys(calc(v))

    check = browser.find_element_by_id("robotCheckbox")
    check.click()

    radio = browser.find_element_by_id("robotsRule")
    radio.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(5)
    wait = WebDriverWait(browser, 10)
    alert = wait.until(EC.alert_is_present())
    text = alert.text
    alert.accept()

finally:
    time.sleep(10)
    browser.quit()
