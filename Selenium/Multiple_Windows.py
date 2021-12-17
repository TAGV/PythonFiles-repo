import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


url = "https://www.redbus.in/"
driver = webdriver.Firefox()
driver.get(url)
driver.maximize_window()

parent_window = driver.current_window_handle
print(parent_window)



action = ActionChains(driver)
action.send_keys(Keys.END).perform()
time.sleep(3)

driver.find_element(By.XPATH,"//a[text()='Careers']").click()

child_windows = driver.window_handles
print(child_windows)

for child in child_windows:
    if child != parent_window:
        print("Switching to child window!!!")
        driver.switch_to.window(child)
        time.sleep(3)
        print(driver.current_url)
        print(driver.title)
        action.send_keys(Keys.END).perform()
        time.sleep(3)
        driver.close()


print("Switching back to Parent window!!!")
driver.switch_to.window(parent_window)
action.send_keys(Keys.HOME).perform()
time.sleep(3)
print(driver.current_url)
print(driver.title)

time.sleep(5)
driver.quit()