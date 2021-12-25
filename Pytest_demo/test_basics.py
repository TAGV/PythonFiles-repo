
#Commands to run from command line(to generate xml and html reports)
#pytest --html = MyReport.html   #Need to install module pytest-html
#pytest -rA --junitxml="Report1.xml"

def test_1():
    print("This is first test!!!")
    x = 10
    y = 10
    assert x == y

def test_2():
    print("This is Second test!!!")
    str1 = 'party'
    str2 = "Welcome to the party"
    assert str1 in str2