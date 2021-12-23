#ToWorkon : Need to work on this file
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import pandas as pd


url = 'https://webscraper.io/test-sites/e-commerce/scroll/computers/laptops'
driver = webdriver.Firefox()
driver.get(url)
driver.maximize_window()

SCROLL_PAUSE_TIME = 0.5
counter = 0

elelist = []
while True:
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)
    counter=counter+1

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    else:
        last_height = new_height
        elelist = driver.find_elements(By.XPATH,'//div[@class="thumbnail"]')

print(len(elelist))
prodlist = []

for prod in elelist:
    title = prod.find_element(By.XPATH,'.//a[@class="title"]').text
    price = prod.find_element(By.XPATH,'.//h4[contains(@class,"price")]').text
    rating = prod.find_element(By.XPATH,'.//p[@class="pull-right"]').text
    #print(title,price,rating)

    prod_dict = {'Title':title,
                 'Price':price,
                 'Ratings':rating
                 }
    prodlist.append(prod_dict)

df = pd.DataFrame(prodlist)
df.to_excel("InfiniteScroll_data.xlsx")
print(df)

print(counter)
time.sleep(5)
driver.quit()