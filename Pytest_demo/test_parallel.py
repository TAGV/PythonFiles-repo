import time
from selenium import webdriver
import pytest

# To run the test in parallel:
# install pytest-xdist package, then run command for n=3 processes
# pytest test_parallel.py -n 3


driver = None
counter = 0
@pytest.fixture
def main():
    global driver
    global counter
    driver = webdriver.Firefox()
    yield                           # Run this file as "pytest test_fixtures.py -s" to see the after yield print output
    time.sleep(3)
    counter = counter + 1
    driver.quit()
    print("Closing the site : ", counter)

def test_site1(main):
    driver.get("https://www.snapdeal.com/products/")


def test_site2(main):
    driver.get("https://www.redbus.in/")

def test_site3(main):
    driver.get("https://www.google.in/")