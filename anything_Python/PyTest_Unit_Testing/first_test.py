import pytest

def add5(x):
    return x + 5

def test_method():
    assert add5(3) == 8
