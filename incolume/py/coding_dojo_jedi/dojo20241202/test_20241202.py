"""Test module."""

from typing import ClassVar, NoReturn
import incolume.py.coding_dojo_jedi.dojo20241202 as pkg
import pytest


class TestCase:
    """Test case class."""

    t0: ClassVar = None

    @pytest.mark.skip
    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            (None, None),
        ],
    )
    def test_3(self, entrance, expected) -> NoReturn:
        """Unittest."""

    def test_2(self) -> NoReturn:
        """Unittest."""
        assert pkg.dojo() == ''

    def test_1(self) -> NoReturn:
        """Unittest."""
        assert pkg.get_content_html() == ''

    def test_0(self) -> NoReturn:
        """Unittest."""
        assert isinstance(pkg.get_list_html(pkg.directory[0]), map)
