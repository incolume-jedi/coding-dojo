"""Module."""
# !/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from . import create_cpf

__author__ = '@britodfbr'  # pragma: no cover


class TestCPFCreate:
    """Class test."""

    @pytest.mark.parametrize(
        'entrance',
        [
            None,
            '',
            000000000,
            111111111,
        ],
    )
    def test_create_cpf_exceptions(self, entrance):
        """TEst it."""
        with pytest.raises(
            expected_exception=ValueError,
            match=(
                'O número de entrada deve conter 9 digitos,'
                ' com ao menos 1 diferente.'
            ),
        ):
            create_cpf(entrance)

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            ('000.000.001', '000.000.001-91'),
            (123456789, '123.456.789-09'),
            ('529.982.247', '529.982.247-25'),
            (529982247, '529.982.247-25'),
        ],
    )
    def test_create_cpf(self, entrance, expected):
        """TEst it."""
        assert create_cpf(entrance) == expected
