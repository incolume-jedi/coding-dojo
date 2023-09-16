import pytest
from dojo20220817 import high_and_low, mysort, mysort0, mysort1


@pytest.mark.parametrize(
    "entrance expected".split(),
    (
        ("1 2 3 4 5", "5 1"),
        ("1 2 -3 4 5", "5 -3"),
        ("1 9 3 4 -5", "9 -5"),
    ),
)
def test_high_and_low(entrance, expected):
    assert high_and_low(entrance) == expected


@pytest.mark.parametrize(
    "entrance expected".split(),
    (
        ((2, 1, 3), (3, 2, 1)),
        ((7, 8, 9), (9, 8, 7)),
        ((1000, 1, 10), (1000, 10, 1)),
        ((3, 1, 2), (3, 2, 1)),
        ((2, 3, 1), (3, 2, 1)),
    ),
)
def test_mysort(entrance, expected):
    assert mysort0(*entrance) == expected
    assert mysort1(*entrance) == expected
    assert mysort(*entrance) == expected
