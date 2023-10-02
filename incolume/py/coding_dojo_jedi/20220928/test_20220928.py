"""Dojo."""
from collections.abc import Iterable

import pytest
from dojo import max_sequence


class TestCase:
    """Test Case."""

    __test__ = False    # Will not be discovered as a test

    @pytest.mark.skip()
    @pytest.mark.parametrize(
        'entrance expected'.split(),
        (  # noqa: PT007
            ([], 0),
            ([-1, -2, -3, -4], 0),
            ([-10, -2, -3, -1], 0),
            ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 45),
            ([10, 1, 2, 3, 4, 5, 6, 7, 8, 9], 55),
            ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
            ([10, -11, 2, 3, 4, 5, -5, 6, 7, -50, 8, -7, 9], 14),
        ),
    )
    def test_max_sequence(self, entrance: Iterable, expected: int) -> None:
        """Max sequence."""
        assert max_sequence(entrance) == expected
