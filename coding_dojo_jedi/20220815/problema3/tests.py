import pytest
from dojo import adedonha


@pytest.mark.parametrize(
    ('entrance', 'expected'),
    (
        (1, 'a'),
        (5, 'e'),
        (26, 'z'),
        (10, 'j'),
        (2, 'b'),
        (3, 'c'),
        (21, 'u'),
        (100, 'v'),
        (80, 'b'),
        (15, 'o'),
        (19, 's'),
        (36, 'j'),
        (1000, 'l'),
    )
)
def test_adedonha(entrance, expected):
    assert adedonha(entrance) == expected
