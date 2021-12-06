import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from TestingDEmo.Tests.new import browser

class FirefoxResult:

    def __init__(self,browser):
        self.browser = browser

    def search_input(self):
        return 'panda'

    def title(self):
        time.sleep(10)
        print("hello World")
        print(self.browser.title)
        return self.browser.title

    def links(self):
        time.sleep(10)
        link = self.browser.find_elements(By.LINK_TEXT,'panda')
        print(type(link))
        return link
