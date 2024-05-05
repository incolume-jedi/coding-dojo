"""Test dojo20231129."""

import pytest

from incolume.py.coding_dojo_jedi.dojo20231129 import dojo20231129 as dojo

tests = [
    (
        [
            'OX',
            'XO',
        ],
        'Total land perimeter: 8',
    ),
    (
        [
            'XOOXX',
            'XOOXO',
            'OOXXO',
            'XXOXO',
            'OXOXO',
        ],
        'Total land perimeter: 30',
    ),
    (
        [
            'XXXXX',
            'XXXXX',
            'XXXXX',
            'XXXXX',
            'XXXXX',
        ],
        'Total land perimeter: 20',
    ),
    (
        [
            'XOOXO',
            'XOOXO',
            'OOOXO',
            'XXOXO',
            'OXOOO',
        ],
        'Total land perimeter: 24',
    ),
    (
        [
            'XOOO',
            'XOXO',
            'XOXO',
            'OOXX',
            'OOOO',
        ],
        'Total land perimeter: 18',
    ),
]


@pytest.mark.parametrize(
    'entrance expected'.split(),
    tests,
)
def test_perimetro_terrestre_0(entrance, expected) -> None:
    """Test it."""
    assert dojo.land_perimeter_0(entrance) == expected


@pytest.mark.parametrize(
    'entrance expected'.split(),
    tests,
)
def test_perimetro_terrestre_1(entrance, expected) -> None:
    """Test it."""
    assert dojo.land_perimeter_1(entrance) == expected


@pytest.mark.parametrize(
    'entrance expected'.split(),
    tests,
)
def test_perimetro_terrestre_2(entrance, expected) -> None:
    """Test it."""
    assert dojo.land_perimeter_2(entrance) == expected


@pytest.mark.parametrize(
    'entrance expected'.split(),
    tests,
)
def test_perimetro_terrestre_3(entrance, expected) -> None:
    """Test it."""
    assert dojo.land_perimeter_3(entrance) == expected


@pytest.mark.parametrize(
    'entrance expected'.split(),
    tests,
)
def test_land_permetecal(entrance, expected) -> None:
    """Test it."""
    assert dojo.land_permetercal(entrance) == expected
