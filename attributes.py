from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
	
try:
    browser = webdriver.Chrome()
    browser.get(link)
    treasurevl = browser.find_element_by_id("treasure")
    x = treasurevl.get_attribute("valuex")
    print(x)
    
    y = calc(x)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    chkbx = browser.find_element_by_id("robotCheckbox").click()
    rdbtn = browser.find_element_by_id("robotsRule").click()
    sbmt = browser.find_element_by_css_selector(".btn").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла