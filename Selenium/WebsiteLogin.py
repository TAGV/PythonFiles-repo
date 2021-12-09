import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

url = "https://infura.io/login"
driver = webdriver.Firefox()

driver.get(url)

#//*[@id="email"]
#//*[@id="password"]
#/html/body/div[1]/div/section/div/div[1]/form/div/button
#//*[@id="menu-button-1"]
#//*[@id="menu-list-item-link-7"]

with open("/home/myubuntu/Desktop/infura_pwd.txt","r") as pwd:
    login = pwd.readline()
    passwd = pwd.readline()

    #Login to the website
    driver.find_element(By.XPATH,'//*[@id="email"]').send_keys(login)
    driver.find_element(By.XPATH,'//*[@id="password"]').send_keys(passwd)
    driver.find_element(By.XPATH,'/html/body/div[1]/div/section/div/div[1]/form/div/button').click()

    time.sleep(10)

    #Logout of the website
    driver.find_element(By.XPATH,'//*[@id="menu-button-1"]').click()
    driver.find_element(By.XPATH,'//*[@id="menu-list-item-link-7"]').click()

    driver.quit()