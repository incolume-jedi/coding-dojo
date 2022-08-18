import pytest
from dojo import mysort


@pytest.mark.parametrize(
    'entrance expected'.split(),
    (
        ((2, 1, 3), (3, 2, 1)),
        ((7, 8, 9), (9, 8, 7)),
        ((1000, 1, 10), (1000, 10, 1)),
    )
)
def test_mysort(entrance, expected):
    assert mysort(*entrance) == expected
