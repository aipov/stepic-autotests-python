from selenium.webdriver import Firefox
import time

driver = Firefox()
driver.get("https://selenium.dev")
doc = driver.find_element_by_css_selector("nav#navbar a[href='/documentation']")
doc.click()
time.sleep(3)
webInList = driver.find_element_by_xpath("//li[@title='WebDriver']/a")
webInList.click()
#final = driver.find_element_by_css_selector("h1#webdriver")
#assert final == "WebDriver"

driver.quit()

