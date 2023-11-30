"""Test Get Planet Name By ID"""
import pytest
from incolume.py.coding_dojo_jedi.dojo20231127.dojo import get_planet_name0, get_planet_name


@pytest.mark.parametrize(
    'entrance expected'.split(),
    [
        (2, 'Venus'),
        (5, 'Jupiter'),
        (3, 'Earth'),
        (4, 'Mars'),
        (8, 'Neptune'),
        (1, 'Mercury'),
    ]
)
def test_get_planet_name0(entrance, expected) -> None:
    """Test it."""
    assert get_planet_name0(entrance) == expected


@pytest.mark.parametrize(
    'entrance expected'.split(),
    [
        (2, 'Venus'),
        (5, 'Jupiter'),
        (3, 'Earth'),
        (4, 'Mars'),
        (8, 'Neptune'),
        (1, 'Mercury'),
    ]
)
def test_get_planet_name(entrance, expected) -> None:
    """Test it."""
    assert get_planet_name(entrance) == expected
