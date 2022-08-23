import pytest
from dojo import table, calc, show



@pytest.mark.parametrize(
    'entrance expected'.split(),
    (
        (1, 2.18),
    )
)
def test_calc(entrance, expected):
    assert calc(entrance) == expected

@pytest.mark.parametrize(
    'expected',
    (
        2.18,
        218,
        109,
        70*218/100,
    )
)
def test_table(expected):
    assert expected in table().values()

@pytest.mark.parametrize(
    'expected',
    (
        '   1 = R$   2.18',
        'R$ 109.00',
        '70 = R$ 152.60',
    )
)
def test_show(capsys, expected):
    show()
    captured = capsys.readouterr()
    assert captured.err == ''
    assert  expected in captured.out

