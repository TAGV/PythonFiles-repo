import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


url = 'https://yourstory.com/'
driver = webdriver.Firefox()
driver.get(url)
driver.maximize_window()

element2hover = driver.find_element(By.XPATH,'//*[@id="root"]/div[4]/header/div[2]/div/div[1]/div[1]/div[1]/div[1]/span')
action = ActionChains(driver)  #Creating object of Action chain

# 1st Method
#action.move_to_element(element2hover).perform()
#driver.find_element(By.XPATH,'//*[@id="root"]/div[4]/header/div[2]/div/div[1]/div[1]/div[1]/div[2]/div[1]/a').click()

# 2nd Method
action.move_to_element(element2hover).pause(5).click(driver.find_element(By.XPATH,'//*[@id="root"]/div[4]/header/div[2]/div/div[1]/div[1]/div[1]/div[2]/div[1]/a')).perform()

time.sleep(10)
driver.quit()