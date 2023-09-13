from dojo import table

import pytest

@pytest.mark.parametrize(
    'entrance expected'.split(),
    (
        (1, 1.99),
        (2, 3.98),
        (50, 99.50),
    )
)
def test_table(entrance, expected):
    assert table(entrance) == expected


def test_tabela():
    assert {x: table(x) for x in range(1, 51)} == {x: x * 1.99 for x in range(1, 51)}
