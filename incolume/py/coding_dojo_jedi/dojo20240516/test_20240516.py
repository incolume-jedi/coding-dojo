"""Module."""

from typing import ClassVar

import pytest
from incolume.py.coding_dojo_jedi.dojo20240516 import (
    two_sum,
    two_sum0,
    inverter_names,
)

__author__ = '@britodfbr'  # pragma: no cover


class CheckDojo:
    """Test case."""

    unittests0: ClassVar = [
        ({'array': [2, 7, 11, 15], 'target': 9}, [0, 1]),
        ({'array': [2, 11, 7, 15], 'target': 9}, [0, 2]),
        ({'array': [11, 7, 2, 15], 'target': 9}, [1, 2]),
        ({'array': [15, 7, 11, 2], 'target': 9}, [1, 3]),
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
