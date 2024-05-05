"""Unittest for dojo."""

import pytest

from incolume.py.coding_dojo_jedi.dojo20220723.dojo20220723 import get_code


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
