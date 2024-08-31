"""Test module."""

from typing import NoReturn
from unittest import mock
import incolume.py.coding_dojo_jedi.dojo20240830 as pkg
import pytest


class TestCase:
    """Test case class."""

    @pytest.mark.parametrize(
        'funct entrance expected'.split(),
        [
            pytest.param(
                pkg.view,
                None,
                'Digite a string no qual quer ler quais'
                ' letras do alfabetos elas possui: ',
                marks=[pytest.mark.skip],
            ),
            pytest.param(pkg.view, '', ''),
            pytest.param(pkg.view, 'oi: ', ''),
        ],
    )
    def test_0(self, funct, entrance, expected, capsys) -> NoReturn:
        """Unittest."""
        with mock.patch('builtins.input', return_value=''):
            funct(entrance)
            out, _ = capsys.readouterr()
            assert out == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            ('abc', {'a': 1, 'b': 1, 'c': 1}),
            ('mississipi', {'m': 1, 'i': 4, 's': 4, 'p': 1}),
        ],
    )
    def test_1(self, entrance, expected):
        """Test unit."""
        assert pkg.dojo(entrance) == expected
