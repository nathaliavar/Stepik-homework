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

    link = 'http://suninjuly.github.io/redirect_accept.html'
    driver = webdriver.Chrome()
    driver.get(link)

    button = driver.find_element(By.CLASS_NAME, 'trollface')
    button.click()
    driver.switch_to.window(driver.window_handles[1])

    input_field = driver.find_element(By.ID, 'answer')
    x = driver.find_element(By.ID,'input_value').text
    input_field.send_keys(calc(x))

    button_submit = driver.find_element(By.TAG_NAME, 'button')
    button_submit.click()

    wait = WebDriverWait(driver, 5)
    alert = wait.until(EC.alert_is_present())
    text = alert.text
    alert.accept()
    print(text)

finally:
    time.sleep(5)
    driver.quit()



