from dojo import index
import pytest


@pytest.mark.parametrize(
    ('entrance', 'expected'),
    (
        (('Python', 0), 'P'),
        (('casa', 6), 's'),
        (('Brasil', 1), 'r'),
        (('Brasília', 4), 'í'),
        (('dojo', 2), 'j'),
        (('xpto', 1026), 't'),
        (('xpto', 2048), 'x'),
        (('xpto', 3073), 'p'),
        (('xpto', 65536), 'x'),
    )
)
def test_index(entrance, expected):
    assert index(*entrance) == expected
