from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


driver.get("http://www.seleniumframework.com/demo-sites/")
driver.save_screenshot("trial.jpeg")
print("Page Title = ", driver.title)
print("Current URL = ", driver.current_url)
print("Page Source = ", driver.page_source)



driver.quit()

