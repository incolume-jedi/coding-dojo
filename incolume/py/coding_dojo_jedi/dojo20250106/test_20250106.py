"""Test module."""

from __future__ import annotations


from pathlib import Path
from typing import ClassVar, NoReturn
from collections.abc import Callable
import incolume.py.coding_dojo_jedi.dojo20250106 as pkg
import pytest
from incolume.py.coding_dojo_jedi.utils import genfile
from tempfile import gettempdir

import numpy as np


class TestCase:
    """Test case class."""

    obj: ClassVar[pkg.PreprocessImage] = pkg.PreprocessImage()
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
        assert self.obj.class_name == 'PreprocessImage'

    def test_open_plot(self) -> NoReturn:
        """Unit test decorator."""
        func = lambda x: x  # noqa: E731
        func = pkg.open_plot(func)
        assert isinstance(func, Callable)
        assert isinstance(func(self.img0), np.ndarray)

    def test_write_plot(self) -> NoReturn:
        """Unit test decorator."""
        func = lambda x: x  # noqa: E731
        func = pkg.open_plot(func)
        func = pkg.write_plot(func)
        result = func(self.img0)
        assert result == ''

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(
                {
                    'fimg': (
                        file := obj.IMG_DIR.joinpath('ctr-1808-08-25.png')
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
                    'fimg': obj.IMG_DIR.joinpath('letter.png'),
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
                    'fimg': (file := obj.IMG_DIR.joinpath('letter.png')),
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
        assert pkg.inverted_image(**entrance) == expected
