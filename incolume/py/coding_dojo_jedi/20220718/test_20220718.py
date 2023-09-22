from math import pi

import dojo20220718
import pytest


def test_ascii():
    assert 1 + 1 == 2
    assert f'{pi:.04f}' == '3.1416'


@pytest.mark.parametrize(
    ('entrada', 'esperado'),
    (
        (65, 'A'),
        (70, 'F'),
        (97, 'a'),
        ('97', 'a'),
    ),
)
def test_ascii_0(entrada, esperado):
    assert dojo20220718.get_char(entrada) == esperado


# Validação de exceção
def test_ascii_exception_0():
    with pytest.raises(
        ValueError,
        match='num deve ser um número entre 0 e 0x10ffff.',
    ):
        assert dojo20220718.get_char(-1)


def test_ascii_exception_1():
    with pytest.raises(
        ValueError,
        match='num deve ser um número entre 0 e 0x10ffff.',
    ):
        assert dojo20220718.get_char('a')
