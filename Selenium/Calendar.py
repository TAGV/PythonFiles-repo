import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


url = "https://www.redbus.in/"
driver = webdriver.Firefox()
driver.get(url)
driver.maximize_window()

#driver.find_element(By.XPATH,"/html/body/section/div[2]/main/section/div/div[2]/section/div/div[3]/div/label").click()
#driver.find_element(By.XPATH,"//td[text()=17]").click()

driver.find_element(By.XPATH,'//input[@id="onward_cal"]').click()

alldates = driver.find_elements(By.XPATH,'//table[@class="rb-monthTable first last"]//td')
print(len(alldates))

for dates in alldates:
    mydate = dates.text
    #print(type(mydate))
    if mydate == '20':
        dates.click()
        break


action = ActionChains(driver)
action.send_keys(Keys.END).perform()
time.sleep(3)

driver.find_element(By.XPATH,"//a[text()='Careers']").click()


time.sleep(5)
driver.quit()