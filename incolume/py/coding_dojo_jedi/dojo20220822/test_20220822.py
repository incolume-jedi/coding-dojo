"""Unittest for dojo."""
import pytest

from incolume.py.coding_dojo_jedi.dojo20220822.dojo20220822 import (
    calc,
    show,
    table,
    table_p2,
)


@pytest.mark.parametrize(
    'entrance expected'.split(),
    [
        (1, 1.99),
        (2, 3.98),
        (50, 99.50),
    ],
)
def test_table0(entrance, expected) -> None:
    """Test table."""
    assert table(entrance) == expected


def test_tabela() -> None:
    """Test table."""
    assert {x: table(x) for x in range(1, 51)} == {
        x: x * 1.99 for x in range(1, 51)
    }


@pytest.mark.parametrize('entrance expected'.split(), [(1, 2.18),])
def test_calc(entrance, expected) -> None:
    """Test calc."""
    assert calc(entrance) == expected


@pytest.mark.parametrize(
    'expected',
    [
        2.18,
        218,
        109,
        70 * 218 / 100,
    ],
)
def test_table(expected) -> None:
    """Test table."""
    assert expected in table_p2().values()


@pytest.mark.parametrize(
    'expected',
    [
        '   1 = R$   2.18',
        'R$ 109.00',
        '70 = R$ 152.60',
    ],
)
def test_show(capsys, expected) -> None:
    """Test show."""
    show()
    captured = capsys.readouterr()
    assert expected in captured.out
