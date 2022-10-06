from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import service as ChromeService


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


driver.get("http://www.seleniumframework.com/demo-sites/")

print("Page Title = ", driver.title)
print("Current URL = ", driver.current_url)
print("Page Source = ", driver.page_source)



driver.quit()
