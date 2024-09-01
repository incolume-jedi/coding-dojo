"""Test for dojo TDD Pytest."""

# tests.py
# -*- encode: utf-8 -*-

import re
from sys import version_info

import pytest
from incolume.py.coding_dojo_jedi.dojo20220720.dojo20220720 import calculadora
from tests import Py38


@Py38
@pytest.mark.parametrize(
    ['entrance', 'expected'],
    [
        (('+', 3, '4'), 7),
        (('+', 3, 4), 7),
        (('-', 3.0, 4), -1.0),
        (('-', '3', 4), -1),
        (('*', 3, '4'), 12),
        (('*', 3, '4.0'), 12.0),
        (('/', 3, '4'), 0.75),
        (('/', 4, 4.0), 1.0),
        (('/', 4, 3.0), 1.3333333333333333),
        (('%', 4, 3), 1),
        (('%', 12, 7), 5),
        (('**', 3, 4), 81),
        (('**', 81, (1 / 4)), 3),
    ],
)
def test_calculadora(entrance, expected) -> None:
    """Testes para resultado das operações."""
    assert calculadora(*entrance) == expected


@pytest.mark.skipif(
    version_info <= (3, 8, 0),
    reason='This run only Python 3.8 or higher',
)
@pytest.mark.parametrize(
    ['entrance', 'expected'],
    [
        (
            ('^', 3, 5),
            {
                'expected_exception': ValueError,
                'match': re.escape('Operador inválido. Use: + - * ** / // %'),
            },
        ),
        (
            ('/', 3, 0),
            {
                'expected_exception': ValueError,
                'match': r'.*y deve ser diferente 0.*',
            },
        ),
        (
            ('/', '3', 0),
            {
                'expected_exception': ValueError,
                'match': r'.*y deve ser diferente 0.*',
            },
        ),
        (
            ('/', 3, '0'),
            {
                'expected_exception': ValueError,
                'match': r'.*y deve ser diferente 0.*',
            },
        ),
        (
            ('/', '3', '0'),
            {
                'expected_exception': ValueError,
                'match': r'.*y deve ser diferente 0.*',
            },
        ),
        (
            ('//', 3, 0),
            {
                'expected_exception': ValueError,
                'match': r'.*y deve ser diferente 0.*',
            },
        ),
        (
            ('//', '3', 0),
            {
                'expected_exception': ValueError,
                'match': r'.*y deve ser diferente 0.*',
            },
        ),
        (
            ('//', 3, '0'),
            {
                'expected_exception': ValueError,
                'match': r'.*y deve ser diferente 0.*',
            },
        ),
        (
            ('//', '3', '0'),
            {
                'expected_exception': ValueError,
                'match': r'.*y deve ser diferente 0.*',
            },
        ),
        (
            ('+', 'a', 'b'),
            {
                'expected_exception': TypeError,
                'match': r'.*x e y devem ser valores numéricos reais.*',
            },
        ),
        (
            ('+', '0', 'b'),
            {
                'expected_exception': TypeError,
                'match': r'.*x e y devem ser valores numéricos reais.*',
            },
        ),
        (
            ('+', 'a', '0'),
            {
                'expected_exception': TypeError,
                'match': r'.*x e y devem ser valores numéricos reais.*',
            },
        ),
        (
            ('+', (3 + 0j), (2 + 0j)),
            {
                'expected_exception': TypeError,
                'match': r'.*x e y devem ser valores numéricos reais.*',
            },
        ),
    ],
)
def test_calculadora_except(entrance, expected) -> None:
    """Test for exceptions."""
    with pytest.raises(**expected):
        calculadora(*entrance)
