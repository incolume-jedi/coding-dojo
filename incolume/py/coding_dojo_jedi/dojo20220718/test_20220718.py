"""Testes para dojo - Pegar valor ascii do caracter."""

from math import pi

import pytest

from incolume.py.coding_dojo_jedi.dojo20220718 import dojo20220718


@pytest.mark.parametrize(
    'entrance expected'.split(),
    [
        (sum([1, 1]), 2),
        (f'{pi:.04f}', '3.1416'),
    ],
)
def test_ascii(entrance, expected) -> None:
    """ASCII test."""
    assert entrance == expected


@pytest.mark.parametrize(
    ['entrada', 'esperado'],
    [
        (65, 'A'),
        (70, 'F'),
        (97, 'a'),
        ('97', 'a'),
    ],
)
def test_ascii_0(entrada: int, esperado: str) -> None:
    """Teste para caminho feliz."""
    assert dojo20220718.get_char(entrada) == esperado


# Validação de exceção
def test_ascii_exception_0() -> None:
    """Teste de exceção para inteiros negativos."""
    with pytest.raises(
        ValueError,
        match='num deve ser um número entre 0 e 0x10ffff.',
    ):
        assert dojo20220718.get_char(-1)


def test_ascii_exception_1() -> None:
    """Teste de exceção para strings."""
    with pytest.raises(
        ValueError,
        match='num deve ser um número entre 0 e 0x10ffff.',
    ):
        assert dojo20220718.get_char('a')  # type: ignore[arg-type]
