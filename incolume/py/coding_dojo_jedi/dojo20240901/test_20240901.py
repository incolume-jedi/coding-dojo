"""Tests for this dojo."""

import pytest
import incolume.py.coding_dojo_jedi.dojo20240901 as pkg


class TestCase:
    """Class case test."""

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            (1, 'um'),
            (19, 'dezenove'),
            (7, 'sete'),
            (15, 'quinze'),
            (35, 'trinta e cinco'),
            (999, 'novecentos e noventa e nove'),
            (1001, 'mil e um'),
            (1978, 'mil e novecentos e setenta e oito'),
            (10000, 'dez mil'),
            (9099, 'nove mil e noventa e nove'),
            (3906, 'três mil e novecentos e seis'),
        ],
    )
    def test_0(self, entrance, expected):
        """Unit test."""
        assert pkg.dojo(entrance) == expected
