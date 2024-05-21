"""tests module."""

from . import romeu_julieta, fizzbuzz
import pytest

tests_fizzbuzz = [
    (1, '1'),
    (3, 'Fizz'),
    (5, 'Buzz'),
    (7, '7'),
    (15, 'FizzBuzz'),
    (30, 'FizzBuzz'),
    (17, '17'),
    (27, 'Fizz'),
    (10, 'Buzz'),
    (45, 'FizzBuzz'),
    (150, 'FizzBuzz'),
    (13, '13'),
    (4, '4'),
    (31, '31'),
]


@pytest.mark.parametrize(
    'entrance expected'.split(),
    tests_fizzbuzz,
)
def test_fizzbuzz0(entrance, expected):
    """Fizzbuzz."""
    assert fizzbuzz(entrance) == expected


@pytest.mark.parametrize(
    'entrance expected'.split(),
    tests_fizzbuzz,
)
def test_fizzbuzz(entrance, expected):
    """Fizzbuzz."""
    assert fizzbuzz(entrance) == expected


@pytest.mark.parametrize(
    'entrance expected'.split(),
    [
        (1, '1'),
        (3, 'queijo'),
        (5, 'goiabada'),
        (7, '7'),
        (15, 'romeu e julieta'),
        (30, 'romeu e julieta'),
        (17, '17'),
        (27, 'queijo'),
        (10, 'goiabada'),
        (45, 'romeu e julieta'),
        (150, 'romeu e julieta'),
        (13, '13'),
        (4, '4'),
        (31, '31'),
    ],
)
def test_romeu_julieta(entrance, expected):
    """Test function."""
    assert romeu_julieta(entrance) == expected
