import pytest

from incolume.py.coding_dojo_jedi.dojo20220714 import dojo20220714


@pytest.mark.parametrize(
    ('entrance', 'expected'),
    [
        ('Python', 'nohtyP'),
        ('Brasil', 'lisarB'),
        ('Ada', 'adA'),
        ('Ana', 'anA'),
    ],
)
def test_rev(entrance: str, expected: str) -> None:
    assert dojo20220714.rev(entrance) == expected
