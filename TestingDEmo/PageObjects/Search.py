from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from TestingDEmo.Tests.new import browser

class FirefoxSearch:

    URL = "https://www.duckduckgo.com/"

    def __init__(self,browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def search(self,phrase):
        input = self.browser.find_element(By.NAME,'q')
        input.send_keys(phrase + Keys.RETURN)
