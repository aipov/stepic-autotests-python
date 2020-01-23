from selenium import webdriver
from selenium.webdriver.common.by import By
import time 


link = "http://suninjuly.github.io/simple_form_find_task.html"
browser = webdriver.Chrome()
browser.get(link)
input1 = browser.find_element_by_tag_name("first_name")
input1.send_keys("Ivan")
time.sleep(30)
button = browser.find_element(By.ID, "submit_button")
button.click()

# закрываем браузер после всех манипуляций
browser.quit()