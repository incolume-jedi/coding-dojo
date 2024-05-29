"""Module."""

import pytest

from . import gen_palindrome_prime, is_prime


__author__ = '@britodfbr'  # pragma: no cover


@pytest.mark.parametrize(
    'entrance expected'.split(),
    [
        (1, False),
        (1065, False),
        (1061, True),
        (9973, True),
    ],
)
def test_not_prime(entrance, expected):
    """Test not prime."""
    assert is_prime(entrance) == expected


def test_primo_palindrome_0():
    """Test menor de 1 algarismo."""
    expected = 2
    gnum = gen_palindrome_prime()
    assert next(gnum) == expected


def test_primo_palindrome_1():
    """Test menor de 2 algarismos."""
    expected = 11
    gnum = gen_palindrome_prime()
    assert [next(gnum) for _ in range(5)][-1] == expected
