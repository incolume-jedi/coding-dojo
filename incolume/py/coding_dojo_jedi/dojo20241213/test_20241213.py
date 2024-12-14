"""Test module."""

from typing import ClassVar, NoReturn
import incolume.py.coding_dojo_jedi.dojo20241213 as pkg
import pytest


class TestLongestConsecutiveSequence:
    """Test case class."""

    t0: ClassVar = None

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param([100, 4, 200, 1, 3, 2], 4),
            pytest.param([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
            pytest.param(
                [100, 4, 200, 201, 203, 202, 0, 3, 7, 2, 5, 8, 4, 6, 0, 1],
                9,
            ),
        ],
    )
    def test_0(self, entrance, expected) -> NoReturn:
        """Unittest."""
        obj = pkg.Solution()
        assert obj.longest_consecutive(entrance) == expected
