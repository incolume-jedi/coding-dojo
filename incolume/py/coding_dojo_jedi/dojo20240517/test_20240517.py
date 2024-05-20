"""Test module."""

from typing import ClassVar
import pytest
from incolume.py.coding_dojo_jedi.dojo20240517 import (
    is_prime,
    is_prime0,
    is_prime1,
    gen_prime,
)


class CheckDojo:
    """Test case."""

    units0: ClassVar = [
        (0, False),
        (1, False),
        (2, True),
        (3, True),
        (4, False),
        (5, True),
        (6, False),
        (7, True),
        (11, True),
        (13, True),
        (15, False),
        (17, True),
        (23, True),
        (31, True),
        (37, True),
        (41, True),
        (43, True),
        (47, True),
    ]

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        units0,
    )
    def test_is_prime0(self, entrance, expected):
        """Test is_prime."""
        assert is_prime0(entrance) == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        units0,
    )
    def test_is_prime1(self, entrance, expected):
        """Test is_prime."""
        assert is_prime1(entrance) == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        units0,
    )
    def test_is_prime(self, entrance, expected):
        """Test is_prime."""
        assert is_prime(entrance) == expected

    def test_gen_prime(self):
        """Test gen_prime."""
        n = gen_prime()
        assert [next(n) for _ in range(15)] == [
            2,
            3,
            5,
            7,
            11,
            13,
            17,
            19,
            23,
            29,
            31,
            37,
            41,
            43,
            47,
        ]
