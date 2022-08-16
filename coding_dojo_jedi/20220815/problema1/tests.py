from dojo import index
import pytest


@pytest.mark.parametrize(
    ('entrance', 'expected'),
    (
        (0, 'P'),
        (6, 'P'),
        (1, 'y'),
        (5, 'n'),
        (2, 't'),
        (1026, 'P'),
        (2048, 't'),
        (3073, 'y'),
        (65536, 'o'),
    )
)
def test_index(entrance, expected):
    assert index(entrance) == expected
