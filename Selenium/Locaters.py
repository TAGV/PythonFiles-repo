import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By


url = "https://infura.io/login"
driver = webdriver.Firefox()
driver.get(url)
driver.maximize_window()


#Forgot your password?
#Sign up
#//input[@name = "email"]
#/html/body/div[2]/div/footer/div/div[2]/div[2]/a[3]
#text-white mr-4
#/html/body/div[2]/div/footer/div/div[2]/div[2]/a[3]
driver.find_element(By.LINK_TEXT,"Forgot your password?").click()
time.sleep(3)
driver.back()
time.sleep(3)
driver.find_element(By.PARTIAL_LINK_TEXT,"Sign").click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR,'input[name = "email"]').send_keys("Hello")    #Check the Syntax and diff with Xpath
driver.find_element(By.XPATH,'//input[@name = "password"]').send_keys("Bye")
time.sleep(3)
driver.find_element(By.XPATH,'/html/body/div[2]/div/footer/div/div[2]/div[2]/a[3]').click()
time.sleep(3)
mtaglist = driver.find_elements(By.TAG_NAME,'a')
print(len(mtaglist))

for tag in mtaglist:
    print(tag.text)
    if tag.text == "Terms of Use":
        tag.click()
        break



time.sleep(5)
driver.quit()