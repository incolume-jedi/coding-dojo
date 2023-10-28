"""Unittest for dojo."""
from incolume.py.coding_dojo_jedi.dojo20220723.dojo20220723 import get_code

def test_get_code0() -> None:
    """Test get code."""
    assert get_code('(') == 40


def test_get_code1() -> None:
    """Test get code."""
    assert get_code('A') == 65


def test_get_code2() -> None:
    """Test get code."""
    assert get_code('x') == 120
