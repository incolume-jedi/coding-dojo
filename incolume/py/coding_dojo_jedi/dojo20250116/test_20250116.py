"""Test module."""

from __future__ import annotations
from pathlib import Path
from typing import ClassVar, NoReturn
import incolume.py.coding_dojo_jedi.dojo20250116 as pkg
import pytest


class TestCase:
    """Test case class."""

    t0: ClassVar = None
    img0: Path = pkg.IMG_DIR / 'letter.jpg'
    img1: Path = pkg.IMG_DIR / 'ctr-1808-08-25.png'

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(
                {},
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
        obj = pkg.PPImg(self.img0)
        assert obj == ''
        assert pkg.dojo(**entrance) == expected
