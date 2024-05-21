"""Testes para dojo "palindrome string"."""

import pytest

from incolume.py.coding_dojo_jedi.dojo20220717 import dojo20220717


def test_dojo202207171() -> None:
    """Testar de Python é palindrome."""
    assert dojo20220717.palindrome('Python') is False


def test_dojo202207172() -> None:
    """Testar se anna é palindrome."""
    assert dojo20220717.palindrome('anna') is True


@pytest.mark.parametrize(
    ['entrada', 'esperado'],
    [
        ('walter', False),
        (12321, True),
        (123456, False),
        ('ada', True),
    ],
)
def test_dojo1(*, entrada: str, esperado: bool) -> None:
    """Testar multiplas possibilidades da função palindrome."""
    assert dojo20220717.palindrome(entrada) == esperado


@pytest.mark.parametrize(
    ['entrada', 'esperado'],
    [
        ('walter', False),
        (12321, True),
        (123456, False),
        ('ada', True),
    ],
)
def test_dojo2(*, entrada: str, esperado: bool) -> None:
    """Testar multiplas possibilidades da função palindrome."""
    assert dojo20220717.palindrome0(entrada) == esperado
