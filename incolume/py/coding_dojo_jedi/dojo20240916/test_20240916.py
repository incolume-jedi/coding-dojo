"""Test module."""

from typing import NoReturn
import incolume.py.coding_dojo_jedi.dojo20240916 as pkg
import pytest


class TestCase:
    """Test case class."""

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            (0, 0),
            (1023, 5),
            (400, 1.96),
        ],
    )
    def test_0(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert pkg.v_dac(entrance) == expected
