"""Module test."""

import pytest
from . import calc_age


@pytest.mark.parametrize(
    'entrance expected'.split(),
    [
        (65, 23725),
        (0, 0),
        (20, 7300),
    ],
)
def test_calc_age(entrance, expected):
    """Test it."""
    assert calc_age(entrance) == expected
