"""Test module."""

from typing import NoReturn
import incolume.py.coding_dojo_jedi.dojo20240705 as pkg
import pytest


class TestCase:
    """Test case class."""

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            (
                5,
                20,
            ),
            (
                1,
                10,
            ),
            (
                2,
                10,
            ),
            (
                3,
                14,
            ),
        ],
    )
    def test_0(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert len(pkg.dojo(entrance)) == expected
