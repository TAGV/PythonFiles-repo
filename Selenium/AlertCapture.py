import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By

url = "https://mail.rediff.com/cgi-bin/login.cgi"
driver = webdriver.Firefox()
driver.get(url)
driver.maximize_window()

driver.find_element(By.NAME,"proceed").click()
time.sleep(3)
alert_cap = driver.switch_to.alert
print("Alert Mesg = ",alert_cap.text)   #Printing the alert mesg text
alert_cap.accept()                      #Capturing the alert
driver.find_element(By.NAME,"login").send_keys("Hello")



time.sleep(10)
driver.quit()