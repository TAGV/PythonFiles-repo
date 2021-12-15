import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains



url = "https://demos.telerik.com/kendo-ui/treeview/animation"

driver = webdriver.Firefox()
driver.get(url)
driver.find_element(By.XPATH,"//button[text()='Accept Cookies']").click()
driver.maximize_window()
#//button[text()='Accept Cookies']
#//span[text()='Storage']
#/html/body/div[4]/div[1]/svg[2]/path
#/html/body/div[4]/div[1]/svg[2]

#/html/body/div[4]/div[1]/svg[2]
#qual_x_svg_dash
#/html/body/main/div/div/div/div[1]/div[4]/div[2]/div/div/ul/li[1]/div/span[2]
#/html/body/main/div/div/div/div[1]/div[4]/div[2]/div/div/ul/li[1]/div/span[1]
#/html/body/main/div/div/div/div[1]/div[4]/div[2]/div/div/ul/li[3]/div/span[1]
driver.find_element(By.CLASS_NAME,"qual_x_svg_dash").click()

#element = driver.find_element(By.XPATH,"//span[text()='Furniture']").click()
#element = driver.find_element(By.XPATH,'/html/body/main/div/div/div/div[1]/div[4]/div[2]/div/div/ul/li[3]/div/span[1]')

driver.execute_script("window.scrollTo(0, 180)")

element = driver.find_element(By.XPATH,"//span[text()='Storage']")
action = ActionChains(driver)
action.double_click(element).perform()



time.sleep(10)
driver.quit()