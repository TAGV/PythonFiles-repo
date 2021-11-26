import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

# This step is not required since I have installed "firefox-geckodriver" module directly.
# The module will be added to the path
# PATH = "/home/myubuntu/geckodriver-v0.30.0-linux64/"

driver = webdriver.Firefox()
#wait = ui.WebDriverWait(driver, 10)
driver.get("https://www.tennis.com/")
#print(driver.title)
#print(driver.current_url)
search = driver.find_element(By.NAME,value="q")
search.clear()
search.send_keys("Roger")
search.send_keys(Keys.RETURN)
time.sleep(20)
driver.close()


"""
driver = webdriver.Firefox()
driver.get("http://www.python.org")
#assert "Python" in driver.title
elem = driver.find_element(By.NAME,value="q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
#assert "No results found." not in driver.page_source
time.sleep(10)
driver.close()

"""