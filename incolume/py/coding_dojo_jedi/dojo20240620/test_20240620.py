"""Test module."""

from typing import NoReturn
import incolume.py.coding_dojo_jedi.dojo20240620 as pkg
import pytest


class TestCase:
    """Test case class."""

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            (9, False),
            (10, True),
        ],
    )
    def test_0(self, entrance, expected) -> NoReturn:
        """Unittest."""
        quantia = len(pkg.dojo()) == entrance
        assert quantia == expected
