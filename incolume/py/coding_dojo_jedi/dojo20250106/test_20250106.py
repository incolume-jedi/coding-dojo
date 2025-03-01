"""Test module."""

from __future__ import annotations


from pathlib import Path
from typing import ClassVar, NoReturn
import incolume.py.coding_dojo_jedi.dojo20250106 as pkg
import pytest
from tempfile import gettempdir
from copy import copy


@pytest.mark.offci
class TestCasePreprocessImageOCR:
    """Test case class."""

    t0: ClassVar = None
    obj: ClassVar[pkg.PreprocessImageOCR] = pkg.PreprocessImageOCR()
    img0: Path = pkg.IMG_DIR / 'letter.jpg'
    img1: Path = pkg.IMG_DIR / 'ctr-1808-08-25.png'

    def test_img_dir_type(self) -> NoReturn:
        """Unittest."""
        entrance = pkg.IMG_DIR
        assert isinstance(entrance, Path)

    def test_img_dir_format(self) -> NoReturn:
        """Unittest."""
        entrance = pkg.IMG_DIR
        assert entrance.is_dir()

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
    def test_img_dir_path(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert expected.issubset(entrance.parts)

    def test_reset(self):
        """Unittest."""
        self.obj.img_path = self.img0
        value = copy(self.obj.img)
        # break array value
        self.obj.img[self.obj.img < 10**3] = 0
        # compare two numpy arrays
        assert value.all() == self.obj.reset().img.all()

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(
                {'img': img0, 'fout': None},
                'letter_latest.jpg',
                marks=[],
            ),
            pytest.param(
                {
                    'img': img0,
                    'fout': Path(gettempdir())
                    / f'{img0.stem}_saved{img0.suffix}',
                },
                'letter_saved.jpg',
                marks=[],
            ),
        ],
    )
    def test_class_save(self, entrance, expected) -> NoReturn:
        """Unittest."""
        self.obj.img_path = entrance.get('img')
        result = self.obj.save(entrance.get('fout'))
        assert set(result.parts).issuperset(
            [expected],
        )


@pytest.mark.offci
class TestCasePPIOCR:
    """Test case."""

    obj: ClassVar[pkg.PreprocessImageOCR] = pkg.PPIOCR()
    img0: Path = pkg.IMG_DIR / 'letter.jpg'
    img1: Path = pkg.IMG_DIR / 'ctr-1808-08-25.png'

    def test_class_name(self) -> NoReturn:
        """Unittest."""
        assert self.obj.class_name == 'PPIOCR'

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(
                img1,
                Path(gettempdir()) / f'{img1.stem}_inverted{img1.suffix}',
                marks=[
                    pytest.mark.skip,
                    pytest.mark.xpass(
                        reason='Implementation failing (but shoulded ran)',
                    ),
                ],
            ),
            pytest.param(
                img0,
                Path(gettempdir()) / f'{img0.stem}_inverted{img0.suffix}',
                marks=[
                    # pytest.mark.skip,
                    pytest.mark.xpass(
                        reason='Implementation failing (but shoulded ran)',
                    ),
                ],
            ),
        ],
    )
    def test_inverted(self, entrance, expected) -> NoReturn:
        """Unittest."""
        self.obj.img_path = entrance
        self.obj.inverted()
        result = self.obj.save(fout=expected)
        assert result.is_file()
        assert result.resolve() == expected.resolve()
