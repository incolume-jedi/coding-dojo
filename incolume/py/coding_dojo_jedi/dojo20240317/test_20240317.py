"""Test module for dojo20240317."""
from incolume.py.coding_dojo_jedi.dojo20240317.dojo import perimeter, qlatas
import pytest


__author__ = "@britodfbr"  # pragma: no cover


@pytest.mark.parametrize(
    "entrance expected".split(),
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
    "entrance expected".split(),
    [
        (108, ['1 lata 18L']),
        (18, ['1 galão 3.6L']),
    ]
)
def test_qlatas(entrance, expected) -> None:
    """Test qlatas."""
    assert qlatas(entrance) == expected
