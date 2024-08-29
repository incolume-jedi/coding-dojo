"""Test module."""

from typing import NoReturn
import incolume.py.coding_dojo_jedi.dojo20240607 as pkg
import pytest
from re import escape


class TestCase:
    """Test case class."""

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            ([1, 2, 3, 1], 4),
            ([2, 7, 9, 3, 1], 12),
            ([0], 0),
            ([400], 400),
        ],
    )
    def test_0(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert pkg.house_robber(entrance) == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            (
                [401],
                {
                    'expected_exception': ValueError,
                    'match': escape('0 <= nums[i] <= 400'),
                },
            ),
            (
                [-1],
                {
                    'expected_exception': ValueError,
                    'match': escape('0 <= nums[i] <= 400'),
                },
            ),
            (
                [],
                {
                    'expected_exception': IndexError,
                    'match': escape('1 <= nums.length <= 100'),
                },
            ),
        ],
    )
    def test_1(self, entrance, expected) -> NoReturn:
        """Unittest."""
        with pytest.raises(**expected):
            assert pkg.house_robber(entrance)
