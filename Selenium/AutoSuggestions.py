import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By
from Locater_POM.Element_locaters import EleLocate      #Page Objects


url = "https://www.redbus.in/"

driver = webdriver.Firefox()
driver.get(url)
driver.maximize_window()

driver.find_element(By.XPATH,EleLocate.destination_box).send_keys('de')
time.sleep(3)
suggestion_list = driver.find_elements(By.XPATH,EleLocate.suggestions)
print(len(suggestion_list))

for sugg in suggestion_list:
    print(sugg.text)
    if sugg.text == 'Dewas':
        sugg.click()
        break

time.sleep(5)
driver.quit()