from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    driver = webdriver.Chrome()
    driver.get(link)

    dates = ['Jhon', 'Dow', 'test@test.com']
    fields = driver.find_elements_by_xpath("//input[@required]")
    for i in range(0, len(fields)):
        fields[i].send_keys(dates[i])

    time.sleep(10)
    button = driver.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = driver.find_element_by_tag_name("h1")

    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:

    time.sleep(10)

    driver.quit()

