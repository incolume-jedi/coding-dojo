"""Unittest for dojo."""

import pytest

from incolume.py.coding_dojo_jedi.dojo20220801.dojo20220801 import is_square


@pytest.mark.parametrize(
    ['entrada', 'esperado'],
    [
        (-1, False),
        (0, True),
        (3, False),
        (4, True),
        (25, True),
        (26, False),
    ],
)
def test_square(entrada, esperado) -> None:
    """Test for is_square."""
    assert is_square(entrada) == esperado
