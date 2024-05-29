"""Module."""

from . import gen_palindrome_prime


__author__ = '@britodfbr'  # pragma: no cover


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
