"""Test module."""

from __future__ import annotations
from pathlib import Path
from typing import ClassVar, NoReturn
import incolume.py.coding_dojo_jedi.dojo20250106 as pkg
import pytest
from incolume.py.coding_dojo_jedi.utils import genfile
from tempfile import gettempdir


class TestCase:
    """Test case class."""

    t0: ClassVar = None

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

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(
                {
                    'fimg': (
                        file := pkg.IMG_DIR.joinpath('ctr-1808-08-25.png')
                    ),
                },
                Path(gettempdir()) / f'{file.stem}_inverted{file.suffix}',
                marks=[
                    # pytest.mark.skip,
                    pytest.mark.xpass(
                        reason='Implementation failing (but shoulded ran)',
                    ),
                ],
            ),
            pytest.param(
                {
                    'fimg': pkg.IMG_DIR.joinpath('letter.png'),
                    'foutput': (file := genfile(suffix='.png')),
                },
                file,
                marks=[
                    pytest.mark.xpass(
                        reason='Implementation failing (but shoulded ran)',
                    ),
                ],
            ),
            pytest.param(
                {
                    'fimg': (file := pkg.IMG_DIR.joinpath('letter.png')),
                },
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
        # assert entrance.get('fimg').is_file()
        assert pkg.inverted_image(**entrance) == expected
