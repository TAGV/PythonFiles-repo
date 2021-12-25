import time
from selenium import webdriver
import pytest
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Firefox()

@pytest.fixture
def start_comment():
    print("Start the browser")
    yield
    print("Action Completed")           # Run this file as "pytest test_fixtures.py -s" to see the after yield output


@pytest.fixture
def maximize_comment():
    print("Maximize the browser")
    yield
    print("Action Completed")


@pytest.fixture
def unittest_comment():
    print("Test the browser")
    yield
    print("Action Completed")



@pytest.fixture
def close_comment():
    print("Quit the driver")
    yield driver
    time.sleep(3)
    driver.quit()



def test_browser(start_comment):
    print("Opening the website")
    driver.get("https://www.redbus.in/")

def test_maximize(maximize_comment):
    print("Maximize the website")
    driver.maximize_window()

def test_unit_testing(unittest_comment):
    print("Unit test the browser")
    time.sleep(3)
    action = ActionChains(driver)
    action.send_keys(Keys.END).perform()
    time.sleep(5)
    driver.find_element(By.XPATH, "//a[text()='Careers']").click()

def test_close(close_comment):
    print("Close the website")