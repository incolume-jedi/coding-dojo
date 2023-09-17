import pytest
from dojo20220810 import is_vogal


@pytest.mark.parametrize(
    ('entrance', 'expected'),
    (
        ('a', True),
        ('c', False),
        ('b', False),
        ('k', False),
        ('w', False),
        ('y', False),
        ('x', False),
        ('e', True),
        ('i', True),
        ('o', True),
        ('u', True),
        ('p', False),
        ('r', False),
    ),
)
def test_is_vogal(entrance, expected):
    assert is_vogal(entrance) == expected
