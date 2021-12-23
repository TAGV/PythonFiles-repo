#ToWorkon : Need to work on this file
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import pandas as pd
from selenium.common.exceptions import NoSuchElementException   #Specifically for exception Handling


url = 'https://www.snapdeal.com/products/mobiles-printed-back-covers?sort=plrty&q=Price%3A76%2C1049%7C'
driver = webdriver.Firefox()
driver.get(url)
driver.maximize_window()
time.sleep(3)
counter = 0

elelist = []
while True:
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")
    #print("last_height= ",last_height)

    # Scroll down to bottom
    for _ in range(1):
        ActionChains(driver).send_keys(Keys.END).perform()
        time.sleep(1)

    # Scroll Up to check reload
    for _ in range(2):
        ActionChains(driver).send_keys(Keys.PAGE_UP).perform()
        time.sleep(1)

    # Wait to load page
    time.sleep(3)
    counter=counter+1

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    #print("New Height= ",new_height)

    if new_height == last_height:
        break
    else:
        last_height = new_height
        elelist = driver.find_elements(By.XPATH,'//div[contains(@class,"product-tuple-listing")]')

print(len(elelist))

prodlist = []
for prod in elelist:
    name = prod.find_element(By.XPATH,'.//p[@class="product-title"]').text
    price = prod.find_element(By.XPATH,'.//span[contains(@class,"product-price")]').text
    discount = prod.find_element(By.XPATH,'.//div[@class="product-discount"]').text
    orig_price = prod.find_element(By.XPATH,'.//span[contains(@class,"price strike")]').text

    #Check for exceptions incase of missing data fields and handle it
    try:
        rating = prod.find_element(By.XPATH,'.//p[@class="product-rating-count"]').text
    except NoSuchElementException:
        rating = "Not Rated Yet!!!"

    #print(name,price,discount,rating,orig_price)


    prod_dict = {'Name':name,
                 'Original Price':orig_price,
                 'Discount':discount,
                 'New Price':price,
                 'Ratings':rating
                 }
    prodlist.append(prod_dict)


df = pd.DataFrame(prodlist)
df.to_excel("Scroll_Ecomm.xlsx")
print(df)

print(counter)
time.sleep(5)
driver.quit()