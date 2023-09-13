import pytest
from dojo import high_and_low


@pytest.mark.parametrize(
    'entrance expected'.split(),
    (
        ("1 2 3 4 5", "5 1"),
        ("1 2 -3 4 5", "5 -3"),
        ("1 9 3 4 -5", "9 -5"),
    )
)
def test_high_and_low(entrance, expected):
    assert high_and_low(entrance) == expected
