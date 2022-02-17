from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import os



try:

    link = 'http://suninjuly.github.io/file_input.html'
    driver = webdriver.Chrome()
    driver.get(link)

    file = 'get.txt'
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, file)

    first_name = driver.find_element(By.NAME, 'firstname')
    last_name = driver.find_element(By.NAME, 'lastname')
    email = driver.find_element(By.NAME, 'email')
    attach_button = driver.find_element(By.ID, 'file')
    submit = driver.find_element(By.TAG_NAME, 'button')

    first_name.send_keys('jane')
    last_name.send_keys('dow')
    email.send_keys('test@test.com')
    attach_button.send_keys(file_path)
    submit.click()

    wait = WebDriverWait(driver, 5)
    alert = wait.until(EC.alert_is_present())
    text = alert.text
    alert.accept()
    print(text)

finally:
    time.sleep(5)
    driver.quit()



