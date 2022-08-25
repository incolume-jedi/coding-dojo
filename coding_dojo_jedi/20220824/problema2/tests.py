import pytest
from dojo import millisseconds


@pytest.mark.parametrize(
    'entrance expected'.split(),
    (
        ({}, 0),
        ({'s': 1}, 1_000),
        ({'m': 1}, 60_000),
        ({'h': 1}, 3_600_000),
        ({'m': 1, 's': 1}, 61_000),
        ({'h': 1, 's': 1}, 3_601_000),
        ({'h': 1, 'm': 1}, 3_660_000),
        ({'h': 0, 'm': 0, 's': 0}, 0),
        ({'h': 23, 'm': 59, 's': 59}, 86_399_000),
    )
)
def test_millissenconds(entrance, expected):
    assert millisseconds(**entrance) == expected


@pytest.mark.parametrize(
    'entrance expected'.split(),
    (
        ({'h': -1, 'm': 0, 's': 0}, {'expected_exception': ValueError, 'match': '0 <= h <= 23'}),
        ({'h': 24, 'm': 0, 's': 0}, {'expected_exception': ValueError, 'match': '0 <= h <= 23'}),
        ({'h': 0, 'm': -1, 's': 0}, {'expected_exception': ValueError, 'match': '0 <= m <= 59'}),
        ({'h': 0, 'm': 60, 's': 0}, {'expected_exception': ValueError, 'match': '0 <= m <= 59'}),
        ({'h': 0, 'm': 0, 's': -2}, {'expected_exception': ValueError, 'match': '0 <= s <= 59'}),
        ({'h': 0, 'm': 0, 's': 60}, {'expected_exception': ValueError, 'match': '0 <= s <= 59'}),
    )
)
def test_millissenconds_exception(entrance, expected):
    with pytest.raises(**expected):
        millisseconds(**entrance)
