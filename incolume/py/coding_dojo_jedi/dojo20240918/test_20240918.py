"""Test module."""

from typing import NoReturn
import incolume.py.coding_dojo_jedi.dojo20240918 as pkg
import pytest


class TestRaspagemWebReportIBGE:
    """Test case class."""

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param('', True, marks=pytest.mark.webtest),
        ],
    )
    def test_download(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert pkg.download_html(entrance) == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param('', True),
        ],
    )
    def test_scrap_estados(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert pkg.scrap_estados(entrance) == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param('', True, marks=pytest.mark.webtest),
        ],
    )
    def test_bandeiras(self, entrance, expected) -> NoReturn:
        """Unittest."""
        expected = 28
        result = pkg.identify_bandeiras(entrance)
        assert len(result) == expected

    def test_load_from_json(self) -> NoReturn:
        """Unittest."""
        assert all(
            isinstance(x, pkg.UnidadesFederativas)
            for x in pkg.load_estados_from_json()
        )

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param('', None, marks=pytest.mark.webtest),
        ],
    )
    def test_0(self, entrance, expected) -> NoReturn:
        """Unittest."""
        expected = ''
        assert pkg.add_bandeiras(entrance) == expected
