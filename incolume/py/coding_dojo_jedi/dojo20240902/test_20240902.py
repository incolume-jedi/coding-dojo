"""Test module."""

from typing import NoReturn
import incolume.py.coding_dojo_jedi.dojo20240902 as pkg
import pytest


class TestCase:
    """Test case class."""

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            (([2, 7, 11, 15], 9), [0, 1]),
            (([3, 2, 4], 6), [1, 2]),
            (([3, 3], 6), [0, 1]),
            (([2, 7, 11, 15], 18), [1, 2]),
            (([2, 7, 11, 15], 17), [0, 3]),
            (([2, 7, 11, 15], 22), [1, 3]),
        ],
    )
    def test_0(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert pkg.dojo(*entrance) == expected
