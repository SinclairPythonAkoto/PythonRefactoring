'''
Paramatrized tests in Pytest allows you to create prexisting paramters
for your tests.
'''

import pytest

@pytest.mark.parametrize("x,y,z", [(10,20,200), (20,40,200)])
def test_method(x,y,z):
    assert x*y == z
