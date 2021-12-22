import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


url = 'https://www.snapdeal.com/products/mobiles-printed-back-covers?sort=plrty&q=Price%3A76%2C1049%7C'
driver = webdriver.Firefox()
driver.get(url)
driver.maximize_window()

elem_left = driver.find_element(By.XPATH,'//a[contains(@class,"left-handle")]')     #Left slider
elem_right = driver.find_element(By.XPATH,'//a[contains(@class,"right-handle")]')   #Right Slider

ActionChains(driver).drag_and_drop_by_offset(elem_left,50,0).perform()
time.sleep(5)
ActionChains(driver).drag_and_drop_by_offset(elem_right,-50,0).perform()
time.sleep(2)

for _ in range(5):
    ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
    time.sleep(2)

driver.find_element(By.XPATH,'//i[contains(@class,"backTopImg")]').click()          #Page Up

time.sleep(5)
driver.quit()