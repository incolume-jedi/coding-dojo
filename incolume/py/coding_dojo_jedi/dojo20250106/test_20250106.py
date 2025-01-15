"""Test module."""

from __future__ import annotations
from pathlib import Path
from typing import ClassVar, NoReturn
import incolume.py.coding_dojo_jedi.dojo20250106 as pkg
import pytest


class TestCase:
    """Test case class."""

    t0: ClassVar = None

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(
                pkg.IMG_DIR,
                {'generic_data', 'text_img'},
                marks=[
                    pytest.mark.xpass(
                        reason='Implementation failing (but shoulded ran)',
                    ),
                ],
            ),
        ],
    )
    def test_img_dir(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert isinstance(entrance, Path)
        assert entrance.is_dir()
        assert expected.issubset(entrance.parts)

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(
                None,
                None,
                marks=[
                    pytest.mark.xpass(
                        reason='Implementation failing (but shoulded ran)',
                    ),
                ],
            ),
        ],
    )
    def test_0(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert pkg.dojo(entrance) == expected
