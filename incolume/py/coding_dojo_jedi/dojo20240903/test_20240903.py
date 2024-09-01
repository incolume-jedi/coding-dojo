"""Test module."""

from typing import NoReturn
import incolume.py.coding_dojo_jedi.dojo20240903 as pkg
import pytest


class TestCase:
    """Test case class."""

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            (
                ([2, 4, 3], [5, 6, 4]),
                [7, 0, 8],
            ),
            (
                ([0], [0]),
                [0],
            ),
            (
                ([9, 9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]),
                [8, 9, 9, 9, 0, 0, 0, 0, 1],
            ),
        ],
    )
    def test_0(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert pkg.dojo(*entrance) == expected
