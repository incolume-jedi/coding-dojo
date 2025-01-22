"""Test module."""

from __future__ import annotations
from typing import ClassVar
import incolume.py.coding_dojo_jedi.dojo20250112 as pkg
import pytest


class TestPrimes:
    """Case teste."""

    test0: ClassVar = [
        (0o2, True),  # octal
        (0x2, True),  # Hexadecimal
        (0b11, True),  # binário
        (3j, False),  # complexo
        (2.0, True),  # float
        (2.1, False),  # float
        (b'2', True),  # bytes
        ('2', True),  # str
        (10**5, False),
        (9323, True),
        (1, False),
        (2, True),
        (3, True),
        (4, False),
        (41, True),
        (51, False),
        (71, True),
        (59, True),
        (89, True),
    ]

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        test0,
    )
    def test_is_prime_0(self, entrance, expected):
        """Check is prime number."""
        assert pkg.is_prime_0(entrance) == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        test0,
    )
    def test_is_prime_1(self, entrance, expected):
        """Check is prime number."""
        assert pkg.is_prime_1(entrance) == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        test0,
    )
    def test_is_prime_2(self, entrance, expected):
        """Check is prime number."""
        assert pkg.is_prime_2(entrance) == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        test0,
    )
    def test_is_prime_3(self, entrance, expected):
        """Check is prime number."""
        assert pkg.is_prime_3(entrance) == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        test0,
    )
    def test_is_prime_4(self, entrance, expected):
        """Check is prime number."""
        assert pkg.is_prime_4(entrance) == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        test0,
    )
    def test_is_prime_5(self, entrance, expected):
        """Check is prime number."""
        assert pkg.is_prime_5(entrance) == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        test0,
    )
    def test_is_prime(self, entrance, expected):
        """Check is prime number."""
        assert pkg.is_prime(entrance) == expected
