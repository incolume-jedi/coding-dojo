"""Test module."""

from typing import NoReturn
import incolume.py.coding_dojo_jedi.dojo20240906 as pkg
import pytest


class TestCase:
    """Test case class."""

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(None, [7]),
            pytest.param(10**4, [7]),
        ],
    )
    def test_0(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert pkg.dojo(entrance) == expected
