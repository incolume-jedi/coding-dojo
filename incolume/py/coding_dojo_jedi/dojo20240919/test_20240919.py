"""Test module."""

from typing import ClassVar, NoReturn
import incolume.py.coding_dojo_jedi.dojo20240919 as pkg
import pytest


class TestCase:
    """Test case class."""

    t0: ClassVar = [
        (([1], 1), []),
        (([1, 2], 1), [1]),
        (([1, 2, 3, 4, 5], 2), [1, 2, 4, 5]),
    ]

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        t0,
    )
    def test_0(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert pkg.dojo(*entrance) == expected
