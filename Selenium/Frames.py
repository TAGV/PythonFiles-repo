import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By


url = "https://www.redbus.in/"
driver = webdriver.Firefox()
driver.get(url)
driver.maximize_window()


driver.find_element(By.XPATH, '//i[@id="i-icon-profile"]').click()
driver.find_element(By.XPATH, '//li[text()="Sign In/Sign Up"]').click()
time.sleep(3)

# Getting the parent window handle
parent_window = driver.current_window_handle

# Element is in Iframe, if not switched then we get an Exception
# NoSuchElementException

# Switching to the iframe | Check ways of switching to iframe in its parent class
driver.switch_to.frame(driver.find_element(By.XPATH, '//iframe[@class="modalIframe"]'))
time.sleep(3)

# Accesing the web elements inside the iframe
driver.find_element(By.XPATH, '//*[@id="mobileNoInp"]').send_keys("4556655")
driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div[1]/div[8]/div[2]/div[2]').click()

# Switching back to the parent frame
driver.switch_to.parent_frame()

# Closing the recently opened iframe
driver.find_element(By.XPATH, '//i[@class="icon-close"]').click()

# Checking for other child window handles
child_windows = driver.window_handles

for child in child_windows:
    if child != parent_window:
        print("Switching to child window!!!")
        driver.switch_to.window(child)
        driver.maximize_window()
        time.sleep(3)
        print(driver.current_url)
        print(driver.title)

        # Closing the child window only
        driver.close()

# Switching back to parent window
print()
print("Switching back to Parent window!!!")
driver.switch_to.window(parent_window)
print(driver.current_url)
print(driver.title)

time.sleep(5)
driver.quit()