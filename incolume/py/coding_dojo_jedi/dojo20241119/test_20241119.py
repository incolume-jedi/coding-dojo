"""Test module."""

import incolume.py.coding_dojo_jedi.dojo20241119 as pkg
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
            pytest.param(
                {
                    'file': Path(__file__)
                    .parents[1]
                    .joinpath(
                        'dojo20241118',
                        'files',
                        'filepdf.pdf',
                    ),
                },
                '',
                marks=[],
            ),
            pytest.param(
                {'file': Path(pkg.artefatos['path'][0]).as_posix()},
                b'',
                marks=[],
            ),
            pytest.param({'file': ''}, '', marks=[]),
            pytest.param({'file': Path()}, '', marks=[]),
        ],
    )
    def test_0(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert pkg.dojo(**entrance) == expected
