import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By


url = "https://www.google.in/"

driver = webdriver.Firefox()
driver.get(url)
driver.maximize_window()

driver.find_element(By.NAME,'q').send_keys('tele')
time.sleep(3)
mlist = driver.find_elements(By.CLASS_NAME,"wM6W7d")
print(len(mlist))

for elements in mlist:
    print(elements.text)
    if elements.text == 'telegram':
        elements.click()
        break

time.sleep(5)

#driver.find_element(By.XPATH,'//a[text()="Videos"]').click()
#time.sleep(5)
#driver.find_element(By.XPATH,'/html/body/div[7]/div/div[10]/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div/div[1]/a/div/cite').click()


#Clicking the first link in the search results space
driver.find_element(By.XPATH,'/html/body/div[7]/div/div[10]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/a/h3').click()
time.sleep(5)
driver.quit()