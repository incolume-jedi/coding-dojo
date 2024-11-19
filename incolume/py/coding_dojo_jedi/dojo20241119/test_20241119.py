"""Test module."""

from pathlib import Path
from typing import ClassVar, NoReturn
import pytest


# ruff: noqa: ERA001
class TestCase:
    """Test case class."""

    t0: ClassVar = None

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            # pytest.param({'file': Path(pkg.artefatos[-1]).as_posix()}, None),
            pytest.param({'file': ''}, '', marks=[]),
            pytest.param({'file': Path()}, '', marks=[]),
        ],
    )
    def test_0(self, entrance, expected) -> NoReturn:
        """Unittest."""
        # assert pkg.dojo(**entrance) == expected
        assert entrance.get('file') == expected
