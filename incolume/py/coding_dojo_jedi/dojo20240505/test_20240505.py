"""Module."""

from typing import NoReturn

import pytest

# !/usr/bin/env python
# -*- coding: utf-8 -*-
from . import CPF

__author__ = '@britodfbr'  # pragma: no cover


class TestCPFInstances:
    """Case tests."""

    def test_instance(self):
        """Test it."""
        cpf = CPF('00000000191')
        assert isinstance(cpf, CPF)

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            (10000000001, '100.000.000-01'),
            (52998224725, '529.982.247-25'),
            ('52998224725', '529.982.247-25'),
            ('529.982.247-25', '529.982.247-25'),
        ],
    )
    def test_format(self, entrance, expected) -> NoReturn:
        """Test it."""
        assert CPF(entrance).cpf_number == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            ('000.000.001-91', True),
            ('000.000.001-92', False),
            ('123.456.789-07', False),
            ('529.982.247-25', True),
            (52998224725, True),
        ],
    )
    def test_valid_method(self, entrance, expected):
        """Test it."""
        cpf = CPF(entrance)
        assert cpf.is_valid() == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            ('000.000.001-91', True),
            ('000.000.001-92', False),
            ('123.456.789-07', False),
            ('529.982.247-25', True),
            (52998224725, True),
        ],
    )
    def test_valid_instance(self, entrance, expected):
        """Test it."""
        cpf = CPF(entrance)
        assert bool(cpf) == expected

    @pytest.mark.parametrize(
        'entrance',
        [
            '',
            None,
            111,
            111111111111,
            'abcdefghij',
        ],
    )
    def test_exceptions(self, entrance):
        """Test it."""
        with pytest.raises(
            expected_exception=ValueError,
            match='Informe 11 digitos numericos distintos.',
        ):
            CPF(entrance)

    @pytest.mark.parametrize(
        'entrance forma expected'.split(),
        [
            (12345678900, 's', '12345678900'),
            (12345678900, 'r', 'CPF(123.456.789-00)'),
        ],
    )
    def test_instance_format(self, entrance, forma, expected):
        """Test it."""
        cpf = CPF(entrance)
        assert f'{cpf:{forma}}' == expected
