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
        (0b01, False),  # binário
        (0b10, True),  # binário
        (0b11, True),  # binário
        (3j, False),  # complexo
        (2.0, True),  # float
        (2.1, False),  # float
        (b'2', True),  # bytes
        ('2', True),  # str
        (10**5, False),
        (-17, False),
    ]
    test1: ClassVar = [
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
        test0 + test1,
    )
    def test_is_prime_0(self, entrance, expected):
        """Check is prime number."""
        assert pkg.is_prime_0(entrance) == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        test0 + test1,
    )
    def test_is_prime_1(self, entrance, expected):
        """Check is prime number."""
        assert pkg.is_prime_1(entrance) == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        test0 + test1,
    )
    def test_is_prime_2(self, entrance, expected):
        """Check is prime number."""
        assert pkg.is_prime_2(entrance) == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        test0 + test1,
    )
    def test_is_prime_3(self, entrance, expected):
        """Check is prime number."""
        assert pkg.is_prime_3(entrance) == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        test0 + test1,
    )
    def test_is_prime_4(self, entrance, expected):
        """Check is prime number."""
        assert pkg.is_prime_4(entrance) == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        test0 + test1,
    )
    def test_is_prime_5(self, entrance, expected):
        """Check is prime number."""
        assert pkg.is_prime_5(entrance) == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        test0 + test1,
    )
    def test_is_prime(self, entrance, expected):
        """Check is prime number."""
        assert pkg.is_prime(entrance) == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(0, 2, marks=[]),
            pytest.param(35, 37, marks=[]),
            pytest.param(9335, 9337, marks=[]),
            pytest.param(10**4, 10007, marks=[]),
            pytest.param(70, 71, marks=[]),
        ],
    )
    def test_gen_prime_0(self, entrance, expected):
        """Unit test."""
        genprime = pkg.gen_prime(entrance)
        assert next(genprime) == expected

    @pytest.mark.parametrize(
        'quant entrance expected'.split(),
        [
            pytest.param(5, -1, [2, 3, 5, 7, 11], marks=[]),
            pytest.param(5, 9000, [9001, 9007, 9011, 9013, 9029], marks=[]),
            pytest.param(5, 79, [79, 83, 89, 97, 101], marks=[]),
            pytest.param(
                15,
                30,
                [31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97],
                marks=[],
            ),
        ],
    )
    def test_gen_prime_1(self, quant, entrance, expected):
        """Unit test."""
        genprime = pkg.gen_prime(entrance)
        assert [next(genprime) for _ in range(quant)] == expected
