"""Test Module."""
from incolume.py.coding_dojo_jedi.dojo20190129.dojo20190129 import dojo20190129


def test_moedas_1() -> None:
    """Test for 1.0 BRL."""
    (notas, moedas) = dojo20190129.moedas(1)
    assert notas == [0, 0, 0, 0, 0, 0]
    assert moedas == [1, 0, 0, 0, 0, 0]


def test_moedas_050() -> None:
    """Test for 50.0 BRL."""
    (notas, moedas) = dojo20190129.moedas(0.5)
    assert notas == [0, 0, 0, 0, 0, 0]
    assert moedas == [0, 1, 0, 0, 0, 0]


def test_moedas_150() -> None:
    """Test for 150.0 BRL."""
    (notas, moedas) = dojo20190129.moedas(1.5)
    assert notas == [0, 0, 0, 0, 0, 0]
    assert moedas == [1, 1, 0, 0, 0, 0]


def test_moedas_191() -> None:
    """Test for 191.0 BRL."""
    (notas, moedas) = dojo20190129.moedas(1.91)
    assert notas == [0, 0, 0, 0, 0, 0]
    assert moedas == [1, 1, 1, 1, 1, 1]


def test_moedas_192() -> None:
    """Test for 192.0 BRL."""
    (notas, moedas) = dojo20190129.moedas(1.92)
    assert notas == [0, 0, 0, 0, 0, 0]
    assert moedas == [1, 1, 1, 1, 1, 2]


def test_notas_100() -> None:
    """Test for 100.0 BRL."""
    (notas, moedas) = dojo20190129.moedas(100)
    assert notas == [1, 0, 0, 0, 0, 0]
    assert moedas == [0, 0, 0, 0, 0, 0]


def test_notas_101() -> None:
    """Test for 101.0 BRL."""
    (notas, moedas) = dojo20190129.moedas(101)
    assert notas == [1, 0, 0, 0, 0, 0]
    assert moedas == [1, 0, 0, 0, 0, 0]


def test_notas_101_92() -> None:
    """Test for 101.92 BRL."""
    (notas, moedas) = dojo20190129.moedas(101.92)
    assert notas == [1, 0, 0, 0, 0, 0]
    assert moedas == [1, 1, 1, 1, 1, 2]


def test_notas_576_73() -> None:
    """Test for 576.73 BRL."""
    (notas, moedas) = dojo20190129.moedas(576.73)
    assert notas == [5, 1, 1, 0, 1, 0]
    assert moedas == [1, 1, 0, 2, 0, 3]


def test_notas_0() -> None:
    """Test for 0.0 BRL."""
    (notas, moedas) = dojo20190129.moedas(0.0)
    assert notas == [0, 0, 0, 0, 0, 0]
    assert moedas == [0, 0, 0, 0, 0, 0]
