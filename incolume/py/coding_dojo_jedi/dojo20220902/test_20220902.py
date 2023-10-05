from sys import version_info

import pytest
from dojo20220902 import trocar_dinheiro


@pytest.mark.skip(reason='replaced for pytest.mark.parametrize')
def test_moedas_150():
    (notas, moedas) = trocar_dinheiro(1.5)
    assert notas == [0, 0, 0, 0, 0, 0, 0]
    assert moedas == [1, 1, 0, 0, 0, 0]


@pytest.mark.skip(reason='replaced for pytest.mark.parametrize')
def test_moedas_191():
    (notas, moedas) = trocar_dinheiro(1.91)
    assert notas == [0, 0, 0, 0, 0, 0, 0]
    assert moedas == [1, 1, 1, 1, 1, 1]


@pytest.mark.skip(reason='replaced for pytest.mark.parametrize')
def test_moedas_192():
    (notas, moedas) = trocar_dinheiro(1.92)
    assert notas == [0, 0, 0, 0, 0, 0, 0]
    assert moedas == [1, 1, 1, 1, 1, 2]


@pytest.mark.skip(reason='replaced for pytest.mark.parametrize')
def test_notas_101():
    (notas, moedas) = trocar_dinheiro(101)
    assert notas == [0, 1, 0, 0, 0, 0, 0]
    assert moedas == [1, 0, 0, 0, 0, 0]


@pytest.mark.skip(reason='replaced for pytest.mark.parametrize')
def test_notas_101_92():
    (notas, moedas) = trocar_dinheiro(101.92)
    assert notas == [0, 1, 0, 0, 0, 0, 0]
    assert moedas == [1, 1, 1, 1, 1, 2]


@pytest.mark.skip(reason='replaced for pytest.mark.parametrize')
def test_notas_0():
    (notas, moedas) = trocar_dinheiro(0.0)
    assert notas == [0, 0, 0, 0, 0, 0, 0]
    assert moedas == [0, 0, 0, 0, 0, 0]


@pytest.mark.skipif(
    version_info < (3, 8, 0),
    reason='This run only Python 3.8+',
)
@pytest.mark.parametrize(
    ('entrance', 'expected'),
    (
        (0, ([0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0])),
        (101, ([0, 1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0])),
        (101.01, ([0, 1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 1])),
        (111.11, ([0, 1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1])),
        (101.92, ([0, 1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 2])),
        (1.92, ([0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 2])),
        (1.91, ([0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1])),
        (1.00, ([0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0])),
        (1, ([0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0])),
        (1.50, ([0, 0, 0, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0])),
        (0.5, ([0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0])),
        (0.25, ([0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0])),
        (0.1, ([0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0])),
        (0.05, ([0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0])),
        (0.01, ([0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1])),
        (2.00, ([0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0])),
        (5.00, ([0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0])),
        (10.00, ([0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0])),
        (20.00, ([0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0])),
        (50.00, ([0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0])),
        (100.00, ([0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0])),
        (200.00, ([1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0])),
        (576.73, ([2, 1, 1, 1, 0, 1, 0], [1, 1, 0, 2, 0, 3])),
        (4.00, ([0, 0, 0, 0, 0, 0, 2], [0, 0, 0, 0, 0, 0])),
        (91.01, ([0, 0, 1, 2, 0, 0, 0], [1, 0, 0, 0, 0, 1])),
        (386.96, ([1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 2, 0, 1])),
        (387.96, ([1, 1, 1, 1, 1, 1, 1], [0, 1, 1, 2, 0, 1])),
        (387.95, ([1, 1, 1, 1, 1, 1, 1], [0, 1, 1, 2, 0, 0])),
        (388.91, ([1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1])),
        (777.82, ([3, 1, 1, 1, 0, 1, 1], [0, 1, 1, 0, 1, 2])),
        (6.0, ([0, 0, 0, 0, 0, 1, 0], [1, 0, 0, 0, 0, 0])),
        (311.11, ([1, 1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1])),
        (262.61, ([1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1])),
        (126.30, ([0, 1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0])),
    ),
)
def test_trocar_dinheiro(entrance, expected):
    """Teste para troca de notas.

    calculo para o menor número de notas e moedas
    possíveis no qual o valor pode ser decomposto.
    """
    assert trocar_dinheiro(entrance) == expected
