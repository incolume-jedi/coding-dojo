"""Test module."""

from typing import NoReturn
import incolume.py.coding_dojo_jedi.dojo20240913 as pkg
import pytest


class TestCase:
    """Test case class."""

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param([-1, 0], [-1, 0], marks=[]),
            pytest.param([0, 1], [1, 0], marks=[]),
            pytest.param([1, 2, 1, 3, 2, 5], [3, 5], marks=[]),
            pytest.param([1, 2, 1, 3, 2, 5], [5, 3], marks=[]),
        ],
    )
    def test_0(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert all(x in expected for x in pkg.dojo(entrance))
