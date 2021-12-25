import pytest
import sys
import platform


@pytest.mark.skip
def test_First():
    print("This is First Test!!!")

@pytest.mark.skipif(sys.version_info>(3,8),reason="Python Version not Supported")   # Giving reason is mandatory
def test_Second():
    print("This is Second Test!!!")

@pytest.mark.skipif(platform.system() != "Windows",reason="Platform Version not Supported")
def test_platform():
    print("This is Platform Test!!!")


@pytest.mark.xfail
def test_3():
    assert True
    print("This is Third Test!!!")

@pytest.mark.xfail
def test_4():
    assert False
    print("This is Fourth Test!!!")

@pytest.mark.parametrize("name,age",
                            [
                                ("Jack",10),
                                ("Rock",30),
                                ("Roger",40)
                            ]
                        )
def test_parameter(name,age):
    print((name))
    print((age))
    mlist = [10,20,40,50]
    #print(mlist[:3])
    assert age in mlist
