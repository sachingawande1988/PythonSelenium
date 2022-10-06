from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
browser = "india"

if browser.lower() == "chrome":
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
else:
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


driver.get("http://www.seleniumframework.com/demo-sites/")

print("Page Title = ", driver.title)
print("Current URL = ", driver.current_url)
print("Page Source = ", driver.page_source)



driver.quit()

