"""Module."""

__author__ = '@britodfbr'  # pragma: no cover

import pytest

from incolume.py.coding_dojo_jedi.dojo20240530 import validar_cnpj


@pytest.mark.parametrize(
    'entrance expected'.split(),
    [
        ('abcdefghijklmn', False),
        ('123', False),
        (123, False),
        ('', False),
        (None, False),
        ('12345678901234', False),
        ('11222333000100', False),
        (11222333000100, False),
        ('11222333000181', True),
        (11222333000181, True),
        ('11.222.333/0001-81', True),
        ('  11 222 333 0001 81  ', True),
    ],
)
def test_cnpj(entrance, expected):
    """Validar função."""
    assert validar_cnpj(entrance) == expected
