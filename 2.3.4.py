from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import math
import time

try:
    def calc(a):
        return str(math.log(abs(12 * math.sin(int(x)))))


    link = ' http://suninjuly.github.io/alert_accept.html'
    driver = webdriver.Chrome()
    driver.get(link)

    button = driver.find_element(By.TAG_NAME, 'button')
    button.click()

    confirm = driver.switch_to.alert
    confirm.accept()

    input_button = driver.find_element(By.ID, 'answer')
    x = driver.find_element(By.ID, 'input_value').text
    input_button.send_keys(calc(int(x)))

    submit = driver.find_element(By.TAG_NAME, 'button')
    submit.click()

    wait = WebDriverWait(driver, 5)
    alert = wait.until(EC.alert_is_present())
    text = alert.text
    alert.accept()
    print(text)

finally:
    time.sleep(10)
    driver.quit()

