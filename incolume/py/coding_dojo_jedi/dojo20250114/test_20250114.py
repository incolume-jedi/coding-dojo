"""Test module."""

from __future__ import annotations
from tempfile import gettempdir
from typing import ClassVar, NoReturn
import incolume.py.coding_dojo_jedi.dojo20250114 as pkg
import pytest
from pathlib import Path


class TestCase:
    """Test case class."""

    obj: ClassVar[pkg.PPIOCR] = pkg.PPIOCR()
    img0: Path = pkg.IMG_DIR / 'letter.jpg'
    img1: Path = pkg.IMG_DIR / 'ctr-1808-08-25.png'

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(
                img0,
                Path('coding-dojo/letter_latest.jpg'),
                marks=[
                    pytest.mark.xpass(
                        reason='Implementation failing (but shoulded ran)',
                    ),
                ],
            ),
            pytest.param(
                img1,
                Path('coding-dojo/ctr-1808-08-25_latest.png'),
                marks=[
                    pytest.mark.xpass(
                        reason='Implementation failing (but shoulded ran)',
                    ),
                ],
            ),
            pytest.param(
                img1,
                Path(gettempdir()) / 'ctr-1808-08-25_latest.png',
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
        assert self.obj.img_data is not None
        assert result.is_file()
        assert set(expected.parts[-1:]).issubset(result.parts)

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(
                img1,
                Path(gettempdir()) / f'{img1.stem}_bw{img1.suffix}',
                marks=[
                    pytest.mark.xpass(
                        reason='Implementation failing (but shoulded ran)',
                    ),
                ],
            ),
            pytest.param(
                img0,
                Path(gettempdir()) / 'coding-dojo/letter_latest.jpg',
                marks=[
                    pytest.mark.xpass(
                        reason='Implementation failing (but shoulded ran)',
                    ),
                ],
            ),
        ],
    )
    def test_bw(self, entrance, expected) -> NoReturn:
        """Unittest."""
        self.obj.img_path = entrance
        self.obj.black_white()
        result = self.obj.save(expected)
        assert self.obj.img_path == entrance
        assert self.obj.img_data is not None
        assert result.is_file()
        assert set(expected.parts[-1:]).issubset(result.parts)
