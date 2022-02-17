from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import os
import math

try:
    def calc(a):
        return str(math.log(abs(12 * math.sin(int(x)))))

    link = 'http://suninjuly.github.io/explicit_wait2.html'
    driver = webdriver.Chrome()
    driver.get(link)

    wait = WebDriverWait(driver, 12)
    price100 = wait.until(EC.text_to_be_present_in_element((By.ID,  'price'), '$100'))
    book = driver.find_element(By.ID, 'book')
    book.click()

    input_field = driver.find_element(By.ID, 'answer')
    x = driver.find_element(By.ID, 'input_value').text
    input_field.send_keys(calc(x))

    submit_button = driver.find_element(By.ID, 'solve')
    submit_button.click()

    alert = wait.until(EC.alert_is_present())
    text = alert.text
    alert.accept()
    print(text)
finally:
    time.sleep(5)
    driver.quit()

