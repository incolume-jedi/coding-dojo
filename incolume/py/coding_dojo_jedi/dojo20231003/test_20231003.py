"""Testing dojo."""
import sys

import pytest

from . import max_sequence


@pytest.mark.skipif(
    sys.version_info < (3, 10),
    reason='requires python3.10 or higher',
)
class TestCase:
    """Class Test Case."""

    __test__ = False

    def test_max_sequence(self) -> None:
        """Test de max_sequence."""
        assert max_sequence([]) == 0

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            ([-1, -2, -3, -4], 0),
            ([-10, -2, -3, -1], 0),
            ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 45),
            ([10, 1, 2, 3, 4, 5, 6, 7, 8, 9], 55),
            ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
            ([10, -11, 2, 3, 4, 5, -5, 6, 7, -50, 8, -7, 9], 14),
        ],
    )
    def test_max_sequence1(self, entrance, expected) -> None:
        """Test de max."""
        assert max_sequence(entrance) == expected
