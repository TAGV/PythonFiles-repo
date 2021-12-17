import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import os

# In Headless mode the scripts are executed in the background

opt = Options()
#opt.add_argument("--headless")
opt.headless = True

url = "https://www.google.in/"
driver = webdriver.Firefox(options=opt)     # Check the argument
driver.get(url)

os.chdir("/home/myubuntu/Desktop")
cwd = (os.getcwd())

driver.find_element(By.NAME,'q').send_keys("Elon")
time.sleep(5)
driver.get_screenshot_as_file(cwd+"/Headless_GoogleSearch.png")



time.sleep(3)
driver.quit()
