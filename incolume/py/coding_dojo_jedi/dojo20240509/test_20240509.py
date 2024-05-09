"""Module test dojo."""

import pytest
from incolume.py.coding_dojo_jedi.dojo20240509 import Numeros
from typing import NoReturn


class TestNumero:
    """Caso de teste Numero."""

    @pytest.mark.parametrize(
        [
            'entrance',
            'expected',
        ],
        [
            ('CMLXXXVII', 987),
            ('MCMLXXVIII', 1978),
            ('I', 1),
            ('II', 2),
            ('IV', 4),
            ('IX', 9),
            ('C', 100),
            ('L', 50),
            ('M', 1000),
            ('MCMLXXXVIII', 1988),
            ('MMIX', 2009),
            ('MMXI', 2011),
            ('D', 500),
            ('MD', 1500),
        ],
    )
    def test_from_roman(self, entrance, expected) -> NoReturn:
        """Testa resultado de conversão de romano para arábico."""
        obj = Numeros()
        assert obj.from_roman(entrance) == expected

    @pytest.mark.parametrize(
        [
            'entrance',
            'expected',
        ],
        [
            (987, 'CMLXXXVII'),
            (1978, 'MCMLXXVIII'),
            (1, 'I'),
            (2, 'II'),
            (4, 'IV'),
            (9, 'IX'),
            (100, 'C'),
            (50, 'L'),
            (1000, 'M'),
            (1988, 'MCMLXXXVIII'),
            (2009, 'MMIX'),
            (2011, 'MMXI'),
            (500, 'D'),
            (1500, 'MD'),
        ],
    )
    def test_to_roman(self, entrance, expected) -> NoReturn:
        """Testa resultado de conversão de arábico para romano."""
        obj = Numeros()
        assert obj.to_roman(entrance) == expected
