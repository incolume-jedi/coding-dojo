"""Test module."""

from typing import NoReturn
import incolume.py.coding_dojo_jedi.dojo20240605 as pkg
import pytest


class TestCase:
    """Test case class."""

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            ('', None),
        ],
    )
    def test_0(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert pkg.scrap_estados(entrance) == expected
