"""Test module."""

from typing import ClassVar, NoReturn
import incolume.py.coding_dojo_jedi.dojo20240907 as pkg
import pytest


class TestCase:
    """Test case class."""

    tests: ClassVar = [
        ((3, 1061), 3),
        ((3, 2006), 9),
    ]

    @pytest.mark.skip('fail implementation')
    @pytest.mark.parametrize(
        'entrance expected'.split(),
        tests,
    )
    def test_0(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert pkg.dojo_0(*entrance) == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        tests,
    )
    def test_1(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert pkg.dojo(*entrance) == expected
