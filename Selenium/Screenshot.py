import time
import os
import datetime
from selenium import webdriver

url = "https://infura.io/login"
driver = webdriver.Firefox()

driver.get(url)

current_dateTime = datetime.datetime.today()
os.chdir("/home/myubuntu/Desktop")
cwd = (os.getcwd())

driver.get_screenshot_as_file(cwd+"/InfuraShot--"+str(current_dateTime)+".png")

time.sleep(10)
driver.quit()