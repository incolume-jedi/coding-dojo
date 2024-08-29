"""Test module."""

from typing import NoReturn
import incolume.py.coding_dojo_jedi.dojo20240603 as pkg
import pytest


class TestCase:
    """Test case class."""

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            (1_125_721, 1061),
            (1, 1),
            (4, 2),
            (9, 3),
            (121, 11),
            (144, 12),
        ],
    )
    def test_0(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert pkg.dojo(entrance) == expected
