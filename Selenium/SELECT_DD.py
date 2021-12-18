import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select



url = "https://www.facebook.com/"

driver = webdriver.Firefox()
driver.get(url)
driver.maximize_window()


driver.find_element(By.XPATH,'//a[text()="Create New Account"]').click()
time.sleep(3)
driver.find_element(By.XPATH,'//label[text()="Male"]').click()

month = driver.find_element(By.ID,'month')
month_ss = Select(month)                        #Object of Select class

#Checking the default option in the drop down list
dd_default_month = month_ss.first_selected_option
assert 'Dec'==dd_default_month.text

month_ss.select_by_index(3) #index starts from zero
time.sleep(2)
month_ss.select_by_value('7')
time.sleep(2)
month_ss.select_by_visible_text('Feb')      #Always preferred way to select the values in Selenium
time.sleep(2)

#Storing/Searching the list of dropdowns

ddmon = month_ss.options
print(len(ddmon))
assert 12==len(ddmon)

for element in ddmon:
    print(element.text)
    if element.text == 'Apr':
        element.click()
        break

time.sleep(5)
driver.quit()