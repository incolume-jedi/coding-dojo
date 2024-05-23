"""Module tests dojo."""

import pytest
from . import num_feliz, list_feliz


class TestNFeliz:
    """Caso de teste para números felizes."""

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            (1, [1]),
            (7, [1, 7]),
            (10, [1, 7, 10]),
            (
                100,
                [
                    1,
                    7,
                    10,
                    13,
                    19,
                    23,
                    28,
                    31,
                    32,
                    44,
                    49,
                    68,
                    70,
                    79,
                    82,
                    86,
                    91,
                    94,
                    97,
                    100,
                ],
            ),
        ],
    )
    def test_menores_que(self, entrance, expected):
        """Testa lista de numeros felizes menores que número passado."""
        assert num_feliz(entrance) == expected

    @pytest.mark.parametrize(
        'entrance',
        [
            1,
            2,
            5,
            25,
        ],
    )
    def test_quantia_0(self, entrance):
        """Test quantidade de números felizes retornados."""
        assert len(list_feliz(entrance)) == entrance

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            (2, [1, 7]),
            (5, [1, 7, 10, 13, 19]),
            (
                25,
                [
                    1,
                    7,
                    10,
                    13,
                    19,
                    23,
                    28,
                    31,
                    32,
                    44,
                    49,
                    68,
                    70,
                    79,
                    82,
                    86,
                    91,
                    94,
                    97,
                    100,
                    103,
                    109,
                    129,
                    130,
                    133,
                ],
            ),
        ],
    )
    def test_quantia_1(self, entrance, expected):
        """Test quantidade de números felizes retornados."""
        assert list_feliz(entrance) == expected
