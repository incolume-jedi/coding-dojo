import pytest
from dojo20220723 import get_code


def test_get_code0():
    assert get_code("(") == 40


def test_get_code1():
    assert get_code("A") == 65


def test_get_code2():
    assert get_code("x") == 120
