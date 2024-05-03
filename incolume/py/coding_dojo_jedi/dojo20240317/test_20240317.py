"""Test module for dojo20240317."""

from incolume.py.coding_dojo_jedi.dojo20240317.dojo20240317 import (
    perimeter,
    qlatas,
)
import pytest


__author__ = '@britodfbr'  # pragma: no cover


@pytest.mark.parametrize(
    'entrance expected'.split(),
    [
        ([], 0),
        ([[1, 2], [3, 4]], 10),
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 40),
        ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], 102),
    ],
)
def test_perimeter(entrance, expected) -> None:
    """Test it."""
    assert perimeter(entrance) == expected


@pytest.mark.parametrize(
    'entrance expected'.split(),
    [
        (
            108,
            (
                'Area: 108 m2; Galão(ões): 7 (3.6)L x R$25 = R$ 175;'
                ' Lata(s): 2 (18)L x R$80 = R$ 160'
            ),
        ),
        (
            18,
            (
                'Area: 18 m2; Galão(ões): 2 (3.6)L x R$25 = R$ 50;'
                ' Lata(s): 1 (18)L x R$80 = R$ 80'
            ),
        ),
    ],
)
def test_qlatas(entrance, expected) -> None:
    """Test qlatas."""
    assert qlatas(entrance) == expected
