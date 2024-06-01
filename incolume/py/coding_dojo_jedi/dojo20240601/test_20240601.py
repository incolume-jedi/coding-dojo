"""Module."""

import pytest

import incolume.py.coding_dojo_jedi.dojo20240601 as pkg

from typing import ClassVar

__author__ = '@britodfbr'  # pragma: no cover


class TestCase:
    """Test case."""

    test_case_0: ClassVar = [
        ('casa', 'a'),
        ('mississipi', 'is'),
        ('abobrinha', 'ab'),
        ('Tudo é difícil até fácil se tornar.', 'i'),
        ('A base do teto desaba', 'ae'),
        ('A cara rajada da jararaca', 'a'),
        ('Socorram-me, subi no ônibus em Marrocos', 'o'),
        ('Me vê se a panela da moça é de aço, Madalena Paes, e vem', 'a'),
    ]

    test_case_1: ClassVar = [
        ('casa', ['a']),
        ('mississipi', 'i s'.split()),
        ('abobrinha', 'a b'.split()),
        ('Tudo é difícil até fácil se tornar.', ['i']),
        ('A base do teto desaba', 'a e'.split()),
        ('A cara rajada da jararaca', ['a']),
        ('Socorram-me, subi no ônibus em Marrocos', ['o']),
        ('Me vê se a panela da moça é de aço, Madalena Paes, e vem', ['a']),
    ]

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        test_case_0,
    )
    def test_max_letter_0(self, entrance, expected):
        """Test it."""
        assert pkg.max_letter0(entrance) in expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        test_case_0,
    )
    def test_max_letter_1(self, entrance, expected):
        """Test it."""
        assert pkg.max_letter1(entrance) in expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        test_case_0,
    )
    def test_max_letter_2(self, entrance, expected):
        """Test it."""
        assert pkg.max_letter2(entrance) in expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        test_case_1,
    )
    def test_max_letter_3(self, entrance, expected):
        """Test it."""
        assert pkg.max_letter(entrance) == expected
