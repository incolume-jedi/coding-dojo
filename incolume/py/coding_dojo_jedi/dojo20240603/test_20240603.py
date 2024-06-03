"""Test module."""

from typing import ClassVar, NoReturn
import . as pkg
import pytest

class TestCase:
    """Test case class."""

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
             (None, None),
        ],
    )
    def test_0(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert pkg.dojo(entrance) == expected
