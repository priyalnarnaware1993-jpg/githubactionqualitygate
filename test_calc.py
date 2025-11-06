import pytest

from calc import add, sub, mul, div

def test_add():
    #compare actual output and exoected output
    assert add(2, 3) == 5

def test_sub():
    #compare actual output and exoected output
    assert sub(3, 1) == 2

def test_mul():
    #compare actual output and exoected output
    assert mul(2, 3) == 6     

def test_div():
    #compare actual output and exoected output
    assert div(4, 2) == 2    