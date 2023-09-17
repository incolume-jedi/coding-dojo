from dojo20220822 import table, table_p2, calc, show

import pytest


@pytest.mark.parametrize(
    'entrance expected'.split(),
    (
        (1, 1.99),
        (2, 3.98),
        (50, 99.50),
    ),
)
def test_table0(entrance, expected):
    assert table(entrance) == expected


def test_tabela():
    assert {x: table(x) for x in range(1, 51)} == {
        x: x * 1.99 for x in range(1, 51)
    }


@pytest.mark.parametrize('entrance expected'.split(), ((1, 2.18),))
def test_calc(entrance, expected):
    assert calc(entrance) == expected


@pytest.mark.parametrize(
    'expected',
    (
        2.18,
        218,
        109,
        70 * 218 / 100,
    ),
)
def test_table(expected):
    assert expected in table_p2().values()


@pytest.mark.parametrize(
    'expected',
    (
        '   1 = R$   2.18',
        'R$ 109.00',
        '70 = R$ 152.60',
    ),
)
def test_show(capsys, expected):
    show()
    captured = capsys.readouterr()
    assert captured.err == ''
    assert expected in captured.out
