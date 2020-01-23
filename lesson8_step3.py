from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects2.html"
#def calc(x):
 #   return str(math.log(abs(12*math.sin(int(x)))))
	
try:
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element_by_id("num1").text
    y = browser.find_element_by_id("num2").text
    
    print(x)
    print(y)
    num1 = int(x)
    num2 = int(y)
    sum = num1 + num2
    print(sum)
    sumstr = str(sum)
    
    select = Select(browser.find_element_by_tag_name("select"))
    #select.select_by_value(sumstr)
    select.select_by_visible_text(sumstr)
    sbmt = browser.find_element_by_css_selector(".btn").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла