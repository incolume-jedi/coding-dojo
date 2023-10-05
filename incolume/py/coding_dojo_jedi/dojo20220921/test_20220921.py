import pytest

from incolume.py.coding_dojo_jedi.dojo20220921.dojo20220921 import (
    to_roman,
    to_roman0,
    to_roman1,
)


@pytest.mark.parametrize(
    ('entrada', 'experado'),
    (
        (1, 'I'),
        (2, 'II'),
        (3, 'III'),
        (4, 'IV'),
        (5, 'V'),
        (6, 'VI'),
        (7, 'VII'),
        (8, 'VIII'),
        (9, 'IX'),
        (10, 'X'),
        (50, 'L'),
        (80, 'LXXX'),
        (100, 'C'),
        (500, 'D'),
        (900, 'CM'),
        (987, 'CMLXXXVII'),
        (1000, 'M'),
        (1988, 'MCMLXXXVIII'),
        (2009, 'MMIX'),
        (2011, 'MMXI'),
        (1978, 'MCMLXXVIII'),
        (1500, 'MD'),
    ),
)
def test_to_roman0(entrada, experado) -> None:
    assert to_roman0(entrada) == experado


@pytest.mark.parametrize(
    ('entrada', 'experado'),
    [
        (1, 'I'),
        (2, 'II'),
        (3, 'III'),
        (4, 'IV'),
        (5, 'V'),
        (6, 'VI'),
        (7, 'VII'),
        (8, 'VIII'),
        (9, 'IX'),
        (10, 'X'),
        (50, 'L'),
        (80, 'LXXX'),
        (100, 'C'),
        (500, 'D'),
        (900, 'CM'),
        (987, 'CMLXXXVII'),
        (1000, 'M'),
        (1988, 'MCMLXXXVIII'),
        (2009, 'MMIX'),
        (2011, 'MMXI'),
        (1978, 'MCMLXXVIII'),
        (1500, 'MD'),
    ],
)
def test_to_roman1(entrada, experado) -> None:
    assert to_roman1(entrada) == experado


@pytest.mark.parametrize(
    ('entrada', 'experado'),
    [
        (1, 'I'),
        (2, 'II'),
        (3, 'III'),
        (4, 'IV'),
        (5, 'V'),
        (6, 'VI'),
        (7, 'VII'),
        (8, 'VIII'),
        (9, 'IX'),
        (10, 'X'),
        (50, 'L'),
        (80, 'LXXX'),
        (100, 'C'),
        (500, 'D'),
        (900, 'CM'),
        (987, 'CMLXXXVII'),
        (1000, 'M'),
        (1988, 'MCMLXXXVIII'),
        (2009, 'MMIX'),
        (2011, 'MMXI'),
        (1978, 'MCMLXXVIII'),
        (1500, 'MD'),
    ],
)
def test_to_roman(entrada, experado) -> None:
    assert to_roman(entrada) == experado
