"""Module tests dojo."""

import pytest
from . import num_feliz


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
