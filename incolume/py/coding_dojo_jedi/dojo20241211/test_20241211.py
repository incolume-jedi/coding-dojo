"""Test module."""

from typing import ClassVar, NoReturn
import incolume.py.coding_dojo_jedi.dojo20241211 as pkg
import pytest
from unittest import mock


class TestCase:
    """Test case class."""

    t0: ClassVar = None

    @pytest.mark.parametrize(
        'entrance expected raises'.split(),
        [
            pytest.param(123456789001, '12345678900188', {}, marks=[]),
            pytest.param(112223330001, '11222333000181', None, marks=[]),
            pytest.param('112223330001', '11222333000181', None, marks=[]),
            pytest.param('11.222.333/0001', '11222333000181', None, marks=[]),
            pytest.param('11 222 333 0001', '11222333000181', None, marks=[]),
            pytest.param(
                '11 222 333 OOO1',
                '11222333000181',
                {
                    'expected_exception': ValueError,
                    'match': 'Quantidade insuficiente de números',
                },
                marks=[],
            ),
            pytest.param(None, '55555555555576', {}, marks=[]),
            pytest.param('', '55555555555576', {}, marks=[]),
        ],
    )
    def test_generate(self, entrance, expected, raises) -> NoReturn:
        """Unittest."""
        with mock.patch('secrets.randbelow', return_value=5):
            if raises:
                with pytest.raises(**raises):
                    pkg.gen_cnpj_verify(entrance)
            else:
                assert pkg.gen_cnpj_verify(entrance) == expected
