"""Test milissegundos."""
import datetime
from re import escape

import pytest

from incolume.py.coding_dojo_jedi.dojo20231115.dojo import milissegundos


@pytest.mark.parametrize(
    'entrance expected'.split(),
    [
        ({}, 0),
        ({'s': 1}, 1_000),
        ({'m': 1}, 60_000),
        ({'h': 1}, 3_600_000),
        ({'m': 1, 's': 1}, 61_000),
        ({'h': 1, 's': 1}, 3_601_000),
        ({'h': 1, 'm': 1}, 3_660_000),
        ({'h': 0, 'm': 0, 's': 0}, 0),
        ({'h': 23, 'm': 59, 's': 59}, 86_399_000),
        ({'hms': datetime.time(hour=1)}, 3_600_000),
        ({'hms': datetime.time(minute=1)}, 60_000),
        ({'hms': datetime.time(second=1)}, 1_000),
        ({'hms': datetime.time(minute=1, second=1)}, 61_000),
        (
            {
                'hms': datetime.datetime(
                    year=2023, month=11, day=27, hour=1, tzinfo='',
                ),
            },
            3_600_000,
        ),
        (
            {
                'hms': datetime.datetime(
                    year=2023, month=11, day=27, minute=1, tzinfo='',
                ),
            },
            60_000,
        ),
        (
            {
                'hms': datetime.datetime(
                    year=2023, month=11, day=27, second=1, tzinfo='',
                ),
            },
            1_000,
        ),
        (
            {
                'hms': datetime.datetime(
                    year=2023, month=11, day=27, minute=1, second=1, tzinfo='',
                ),
            },
            61_000,
        ),
    ],
)
def test_millissenconds(entrance, expected) -> None:
    """Test for millisseconds."""
    assert milissegundos(**entrance) == expected


# @pytest.mark.skip
@pytest.mark.parametrize(
    'entrance expected'.split(),
    [
        pytest.param(
            (0, 0, 0),
            {
                'expected_exception': TypeError,
                'match': escape(
                    'milissegundos() takes 0 positional'
                    ' arguments but 3 were given',
                ),
            },
        ),
        pytest.param(
            (1, 1, 1),
            {
                'expected_exception': TypeError,
                'match': escape(
                    'milissegundos() takes 0 positional'
                    ' arguments but 3 were given',
                ),
            },
        ),
    ],
)
def test_millissenconds_exception0(entrance, expected) -> None:
    """Test for millisseconds exceptions."""
    with pytest.raises(**expected):
        milissegundos(*entrance)


# @pytest.mark.skip
@pytest.mark.parametrize(
    'entrance expected'.split(),
    [
        (
            {'h': -1, 'm': 0, 's': 0},
            {'expected_exception': ValueError, 'match': '0 <= h <= 23'},
        ),
        (
            {'h': 24, 'm': 0, 's': 0},
            {'expected_exception': ValueError, 'match': '0 <= h <= 23'},
        ),
        (
            {'h': 0, 'm': -1, 's': 0},
            {'expected_exception': ValueError, 'match': '0 <= m <= 59'},
        ),
        (
            {'h': 0, 'm': 60, 's': 0},
            {'expected_exception': ValueError, 'match': '0 <= m <= 59'},
        ),
        (
            {'h': 0, 'm': 0, 's': -2},
            {'expected_exception': ValueError, 'match': '0 <= s <= 59'},
        ),
        (
            {'h': 0, 'm': 0, 's': 60},
            {'expected_exception': ValueError, 'match': '0 <= s <= 59'},
        ),
    ],
)
def test_millissenconds_exception(entrance, expected) -> None:
    """Test for millisseconds exceptions."""
    with pytest.raises(**expected):
        milissegundos(**entrance)
