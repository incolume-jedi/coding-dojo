"""Module."""

from typing import ClassVar

import pytest
from incolume.py.coding_dojo_jedi.dojo20240516 import (
    two_sum,
    two_sum0,
    inverter_names,
    classify,
)

__author__ = '@britodfbr'  # pragma: no cover


class CheckDojo:
    """Test case."""

    unittests0: ClassVar = [
        ({'array': [2, 7, 11, 15], 'target': 9}, [0, 1]),
        ({'array': [2, 11, 7, 15], 'target': 9}, [0, 2]),
        ({'array': [11, 7, 2, 15], 'target': 9}, [1, 2]),
        ({'array': [15, 7, 11, 2], 'target': 9}, [1, 3]),
        ({'array': [15, 7, 11, 2], 'target': 5}, []),
    ]

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        unittests0,
    )
    def test_twosum0(self, entrance, expected):
        """Test two_sum."""
        assert two_sum0(**entrance) == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        unittests0,
    )
    def test_twosum(self, entrance, expected):
        """Test two_sum."""
        assert two_sum(**entrance) == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            (
                ['Brett', 'Emily', 'Gregory', 'Pablo', 'Thomas'],
                ['Tterb', 'Ylime', 'Yrogerg', 'Olbap', 'Samoht'],
            ),
        ],
    )
    def test_inverter_names(self, entrance, expected):
        """Test inverter_names."""
        assert inverter_names(entrance) == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            ({'quantia': 3, 'array': [19, 7, 11]}, ([19, 11, 7], [7, 11, 19])),
            ({'quantia': 1, 'array': [33, 37, 87, 87, 23]}, ([87], [23])),
            (
                {'quantia': 4, 'array': [33, 37, 87, 87, 23]},
                ([87, 87, 37, 33], [23, 33, 37, 87]),
            ),
            (
                {
                    'quantia': 7,
                    'array': [
                        33,
                        37,
                        87,
                        87,
                        23,
                        83,
                        29,
                        85,
                        18,
                        28,
                        82,
                        93,
                        23,
                        16,
                        9,
                    ],
                },
                ([93, 87, 87, 85, 83, 82, 37], [9, 16, 18, 23, 23, 28, 29]),
            ),
            (
                {
                    'quantia': 10,
                    'array': [
                        87,
                        23,
                        83,
                        29,
                        85,
                        18,
                        28,
                        82,
                        93,
                        23,
                        16,
                        9,
                        68,
                        27,
                        95,
                        37,
                        3,
                        55,
                        16,
                        87,
                        77,
                        1,
                        35,
                        18,
                        10,
                        33,
                        57,
                        95,
                        55,
                        17,
                        32,
                        45,
                        29,
                        62,
                        96,
                        70,
                        72,
                        54,
                        85,
                        46,
                        55,
                        81,
                        40,
                        83,
                        15,
                        44,
                        76,
                        81,
                        33,
                        88,
                    ],
                },
                (
                    [96, 95, 95, 93, 88, 87, 87, 85, 85, 83],
                    [1, 3, 9, 10, 15, 16, 16, 17, 18, 18],
                ),
            ),
            ({'quantia': 3, 'array': [19, 7]}, ()),
        ],
    )
    def test_classify(self, entrance, expected):
        """Test classify."""
        assert classify(**entrance) == expected
