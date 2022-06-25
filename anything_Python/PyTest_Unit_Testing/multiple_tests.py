import pytest

@pytest.mark.one
def test_method1():
    x = 5
    y = 10
    print("Hello world")
    assert x == y

@pytest.mark.two
def test_method2():
    a = 15
    b = 20
    assert a+5 == b

'''
Run the individual methods by typing in the terminal:
    py.test -m <one/two>

These can be used to group tests together.
'''
