import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By
import pandas as pd


url = 'https://www.snapdeal.com/products/mobiles-printed-back-covers?sort=plrty&q=Price%3A76%2C1049%7C'
driver = webdriver.Firefox()
driver.get(url)
driver.maximize_window()

listOfProducts = []

prod_list = driver.find_elements(By.XPATH,'//div[contains(@class,"product-desc-rating ")]')
print(len(prod_list))

for product in prod_list:
    title = product.find_element(By.XPATH,'.//p[contains(@class,"product-title")]')
    price = product.find_element(By.XPATH,'.//span[contains(@class,"product-price")]')
    discount = product.find_element(By.XPATH,'.//div[contains(@class,"product-discount")]')
    original_price = product.find_element(By.XPATH,'.//span[contains(@class,"lfloat product-desc-price strike")]')
    #print(title.text,price.text,discount.text)
    prod_items = {
        'Title': title.text,
        'Original Price': original_price.text,
        'Discount': discount.text,
        'New Price':price.text
    }
    listOfProducts.append(prod_items)


df = pd.DataFrame(listOfProducts)
#df.to_excel("/home/myubuntu/Desktop/Ecom_data.xlsx")
df.to_excel("Ecommerce_data.xlsx")
print(df)

time.sleep(5)
driver.quit()