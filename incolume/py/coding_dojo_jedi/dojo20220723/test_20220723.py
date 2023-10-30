"""Unittest for dojo."""
import pytest

from incolume.py.coding_dojo_jedi.dojo20220723.dojo20220723 import get_code


# def test_get_code0() -> None:
#     """Test get code."""
#     assert get_code('(') == 40
#
#
# def test_get_code1() -> None:
#     """Test get code."""
#     assert get_code('A') == 65
#
#
# def test_get_code2() -> None:
#     """Test get code."""
#     assert get_code('x') == 120
#
@pytest.mark.parametrize(
    'char expected'.split(),
    [
        ('(', 40),
        ('A', 65),
        ('x', 120),
    ],
)
def test_get_code(char, expected) -> None:
    """Test get code."""
    assert get_code(char) == expected
