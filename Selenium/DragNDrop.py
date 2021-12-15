import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains



url = "https://demos.telerik.com/kendo-ui/treeview/dragdrop"

driver = webdriver.Firefox()
driver.get(url)
driver.maximize_window()


source = driver.find_element(By.XPATH,'/html/body/main/div/div/div/div[1]/div[4]/div/div/div[1]/div/ul/li[1]/ul/li[3]/div/span')
target = driver.find_element(By.XPATH,'/html/body/main/div/div/div/div[1]/div[4]/div/div/div[2]/div/ul/li[1]/ul/li[3]/div/span')

action = ActionChains(driver)
action.drag_and_drop(source,target).pause(5).perform()

time.sleep(10)
driver.quit()