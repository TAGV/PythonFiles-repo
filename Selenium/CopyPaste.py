import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

url = "https://infura.io/login"
driver = webdriver.Firefox()
driver.get(url)
driver.maximize_window()

driver.find_element(By.XPATH,"//a[text()='Forgot your password?']").click()
driver.back()                                                                   #Navigate the webpages
driver.find_element(By.XPATH,'//*[@id="email"]').send_keys('Hello')

action = ActionChains(driver)
action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()    # Select Action
action.key_down(Keys.CONTROL).send_keys('x').key_up(Keys.CONTROL).perform()    # Cut Action
action.send_keys(Keys.TAB).perform()                                           # Tab key press
action.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()    # Paste Action
action.send_keys(Keys.ENTER).perform()
time.sleep(3)

# Scroll down the current page
action.send_keys(Keys.TAB).perform()
action.send_keys(Keys.TAB).perform()
action.send_keys(Keys.PAGE_DOWN).perform()

driver.find_element(By.XPATH,"//a[text()='Careers']").click()
time.sleep(3)
action.send_keys(Keys.PAGE_DOWN).perform()
time.sleep(3)
action.send_keys(Keys.PAGE_DOWN).perform()
time.sleep(3)
action.send_keys(Keys.PAGE_DOWN).perform()
print(driver.get_window_position())
print(driver.get_window_size())
print(driver.get_window_rect())
time.sleep(3)
action.send_keys(Keys.END).perform()

# Page Navigation
driver.back()
driver.refresh()
driver.forward()
action.send_keys(Keys.HOME).perform()


time.sleep(10)
driver.quit()