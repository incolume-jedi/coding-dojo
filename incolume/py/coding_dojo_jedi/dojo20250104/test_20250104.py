"""Test module."""

from typing import ClassVar, NoReturn
import incolume.py.coding_dojo_jedi.dojo20250104 as pkg
import pytest
import tempfile
from pathlib import Path


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
        result = pkg.dojo(**entrance)
        assert result == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(
                {'url': pkg.URL, 'dir_output': Path(tempfile.gettempdir())},
                'pi-1M.tar.gz',
                marks=[],
            ),
            pytest.param(
                {'dir_output': Path(tempfile.gettempdir())},
                'pi-1M.tar.gz',
                marks=[],
            ),
            pytest.param({}, 'pi-1M.tar.gz', marks=[]),
        ],
    )
    def test_download(self, entrance, expected):
        """Unittest."""
        result = pkg.download_file(**entrance)
        assert expected in result.parts
        assert result.is_file()
