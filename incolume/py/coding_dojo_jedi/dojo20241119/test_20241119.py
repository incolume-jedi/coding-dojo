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
                'application/pdf',
                marks=[pytest.importorskip('magic')],
            ),
            pytest.param(
                {'file': pkg.artefatos['path'][0].as_posix()},
                'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
                marks=[pytest.importorskip('magic')],
            ),
            pytest.param(
                {'file': pkg.artefatos['path'][1].as_posix()},
                'application/vnd.oasis.opendocument.text',
                marks=[pytest.importorskip('magic')],
            ),
            pytest.param(
                {'file': pkg.artefatos['path'][2].as_posix()},
                'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                marks=[pytest.importorskip('magic')],
            ),
            pytest.param(
                {'file': pkg.artefatos['path'][3].as_posix()},
                'application/pdf',
                marks=[pytest.importorskip('magic')],
            ),
            pytest.param(
                {
                    'file': Path(__file__)
                    .parents[1]
                    .joinpath(
                        'dojo20241118',
                        'files',
                        'filepdf.pdf',
                    ),
                    'method': 'filetype',
                },
                'application/pdf',
                marks=[pytest.importorskip('filetype')],
            ),
            pytest.param(
                {
                    'file': pkg.artefatos['path'][0].as_posix(),
                    'method': 'filetype',
                },
                'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
                marks=[pytest.importorskip('filetype')],
            ),
            pytest.param(
                {
                    'file': pkg.artefatos['path'][1].as_posix(),
                    'method': 'filetype',
                },
                'application/vnd.oasis.opendocument.text',
                marks=[pytest.importorskip('filetype')],
            ),
            pytest.param(
                {
                    'file': pkg.artefatos['path'][2].as_posix(),
                    'method': 'filetype',
                },
                'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                marks=[pytest.importorskip('filetype')],
            ),
            pytest.param(
                {
                    'file': pkg.artefatos['path'][3].as_posix(),
                    'method': 'filetype',
                },
                'application/pdf',
                marks=[pytest.importorskip('filetype')],
            ),
            pytest.param(
                {
                    'file': pkg.artefatos['path'][3].as_posix(),
                    'method': None,
                },
                "Método inválido utilize: ('filetype', 'magic', 'puremagic')",
                marks=[],
            ),
            pytest.param(
                {
                    'file': pkg.artefatos['path'][3].as_posix(),
                    'method': 'puremagic',
                },
                'application/pdf',
                marks=[pytest.importorskip('puremagic')],
            ),
        ],
    )
    def test_0(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert pkg.dojo(**entrance) == expected
