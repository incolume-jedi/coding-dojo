"""Dojo validação de CPF realizado em 02/05/2024."""

import pytest
from incolume.py.coding_dojo_jedi.dojo20240502 import check_cpf, verify_cpf
from typing import ClassVar


class TestCheckCPF:
    """CheckCPF tests."""

    elements: ClassVar = [
        ('000.000.001-91', True),
        ('000.000.002-72', True),
        ('000.000.003-53', True),
        ('000.000.000-00', False),
        ('123.456.789-12', False),
        ('529.982.247-25', True),
        ('777.777.777-77', False),
        (49691275228, True),
        (56681418104, True),
        ('777.777.777', False),
        ('', False),
        (45136754702, True),
    ]

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        elements,
    )
    def test_check_cpf(self, entrance, expected):
        """Test it."""
        assert check_cpf(entrance) == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        elements,
    )
    def test_verify_cpf(self, entrance, expected):
        """Test it."""
        assert verify_cpf(entrance) == expected
