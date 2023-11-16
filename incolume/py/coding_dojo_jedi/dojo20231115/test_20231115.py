from re import escape

import pytest
from incolume.py.coding_dojo_jedi.dojo20231115.dojo import (
    milissegundos, validar_entrada)


# def test_validar_entrada() -> None:
#     """Test validar_entrada."""
#     assert validar_entrada(1, 2, 3, 2) == ''
    # h = 0
    # m = 1
    # s = 1
    #
    # milissegundos(h, m, s) == 61000
    # milissegundos(datetime(h, m, s)) == 61000
    # milissegundos(time(h, m, s)) == 61000


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
    ],
)
def test_millissenconds(entrance, expected) -> None:
    """Test for millisseconds."""
    assert milissegundos(**entrance) == expected


@pytest.mark.skip
@pytest.mark.parametrize(
    'entrance expected'.split(),
    [
        pytest.param(
            (0, 0, 0),
            {
                'expected_exception': TypeError,
                'match': r'millisseconds\(\) takes 0 positional'
                         r' arguments but 3 were given',
            },
            marks=pytest.mark.skip,
        ),
        pytest.param(
            (1, 1, 1),
            {
                'expected_exception': TypeError,
                'match': escape(
                    'millisseconds() takes 0 positional '
                    'arguments but 3 were given',
                ),
            },
            marks=pytest.mark.skip
        ),

    ],
)
def test_millissenconds_exception0(entrance, expected) -> None:
    """Test for millisseconds exceptions."""
    with pytest.raises(**expected):
        milissegundos(*entrance)

@pytest.mark.skip
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
    ]
)
def test_millissenconds_exception(entrance, expected) -> None:
    """Test for millisseconds exceptions."""
    with pytest.raises(**expected):
        milissegundos(**entrance)
