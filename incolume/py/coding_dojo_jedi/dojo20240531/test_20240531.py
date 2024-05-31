"""Module."""

import pytest

from incolume.py.coding_dojo_jedi.dojo20240531 import (
    last_dig,
    last_dig0,
    last_dig1,
    num_extense,
)

__author__ = '@britodfbr'  # pragma: no cover


@pytest.mark.parametrize(
    'function entrance expected'.split(),
    [
        (last_dig0, (2, 27), 8),
        (last_dig1, (2, 27), 8),
        (last_dig, (2, 27), 8),
    ],
)
def test_last_dig(function, entrance, expected):
    """Test last_dig."""
    assert function(*entrance) == expected


@pytest.mark.parametrize(
    'entrance expected'.split(),
    [
        ('vinte', 20),
        ('cento e quarenta e cinco', 145),
        ('mil e um', 1001),
        ('dezenove', 19),
        ('doze', 12),
        ('um', 1),
        ('zero', 0),
        ('mil novecentos e setenta e oito', 1978),
        ('dezessete', 17),
        ('quinhentos', 500),
        ('quinhentos e dezessete', 517),
    ],
)
def test_num_extenso(entrance, expected):
    """Test it."""
    assert num_extense(entrance) == expected
