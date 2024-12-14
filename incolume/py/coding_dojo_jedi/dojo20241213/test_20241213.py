"""Test module."""

from typing import ClassVar, NoReturn
import incolume.py.coding_dojo_jedi.dojo20241213 as pkg
import pytest


class TestLongestConsecutiveSequence:
    """Test case class."""

    t0: ClassVar = [
        [100, 4, 200, 1, 3, 2],
        [0, 3, 7, 2, 5, 8, 4, 6, 0, 1],
        [100, 4, 200, 201, 203, 202, 0, 3, 7, 2, 5, 8, 4, 6, 0, 1],
    ]

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(t0[0], 4, marks=[]),
            pytest.param(t0[1], 9, marks=[]),
            pytest.param(t0[2], 9, marks=[pytest.mark.skip]),
        ],
    )
    def test_0(self, entrance, expected) -> NoReturn:
        """Unittest."""
        obj = pkg.Solutions()
        assert obj.longest_consecutive(entrance) == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(t0[0], 4, marks=[]),
            pytest.param(t0[1], 9, marks=[]),
            pytest.param(t0[2], 9, marks=[]),
        ],
    )
    def test_1(self, entrance, expected) -> NoReturn:
        """Unittest."""
        obj = pkg.Solutions()
        assert obj.longest_consecutive1(entrance) == expected
