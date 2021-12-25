import pytest

#pytest -rA test_Markers.py -m "unit"
#pytest -rA test_Markers.py -m "functional"
#pytest -rA test_Markers.py -m "unit or functional"

#We are creating our own custom markers over here: unit & functional

@pytest.mark.unit
def test_1():
    print("This is First Test!!!")

@pytest.mark.unit
def test_2():
    print("This is Second Test!!!")

@pytest.mark.functional
def test_3():
    print("This is Third Test!!!")
