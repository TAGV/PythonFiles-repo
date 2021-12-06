import time

from TestingDEmo.Tests.new import browser
from TestingDEmo.PageObjects.Search import FirefoxSearch
from TestingDEmo.PageObjects.Results import FirefoxResult



def test_1(browser):
    search_page = FirefoxSearch(browser)
    result_page = FirefoxResult(browser)

    search_page.load()
    search_page.search("panda")

    assert "panda" == result_page.search_input()
    assert "panda" in result_page.title()

    #for link in result_page.links():
        #assert "panda" in link

    #print(result_page.links())
    print(len(result_page.links()))

    for lt in result_page.links():
        print(lt)
        assert "panda" in lt.lower()
        time.sleep(2)
