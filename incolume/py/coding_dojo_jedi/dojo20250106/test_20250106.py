"""Test module."""

from __future__ import annotations


from pathlib import Path
from typing import ClassVar, NoReturn
import incolume.py.coding_dojo_jedi.dojo20250106 as pkg
import pytest
from tempfile import gettempdir


class TestCase:
    """Test case class."""

    obj: ClassVar[pkg.PreprocessImageOCR] = pkg.PreprocessImageOCR()
    img0: ClassVar[Path] = obj.IMG_DIR / 'letter.png'
    img1: ClassVar[Path] = obj.IMG_DIR / 'ctr-1808-08-25.png'

    t0: ClassVar = None

    def test_img_dir_type(self) -> NoReturn:
        """Unittest."""
        entrance = self.obj.IMG_DIR
        assert isinstance(entrance, Path)

    def test_img_dir_format(self) -> NoReturn:
        """Unittest."""
        entrance = self.obj.IMG_DIR
        assert entrance.is_dir()

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(
                obj.IMG_DIR,
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

    def test_class_name(self) -> NoReturn:
        """Unittest."""
        assert self.obj.class_name == 'PreprocessImageOCR'

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(
                {'img': img0, 'fout': None},
                'letter_latest.png',
                marks=[],
            ),
            pytest.param(
                {
                    'img': img0,
                    'fout': Path(gettempdir())
                    / f'{img0.stem}_saved{img0.suffix}',
                },
                'letter_saved.png',
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

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(
                (file := obj.IMG_DIR.joinpath('ctr-1808-08-25.png')),
                Path(gettempdir()) / f'{file.stem}_inverted{file.suffix}',
                marks=[
                    # pytest.mark.skip,
                    pytest.mark.xpass(
                        reason='Implementation failing (but shoulded ran)',
                    ),
                ],
            ),
            pytest.param(
                obj.IMG_DIR.joinpath('letter.png'),
                file,
                marks=[
                    pytest.mark.xpass(
                        reason='Implementation failing (but shoulded ran)',
                    ),
                ],
            ),
            pytest.param(
                (file := obj.IMG_DIR.joinpath('letter.png')),
                Path(gettempdir()) / f'{file.stem}_inverted{file.suffix}',
                marks=[
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
        assert result == expected
