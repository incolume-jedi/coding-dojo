from incolume.py.coding_dojo_jedi.dojo20240317.dojo import perimeter
import pytest


__author__ = '@britodfbr'  # pragma: no cover


@pytest.mark.parametrize(
    'entrance expected'.split(),
    [
        ([], 0),
        ([[1, 2, 3],[4, 5, 6], [7, 8, 9]], 10),
    ],
)
def test_perimeter(entrance, expected):
    """"""
    assert perimeter( entrance ) == expected
