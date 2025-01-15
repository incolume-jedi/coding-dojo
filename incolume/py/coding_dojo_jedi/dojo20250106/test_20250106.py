"""Test module."""

from __future__ import annotations
from pathlib import Path
from typing import ClassVar, NoReturn
import incolume.py.coding_dojo_jedi.dojo20250106 as pkg
import pytest
from incolume.py.coding_dojo_jedi.utils import genfile


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
                {
                    'fimg': pkg.IMG_DIR.joinpath('ctr-1808-08-25.png'),
                },
                None,
                marks=[
                    pytest.mark.xpass(
                        reason='Implementation failing (but shoulded ran)',
                    ),
                ],
            ),
            pytest.param(
                {
                    'fimg': pkg.IMG_DIR.joinpath('letter.png'),
                    'foutput': genfile(suffix='.png'),
                },
                None,
                marks=[
                    pytest.mark.xpass(
                        reason='Implementation failing (but shoulded ran)',
                    ),
                ],
            ),
            pytest.param(
                {
                    'fimg': pkg.IMG_DIR.joinpath('letter.png'),
                },
                None,
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
