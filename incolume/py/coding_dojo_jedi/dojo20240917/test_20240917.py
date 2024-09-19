"""Test module."""

from typing import ClassVar, NoReturn
import incolume.py.coding_dojo_jedi.dojo20240917 as pkg
import pytest
from tests.conftest import pytestmark


@pytestmark
class TestCase:
    """Test case class."""

    t0: ClassVar = None

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            (None, None),
        ],
    )
    def test_0(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert pkg.dojo(entrance) == expected
