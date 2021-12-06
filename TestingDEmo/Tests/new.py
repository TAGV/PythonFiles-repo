import time

import pytest
from selenium import webdriver


# Fixtures are functions, which will run before each test function to which it is applied
@pytest.fixture
def browser():
    driver = webdriver.Firefox()
    driver.implicitly_wait(15)      # This delay is reqd to allow race conditions
    yield driver                    # Returns the webdriver object and inserted in any test case that calls this fixture
    time.sleep(10)
    driver.close()                   # Closes the browser






