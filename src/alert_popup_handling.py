# Changed to show git commit and push
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


driver.maximize_window()
time.sleep(2)
driver.get("http://demo.guru99.com/test/delete_customer.php")
time.sleep(2)
driver.find_element(By.NAME, "cusid").send_keys("53920")
time.sleep(2)
driver.find_element(By.NAME, "submit").submit()
time.sleep(2)
alert = driver.switch_to.alert
time.sleep(2)
alert_message = alert.text
time.sleep(2)
print("ALERT TEXT = ", alert_message)
time.sleep(2)
alert.accept()
time.sleep(2)
driver.quit()
