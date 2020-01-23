from selenium import webdriver
import time 
import math
from math import log, sin

link = "http://suninjuly.github.io/execute_script.html"

def calc(x):
  return str(math.log(abs(12*sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    print(x)
    y = calc(x)
    print(y)
	
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    chkbx = browser.find_element_by_id("robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", chkbx)
    chkbx.click()
    rdbtn = browser.find_element_by_id("robotsRule").click()
    sbmt = browser.find_element_by_css_selector(".btn").click()
	

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
