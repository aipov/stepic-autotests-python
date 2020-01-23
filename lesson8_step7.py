from selenium import webdriver
import time 
import os 


try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    firstName = browser.find_element_by_name("firstname")
    firstName.send_keys("Ben")
    secondName = browser.find_element_by_name("lastname")
    secondName.send_keys("Jonson")
    email = browser.find_element_by_name("email")
    email.send_keys("Jonson@mail.com")
    sndfl = browser.find_element_by_name("file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    sndfl.send_keys(file_path)
    sbmtbttn = browser.find_element_by_css_selector(".btn").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()