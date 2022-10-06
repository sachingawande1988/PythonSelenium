from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get(r"C:\Users\sachin-gawande\Downloads\chromedriver_win32\chromedriver.exe")

driver.get("http://www.seleniumframework.com/demo-sites/")

driver.refresh()

time.sleep(2)

driver.find_element(By.XPATH, value="//a[@href='http://www.seleniumframework.com/introduction/']").click()

time.sleep(2)

driver.find_element(By.LINK_TEXT, value="PYTHON").click()

time.sleep(2)

driver.back()

time.sleep(2)

driver.forward()

time.sleep(2)

driver.quit()