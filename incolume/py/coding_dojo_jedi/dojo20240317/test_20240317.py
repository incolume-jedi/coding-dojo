"""Test module for dojo20240317."""
from incolume.py.coding_dojo_jedi.dojo20240317.dojo import perimeter
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
