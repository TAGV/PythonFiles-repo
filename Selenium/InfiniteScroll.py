#ToWorkon : Need to work on this file
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import pandas as pd


url = 'https://www.snapdeal.com/products/mobiles-printed-back-covers?sort=plrty&q=Price%3A76%2C1049%7C'
driver = webdriver.Firefox()
driver.get(url)
driver.maximize_window()


#//section[contains(@class,"js-section clearfix dp-widget dp-fired")]
#//section[contains(@class,"js-section clearfix dp-widget dp-fired")]/div/div/div/a/p
#//section[contains(@class,"js-section clearfix dp-widget dp-fired")]/div/div/div/a/p[contains(@class,"product-title")]


prodlist = driver.find_elements(By.XPATH,'.//section[contains(@class,"js-section clearfix dp-widget dp-fired")]/div/div/div/a/p[contains(@class,"product-title")]')

print(len(prodlist))
#print(prodlist)

for ele in prodlist:
    print(ele.text)

time.sleep(3)

#for _ in range(20):
ActionChains(driver).send_keys(Keys.END).perform()
  # time.sleep(1)

time.sleep(3)
newlist = driver.find_elements(By.XPATH,'.//section[contains(@class,"js-section clearfix dp-widget dp-fired")]/div/div/div/a/p[contains(@class,"product-title")]')
print(len(newlist))
#print(newlist)

for prod in set(newlist):
    print(prod.text)


time.sleep(5)
driver.quit()