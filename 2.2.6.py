from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math



try:
    def calc(a):
        return str(math.log(abs(12 * math.sin(int(x)))))

    browser = webdriver.Chrome()
    link = "http://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    x = browser.find_element_by_id('input_value').text
    answer = browser.find_element_by_id('answer')
    answer.send_keys(calc(x))

    not_robot = browser.find_element_by_id('robotCheckbox')
    not_robot.click()

    robots_rule = browser.find_element_by_id('robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", robots_rule)
    robots_rule.click()

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    wait = WebDriverWait(browser, 10)
    alert = wait.until(EC.alert_is_present())
    text = alert.text
    alert.accept()
    print(text)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
