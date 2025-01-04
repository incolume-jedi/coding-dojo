"""Test module."""

from typing import ClassVar, NoReturn
import incolume.py.coding_dojo_jedi.dojo20250104 as pkg
import pytest


class TestCase:
    """Test case class."""

    t0: ClassVar = None

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param({}, None, marks=[pytest.mark.skip]),
        ],
    )
    def test_0(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert pkg.dojo(**entrance) == expected

    def test_download(self):
        """Unittest."""
        assert pkg.download_file() == ''
