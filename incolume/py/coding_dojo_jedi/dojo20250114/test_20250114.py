"""Test module."""

from __future__ import annotations
from typing import ClassVar, NoReturn
import incolume.py.coding_dojo_jedi.dojo20250114 as pkg
import pytest
from pathlib import Path


class TestCase:
    """Test case class."""

    obj: ClassVar[pkg.PPIOCR] = pkg.PPIOCR()
    img0: Path = pkg.IMG_DIR / 'letter.png'
    img1: Path = pkg.IMG_DIR / 'ctr-1808-08-25.png'

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(
                img0,
                set('coding-dojo letter_latest.png'.split()),
                marks=[
                    pytest.mark.xpass(
                        reason='Implementation failing (but shoulded ran)',
                    ),
                ],
            ),
        ],
    )
    def test_gray_scale(self, entrance, expected) -> NoReturn:
        """Unittest."""
        self.obj.img_path = entrance
        self.obj.grayscale()
        result = self.obj.save()
        assert self.obj.img_path == entrance
        assert self.obj.img is not None
        assert result.is_file()
        assert expected.issubset(result.parts)
