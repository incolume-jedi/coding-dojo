"""Test module."""

from typing import ClassVar, NoReturn
import incolume.py.coding_dojo_jedi.dojo20241216 as dojo147
import incolume.py.coding_dojo_jedi.dojo20241220 as pkg
import pytest
from pathlib import Path


class TestCase:
    """Test case class."""

    t0: ClassVar = None

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            ({'link': dojo147.url}, 'python-powered-h-50x65.json'),
        ],
    )
    def test_0(self, entrance, expected) -> NoReturn:
        """Unittest."""
        result = pkg.write_json(**entrance)
        assert isinstance(result, Path)
        assert result.name == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            (
                {'json_file': 'python-powered-h-50x65.json'},
                'python-powered-h-50x65.png',
            ),
        ],
    )
    def test_1(self, entrance, expected) -> NoReturn:
        """Unittest."""
        result = pkg.recover_image(**entrance)
        assert isinstance(result, Path)
        assert result.name == expected
