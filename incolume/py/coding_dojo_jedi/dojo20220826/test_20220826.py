"""Unittest for dojo."""
import pytest

from incolume.py.coding_dojo_jedi.dojo20220826.dojo20220826 import (
    imc,
    imc0,
    no_exclamation,
    tabuada,
)


@pytest.mark.parametrize(
    ('entrance', 'expected'),
    [
        ('Hello World!', 'Hello World'),
        ('Hello World!!!', 'Hello World'),
        ('Hi! Hello!', 'Hi Hello'),
        ('', ''),
        ('Oh, no!!!', 'Oh, no'),
    ],
)
def test_noexclamation(entrance, expected) -> None:
    """Test noexclamation."""
    assert no_exclamation(entrance) == expected


@pytest.mark.parametrize(
    'entrance expected'.split(),
    [
        (
            (10),
            [
                '10 X 1 = 10',
                '10 X 2 = 20',
                '10 X 3 = 30',
                '10 X 4 = 40',
                '10 X 5 = 50',
                '10 X 6 = 60',
                '10 X 7 = 70',
                '10 X 8 = 80',
                '10 X 9 = 90',
                '10 X 10 = 100',
            ],
        ),
        ((5, 4, 7), ['5 X 4 = 20', '5 X 5 = 25', '5 X 6 = 30', '5 X 7 = 35']),
        ((5, 7, 4), ['5 X 4 = 20', '5 X 5 = 25', '5 X 6 = 30', '5 X 7 = 35']),
        (
            (10, 6, 3),
            [
                '10 X 3 = 30',
                '10 X 4 = 40',
                '10 X 5 = 50',
                '10 X 6 = 60',
            ],
        ),
        (
            (10, 3, 6),
            [
                '10 X 3 = 30',
                '10 X 4 = 40',
                '10 X 5 = 50',
                '10 X 6 = 60',
            ],
        ),
        (
            (10, 10, 7),
            [
                '10 X 7 = 70',
                '10 X 8 = 80',
                '10 X 9 = 90',
                '10 X 10 = 100',
            ],
        ),
        (
            (10, 7, 10),
            [
                '10 X 7 = 70',
                '10 X 8 = 80',
                '10 X 9 = 90',
                '10 X 10 = 100',
            ],
        ),
        (
            {'tab_ref': 10, 'inicial': 10, 'final': 7},
            [
                '10 X 7 = 70',
                '10 X 8 = 80',
                '10 X 9 = 90',
                '10 X 10 = 100',
            ],
        ),
        (
            {'tab_ref': 10, 'inicial': 7, 'final': 10},
            [
                '10 X 7 = 70',
                '10 X 8 = 80',
                '10 X 9 = 90',
                '10 X 10 = 100',
            ],
        ),
    ],
)
def test_tabuada(entrance, expected) -> None:
    """Test tabuada."""
    if isinstance(entrance, dict):
        assert tabuada(**entrance) == expected
    if isinstance(entrance, tuple):
        assert tabuada(*entrance) == expected


@pytest.mark.parametrize(
    'entrance expected'.split(),
    [
        ((1.74, 75), 'peso normal'),
        ((1.54, 125), 'Obesidade III'),
        ((1.72, 80), 'Sobrepeso'),
        ((1.84, 55), 'abaixo do peso'),
        ((1.64, 75), 'Sobrepeso'),
        ((1.84, 135), 'Obesidade II'),
        ((1.78, 95), 'Obesidade I'),
        ((1.78, 98), 'Obesidade I'),
    ],
)
def test_imc0(entrance, expected) -> None:
    """Test imc."""
    assert imc0(*entrance) == expected


@pytest.mark.parametrize(
    'entrance expected'.split(),
    [
        ((1.74, 75), 'peso normal'),
        ((1.54, 125), 'Obesidade III'),
        ((1.72, 80), 'Sobrepeso'),
        ((1.84, 55), 'abaixo do peso'),
        ((1.64, 75), 'Sobrepeso'),
        ((1.84, 135), 'Obesidade II'),
        ((1.78, 95), 'Obesidade I'),
        ((1.78, 98), 'Obesidade I'),
    ],
)
def test_imc(entrance, expected) -> None:
    """Test imc."""
    assert imc(*entrance) == expected
