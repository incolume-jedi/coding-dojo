"""Module."""

import pytest


from . import is_narcisist, char_position, counting_sheep


__author__ = '@britodfbr'  # pragma: no cover


class TestNarcisista:
    """Caso test number narcisist."""

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            (1, True),
            (10, False),
            (153, True),
            (222, False),
            (1634, True),
            (1111, False),
        ],
    )
    def test_is_narcisist(self, entrance, expected):
        """Test if is narcisist number."""
        assert is_narcisist(entrance) == expected


class TestLettersPosition:
    """Case test letter position."""

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            ('água', {'á': [0], 'a': [3], 'g': [1], 'u': [2]}),
            ('açaí', {'a': [0, 2], 'ç': [1], 'í': [3]}),
            ('azul', {'a': [0], 'z': [1], 'u': [2], 'l': [3]}),
            (
                'abracadabra',
                {
                    'a': [0, 3, 5, 7, 10],
                    'b': [1, 8],
                    'r': [2, 9],
                    'c': [4],
                    'd': [6],
                },
            ),
            (
                'mississipi',
                {'i': [1, 4, 7, 9], 'm': [0], 'p': [8], 's': [2, 3, 5, 6]},
            ),
            (
                'aibofobia',
                {'a': [0, 8], 'b': [2, 6], 'f': [4], 'i': [1, 7], 'o': [3, 5]},
            ),
            (
                'A base do teto desaba',
                {
                    ' ': [1, 6, 9, 14],
                    'A': [0],
                    'a': [3, 18, 20],
                    'b': [2, 19],
                    'd': [7, 15],
                    'e': [5, 11, 16],
                    'o': [8, 13],
                    's': [4, 17],
                    't': [10, 12],
                },
            ),
            (
                'A cara rajada da jararaca',
                {
                    ' ': [1, 6, 13, 16],
                    'A': [0],
                    'a': [3, 5, 8, 10, 12, 15, 18, 20, 22, 24],
                    'c': [2, 23],
                    'd': [11, 14],
                    'j': [9, 17],
                    'r': [4, 7, 19, 21],
                },
            ),
            (
                'Socorram-me, subi no ônibus em Marrocos',
                {
                    'S': [0],
                    'o': [1, 3, 19, 35, 37],
                    'c': [2, 36],
                    'r': [4, 5, 33, 34],
                    'a': [6, 32],
                    'm': [7, 9, 29],
                    '-': [8],
                    'e': [10, 28],
                    ',': [11],
                    ' ': [12, 17, 20, 27, 30],
                    's': [13, 26, 38],
                    'u': [14, 25],
                    'b': [15, 24],
                    'i': [16, 23],
                    'n': [18, 22],
                    'ô': [21],
                    'M': [31],
                },
            ),
            (
                'Me vê se a panela da moça é de aço, Madalena Paes, e vem',
                {
                    'M': [0, 36],
                    'e': [1, 7, 14, 29, 41, 47, 51, 54],
                    ' ': [2, 5, 8, 10, 17, 20, 25, 27, 30, 35, 44, 50, 52],
                    'v': [3, 53],
                    'ê': [4],
                    's': [6, 48],
                    'a': [9, 12, 16, 19, 24, 31, 37, 39, 43, 46],
                    'p': [11],
                    'n': [13, 42],
                    'l': [15, 40],
                    'd': [18, 28, 38],
                    'm': [21, 55],
                    'o': [22, 33],
                    'ç': [23, 32],
                    'é': [26],
                    ',': [34, 49],
                    'P': [45],
                },
            ),
        ],
    )
    def test_check(self, entrance, expected):
        """Check result."""
        assert char_position(entrance) == expected


class TestSheep:
    """Case test sheep."""

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            (
                [
                    True,
                    True,
                    True,
                    'nill',
                    True,
                    True,
                    True,
                    True,
                    True,
                    'null',
                    True,
                    'false',
                    True,
                    False,
                    'undefined',
                    'True',
                    'true',
                    True,
                    True,
                    True,
                    False,
                    False,
                    True,
                    True,
                ],
                17,
            ),
            (
                [
                    True,
                    True,
                    True,
                    False,
                    True,
                    True,
                    True,
                    True,
                    True,
                    False,
                    True,
                    False,
                    True,
                    False,
                    False,
                    True,
                    True,
                    True,
                    True,
                    True,
                    False,
                    False,
                    True,
                    True,
                ],
                17,
            ),
            (
                [
                    [True, True, True, False],
                    [True, True, True, True],
                    [True, False, True, False],
                    [True, False, False, True],
                    [True, True, True, True],
                    [False, False, True, True],
                ],
                17,
            ),
            (
                [
                    [True, True, True, 'undefined'],
                    [True, True, True, True],
                    [True, False, True, 'nill'],
                    [True, None, False, True],
                    [True, True, True, True],
                    [False, 'null', 'True', True],
                ],
                17,
            ),
        ],
    )
    def test_counting_sheep(self, entrance, expected):
        """Test count sheep."""
        assert counting_sheep(entrance) == expected
