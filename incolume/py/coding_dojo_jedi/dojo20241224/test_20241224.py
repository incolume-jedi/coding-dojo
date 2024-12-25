"""Test module."""

from pathlib import Path
from tempfile import gettempdir
from typing import ClassVar, NoReturn
from collections.abc import Container
import incolume.py.coding_dojo_jedi.dojo20241224 as pkg
import pytest
import mimetypes
from icecream import ic
from incolume.py.coding_dojo_jedi.utils import check_connectivity

# ruff: noqa: ERA001


@pytest.mark.webtest
@pytest.mark.slow
@pytest.mark.skipif(
    not check_connectivity(),
    reason='This test need network connectivity.',
)
class TestPresidenteFoto:
    """Test case class."""

    t0: ClassVar = None

    def test_source(self):
        """Unittest."""
        assert pkg.SOURCE.is_file()

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param({}, 'dojo_review.json'),
            pytest.param(
                {
                    'output': (
                        file := Path(gettempdir(), 'presidente.json').resolve()
                    ),
                },
                file.as_posix(),
            ),
        ],
    )
    def test_review(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert pkg.dojo_review(**entrance).is_file()
        assert pkg.dojo_review(**entrance).as_posix() == expected

    def test_title_len(self):
        """Unittest."""
        assert len(pkg.title)

    def test_title_type(self):
        """Unittest."""
        assert isinstance(pkg.title, Container)
        assert len(pkg.title)

    @pytest.mark.parametrize(
        'entrance',
        [
            pytest.param('NR', marks=[]),
            pytest.param('PRESIDENTE', marks=[]),
            pytest.param('FOTOGRAFIA', marks=[]),
            pytest.param('MANDATO', marks=[]),
            pytest.param('PARTIDO', marks=[]),
            pytest.param('VICE-PRESIDENTE(S)', marks=[]),
            pytest.param('REFERÊNCIAS E NOTAS', marks=[]),
            pytest.param('ELEIÇÃO', marks=[]),
        ],
    )
    def test_title_content(self, entrance):
        """Unittest."""
        assert entrance in pkg.title

    def test_1(self):
        """Unittest."""
        assert set(pkg.content_to_dataframe().columns) == set(pkg.title)

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(
                {
                    'url_or_path': pkg.URL,
                    'file_type': 'json',
                    'output': Path(gettempdir(), 'presidente.json').resolve(),
                },
                'presidente.json',
            ),
            pytest.param(
                {
                    'url_or_path': pkg.URL,
                    'file_type': 'csv',
                    'output': Path(gettempdir(), 'presidente.json').resolve(),
                },
                'presidente.csv',
            ),
            pytest.param(
                {
                    'url_or_path': pkg.URL,
                    'file_type': 'excel',
                    'output': Path(gettempdir(), 'presidente.json').resolve(),
                },
                'presidente.xlsx',
            ),
        ],
    )
    def test_2(self, entrance, expected):
        """Unittest."""
        file = pkg.dojo(**entrance)
        assert file.is_file()
        assert file.name == expected

    @pytest.mark.parametrize(
        'entrance',
        [
            pytest.param(
                {'file_type': None},
                marks=[],
            ),
            pytest.param(
                {'file_type': 'tsv'},
                marks=[],
            ),
        ],
    )
    def test_2_exceptions(self, entrance):
        """Unittest."""
        with pytest.raises(TypeError, match=''):
            assert pkg.dojo(**entrance).name

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(
                {
                    'url_or_path': pkg.URL,
                    'file_type': 'json',
                    'output': Path(gettempdir(), 'presidente.json').resolve(),
                },
                'application/json',
            ),
            pytest.param(
                {
                    'url_or_path': pkg.URL,
                    'file_type': 'csv',
                    'output': Path(gettempdir(), 'presidente.json').resolve(),
                },
                'text/csv',
            ),
            pytest.param(
                {
                    'url_or_path': pkg.URL,
                    'file_type': 'excel',
                    'output': Path(gettempdir(), 'presidente.json').resolve(),
                },
                'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                marks=[
                    pytest.mark.skip(reason='Falso positivo'),
                ],
            ),
        ],
    )
    def test_mime_type(self, entrance, expected):
        """Unittest."""
        file = pkg.dojo(**entrance)
        mime = mimetypes.MimeTypes()
        ic(file)
        assert file.is_file()
        assert mime.guess_type(file)[0] == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(
                'https://pt.wikipedia.org/wiki/Lista_de_presidentes_do_Brasil',
                str,
            ),
            pytest.param(
                None,
                Path,
                marks=[],
            ),
            pytest.param(
                pkg.SOURCE,
                Path,
                marks=[],
            ),
            pytest.param(
                Path(pkg.SOURCE),
                Path,
                marks=[],
            ),
        ],
    )
    def test_valid_url_or_path(self, entrance, expected):
        """Unittest."""
        assert isinstance(pkg.valid_url_or_path(entrance), expected)

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(
                'https://pt.wikipedia.org/wiki/Lista_de_presidentes_do_Brasil',
                list,
            ),
            pytest.param(
                pkg.Path,
                Path,
                marks=[pytest.mark.skip],
            ),
        ],
    )
    def test_get_foto(self, entrance, expected):
        """Unittest."""
        assert isinstance(pkg.get_foto(entrance), expected)

    def test_fotos2string(self):
        """Unittest."""
        entrance = pkg.get_foto(pkg.URL)
        expected = True
        assert (
            all(isinstance(foto, str) for foto in pkg.fotos2string(entrance))
            == expected
        )
