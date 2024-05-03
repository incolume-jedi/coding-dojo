"""Test Notas e Moedas POO."""

import pytest

from incolume.py.coding_dojo_jedi.dojo20231113.dojo20231113 import TrocaNotas


class TestCase:
    """Testa classe TrocaNotas."""

    @pytest.fixture()
    def obj_trocanotas(self) -> TrocaNotas:
        """Retorna um objeto TrocaNotas."""
        return TrocaNotas()

    @pytest.mark.parametrize(
        ['entrance', 'expected'],
        [
            ('cedulas', [200, 100, 50, 20, 10, 5, 2]),
            ('moedas', [1.0, 0.5, 0.25, 0.1, 0.05, 0.01]),
        ],
    )
    def test_base_monetaria(self, obj_trocanotas, entrance, expected) -> None:
        """Testa base monetaria da classe."""
        assert getattr(obj_trocanotas, entrance) == expected

    @pytest.mark.parametrize(
        ['entrance', 'expected'],
        [
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
        ],
    )
    def test_trocar_dinheiro0(
        self,
        obj_trocanotas,
        entrance,
        expected,
    ) -> None:
        """Teste para troca de notas.

        calculo para o menor número de notas e moedas
        possíveis no qual o valor pode ser decomposto.
        """
        assert obj_trocanotas.trocar(entrance) == expected

    @pytest.mark.parametrize(
        ['entrance', 'expected'],
        [
            pytest.param(
                0,
                ([0, 0, 0, 0, 0], [0, 0, 0, 0]),
            ),
            pytest.param(
                101,
                ([1, 0, 0, 0, 1], [0, 0, 0, 0]),
            ),
            pytest.param(
                101.01,
                ([1, 0, 0, 0, 1], [0, 0, 0, 1]),
            ),
            pytest.param(
                111.11,
                ([1, 0, 1, 0, 1], [0, 1, 0, 1]),
            ),
            pytest.param(
                101.92,
                ([1, 0, 0, 0, 1], [1, 4, 0, 2]),
            ),
            pytest.param(
                1.92,
                ([0, 0, 0, 0, 1], [1, 4, 0, 2]),
            ),
            pytest.param(
                1.91,
                ([0, 0, 0, 0, 1], [1, 4, 0, 1]),
            ),
            pytest.param(
                1.00,
                ([0, 0, 0, 0, 1], [0, 0, 0, 0]),
            ),
            pytest.param(
                1,
                ([0, 0, 0, 0, 1], [0, 0, 0, 0]),
            ),
            pytest.param(
                1.50,
                ([0, 0, 0, 0, 1], [1, 0, 0, 0]),
            ),
            pytest.param(
                0.5,
                ([0, 0, 0, 0, 0], [1, 0, 0, 0]),
            ),
            pytest.param(
                0.25,
                ([0, 0, 0, 0, 0], [0, 2, 1, 0]),
            ),
            pytest.param(
                0.1,
                ([0, 0, 0, 0, 0], [0, 1, 0, 0]),
            ),
            pytest.param(
                0.05,
                ([0, 0, 0, 0, 0], [0, 0, 1, 0]),
            ),
            pytest.param(
                0.01,
                ([0, 0, 0, 0, 0], [0, 0, 0, 1]),
            ),
            pytest.param(
                2.00,
                ([0, 0, 0, 0, 2], [0, 0, 0, 0]),
            ),
            pytest.param(
                5.00,
                ([0, 0, 0, 1, 0], [0, 0, 0, 0]),
            ),
            pytest.param(
                10.00,
                (
                    [0, 0, 1, 0, 0],
                    [
                        0,
                        0,
                        0,
                        0,
                    ],
                ),
            ),
            pytest.param(
                20.00,
                ([0, 0, 2, 0, 0], [0, 0, 0, 0]),
            ),
            pytest.param(
                50.00,
                (
                    [0, 1, 0, 0, 0],
                    [
                        0,
                        0,
                        0,
                        0,
                    ],
                ),
            ),
            pytest.param(
                100.00,
                ([1, 0, 0, 0, 0], [0, 0, 0, 0]),
            ),
            pytest.param(
                200.00,
                ([2, 0, 0, 0, 0], [0, 0, 0, 0]),
            ),
            pytest.param(
                576.73,
                ([5, 1, 2, 1, 1], [1, 2, 0, 3]),
            ),
            pytest.param(
                4.00,
                ([0, 0, 0, 0, 4], [0, 0, 0, 0]),
            ),
            pytest.param(
                91.01,
                ([0, 1, 4, 0, 1], [0, 0, 0, 1]),
            ),
            pytest.param(
                386.96,
                ([3, 1, 3, 1, 1], [1, 4, 1, 1]),
            ),
            pytest.param(
                387.96,
                ([3, 1, 3, 1, 2], [1, 4, 1, 1]),
            ),
            pytest.param(
                387.95,
                ([3, 1, 3, 1, 2], [1, 4, 1, 0]),
            ),
            pytest.param(
                388.91,
                ([3, 1, 3, 1, 3], [1, 4, 0, 1]),
            ),
            pytest.param(777.82, ([7, 1, 2, 1, 2], [1, 3, 0, 2])),
            pytest.param(
                6.0,
                ([0, 0, 0, 1, 1], [0, 0, 0, 0]),
            ),
            pytest.param(
                311.11,
                ([3, 0, 1, 0, 1], [0, 1, 0, 1]),
            ),
            pytest.param(
                262.61,
                ([2, 1, 1, 0, 2], [1, 1, 0, 1]),
            ),
            pytest.param(
                126.30,
                ([1, 0, 2, 1, 1], [0, 3, 0, 0]),
                marks=pytest.mark.skip(reason='Falso Positivo'),
            ),
        ],
    )
    def test_trocar_dinheiro1(
        self,
        obj_trocanotas,
        entrance,
        expected,
    ) -> None:
        """Teste para troca de notas.

        calculo para o menor número de notas e moedas
        possíveis no qual o valor pode ser decomposto.
        """
        obj_trocanotas.cedulas = [100, 50, 10, 5, 1]
        obj_trocanotas.moedas = [0.5, 0.1, 0.05, 0.01]

        assert obj_trocanotas.trocar(entrance) == expected

    # @pytest.mark.skip()
    @pytest.mark.parametrize(
        ['entrance', 'expected'],
        [
            pytest.param(
                0,
                ([0, 0, 0, 0, 0], [0, 0, 0, 0]),
            ),
            pytest.param(
                101,
                ([1, 0, 0, 0, 1], [0, 0, 0, 0]),
            ),
            pytest.param(
                101.01,
                ([1, 0, 0, 0, 1], [0, 0, 0, 1]),
            ),
            pytest.param(
                111.11,
                ([1, 0, 1, 0, 1], [0, 1, 0, 1]),
            ),
            pytest.param(
                101.92,
                ([1, 0, 0, 0, 1], [1, 4, 0, 2]),
            ),
            pytest.param(
                1.92,
                ([0, 0, 0, 0, 1], [1, 4, 0, 2]),
            ),
            pytest.param(
                1.91,
                ([0, 0, 0, 0, 1], [1, 4, 0, 1]),
            ),
            pytest.param(
                1.00,
                ([0, 0, 0, 0, 1], [0, 0, 0, 0]),
            ),
            pytest.param(
                1,
                ([0, 0, 0, 0, 1], [0, 0, 0, 0]),
            ),
            pytest.param(
                1.50,
                ([0, 0, 0, 0, 1], [1, 0, 0, 0]),
            ),
            pytest.param(
                0.5,
                ([0, 0, 0, 0, 0], [1, 0, 0, 0]),
            ),
            pytest.param(
                0.25,
                ([0, 0, 0, 0, 0], [0, 2, 1, 0]),
            ),
            pytest.param(
                0.1,
                ([0, 0, 0, 0, 0], [0, 1, 0, 0]),
            ),
            pytest.param(
                0.05,
                ([0, 0, 0, 0, 0], [0, 0, 1, 0]),
            ),
            pytest.param(
                0.01,
                ([0, 0, 0, 0, 0], [0, 0, 0, 1]),
            ),
            pytest.param(
                2.00,
                ([0, 0, 0, 0, 2], [0, 0, 0, 0]),
            ),
            pytest.param(
                5.00,
                ([0, 0, 0, 1, 0], [0, 0, 0, 0]),
            ),
            pytest.param(
                10.00,
                (
                    [0, 0, 1, 0, 0],
                    [
                        0,
                        0,
                        0,
                        0,
                    ],
                ),
            ),
            pytest.param(
                20.00,
                ([0, 0, 2, 0, 0], [0, 0, 0, 0]),
            ),
            pytest.param(
                50.00,
                (
                    [0, 1, 0, 0, 0],
                    [
                        0,
                        0,
                        0,
                        0,
                    ],
                ),
            ),
            pytest.param(
                100.00,
                ([1, 0, 0, 0, 0], [0, 0, 0, 0]),
            ),
            pytest.param(
                200.00,
                ([2, 0, 0, 0, 0], [0, 0, 0, 0]),
            ),
            pytest.param(
                576.73,
                ([5, 1, 2, 1, 1], [1, 2, 0, 3]),
            ),
            pytest.param(
                4.00,
                ([0, 0, 0, 0, 4], [0, 0, 0, 0]),
            ),
            pytest.param(
                91.01,
                ([0, 1, 4, 0, 1], [0, 0, 0, 1]),
            ),
            pytest.param(
                386.96,
                ([3, 1, 3, 1, 1], [1, 4, 1, 1]),
            ),
            pytest.param(
                387.96,
                ([3, 1, 3, 1, 2], [1, 4, 1, 1]),
            ),
            pytest.param(
                387.95,
                ([3, 1, 3, 1, 2], [1, 4, 1, 0]),
            ),
            pytest.param(
                388.91,
                ([3, 1, 3, 1, 3], [1, 4, 0, 1]),
            ),
            pytest.param(777.82, ([7, 1, 2, 1, 2], [1, 3, 0, 2])),
            pytest.param(
                6.0,
                ([0, 0, 0, 1, 1], [0, 0, 0, 0]),
            ),
            pytest.param(
                311.11,
                ([3, 0, 1, 0, 1], [0, 1, 0, 1]),
            ),
            pytest.param(
                262.61,
                ([2, 1, 1, 0, 2], [1, 1, 0, 1]),
            ),
            pytest.param(
                126.30,
                ([1, 0, 2, 1, 1], [0, 3, 0, 0]),
                marks=pytest.mark.skip(reason='Falso Positivo'),
            ),
        ],
    )
    def test_trocar_dinheiro2(self, entrance, expected) -> None:
        """Teste para troca de notas.

        calculo para o menor número de notas e moedas
        possíveis no qual o valor pode ser decomposto.
        """
        obj = TrocaNotas(
            cedulas=[100, 50, 10, 5, 1],
            moedas=[0.5, 0.1, 0.05, 0.01],
        )
        assert obj.trocar(entrance) == expected
