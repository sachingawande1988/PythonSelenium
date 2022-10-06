import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://demo.guru99.com/popup.php")

driver.maximize_window()

driver.find_element(By.XPATH, "//*[contains(@href,'popup.php')]").click()

windows = driver.window_handles
print(windows)
for window in windows:
    time.sleep(2)
    driver.switch_to.window(window)
    time.sleep(2)
    try:
        driver.find_element(By.NAME, "emailid").send_keys("kapil@gmail.com")
        time.sleep(2)
        driver.find_element(By.NAME, "btnLogin").click()
        time.sleep(2)
    except Exception:
        pass
    time.sleep(2)
    print(driver.window_handles)
    driver.close()

    time.sleep(2)


driver.quit()
