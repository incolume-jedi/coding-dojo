"""Test module."""

from typing import NoReturn
import incolume.py.coding_dojo_jedi.dojo20240604 as pkg
import pytest
from tempfile import NamedTemporaryFile
from pathlib import Path


class TestCase:
    """Test case class."""

    filename = Path(NamedTemporaryFile().name)

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(
                {'url': pkg.url},
                True,
                marks=[
                    pytest.mark.skip(reason='only get index.html'),
                    pytest.mark.webtest,
                ],
            ),
            pytest.param(
                {'url': pkg.url, 'fout': Path(NamedTemporaryFile().name)},
                True,
                marks=pytest.mark.webtest,
            ),
        ],
    )
    def test_download(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert pkg.download(**entrance) == expected

    def test_content(self):
        """Test content."""
        expected = True
        obj = pkg.CampionatoBrasileiro(pkg.url, self.filename)
        assert isinstance(obj.content, pkg.pd.DataFrame) == expected

    def test_sort_by_name(self):
        """Test sort."""
        expected = [
            'América-MG',
            'Athletico-PR',
            'Atlético-GO',
            'Atlético-MG',
            'Avaí',
            'Botafogo',
            'Bragantino',
            'Ceará SC',
            'Corinthians',
            'Coritiba',
            'Cuiabá',
            'Flamengo',
            'Fluminense',
            'Fortaleza',
            'Goiás',
            'Internacional',
            'Juventude',
            'Palmeiras',
            'Santos',
            'São Paulo',
        ]
        obj = pkg.CampionatoBrasileiro(pkg.url, self.filename)
        assert obj.sort_by_name() == expected

    def test_sort_by_point(self):
        """Test sort."""
        expected = [
            'Juventude',
            'Avaí',
            'Atlético-GO',
            'Ceará SC',
            'Cuiabá',
            'Coritiba',
            'Bragantino',
            'Goiás',
            'Santos',
            'Botafogo',
            'América-MG',
            'São Paulo',
            'Fortaleza',
            'Athletico-PR',
            'Atlético-MG',
            'Flamengo',
            'Corinthians',
            'Fluminense',
            'Internacional',
            'Palmeiras',
        ]
        obj = pkg.CampionatoBrasileiro(pkg.url, self.filename)
        assert obj.sort_by_point() == expected

    def test_classify(self):
        """Test classify."""
        expected = [
            'Palmeiras',
            'Internacional',
            'Fluminense',
            'Corinthians',
            'Flamengo',
            'Atlético-MG',
            'Athletico-PR',
            'Fortaleza',
            'São Paulo',
            'América-MG',
            'Botafogo',
            'Santos',
            'Goiás',
            'Bragantino',
            'Coritiba',
            'Cuiabá',
            'Ceará SC',
            'Atlético-GO',
            'Avaí',
            'Juventude',
        ]
        obj = pkg.CampionatoBrasileiro(pkg.url, self.filename)
        assert obj.classify() == expected

    def test_class_lib(self):
        """Test classify."""
        expected = ['Palmeiras', 'Internacional', 'Fluminense', 'Corinthians']
        obj = pkg.CampionatoBrasileiro(pkg.url, self.filename)
        assert obj.classify_libertadores() == expected

    def test_qua_lib(self):
        """Test classify."""
        expected = ['Flamengo', 'Atlético-MG']
        obj = pkg.CampionatoBrasileiro(pkg.url, self.filename)
        assert obj.qualify_libertadores() == expected

    def test_selc_sulameric(self):
        """Test classify."""
        expected = [
            'Athletico-PR',
            'Fortaleza',
            'São Paulo',
            'América-MG',
            'Botafogo',
            'Santos',
        ]
        obj = pkg.CampionatoBrasileiro(pkg.url, self.filename)
        assert obj.select_sulamericana() == expected

    def test_rebaixados(self):
        """Test classify."""
        expected = ['Ceará SC', 'Atlético-GO', 'Avaí', 'Juventude']
        obj = pkg.CampionatoBrasileiro(pkg.url, self.filename)
        assert obj.rebaixados() == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            ('Ceará SC', 16),
            ('Atlético-GO', 17),
            ('Avaí', 18),
            ('Juventude', 19),
        ],
    )
    def test_clube(self, entrance, expected):
        """Test classify."""
        obj = pkg.CampionatoBrasileiro(pkg.url, self.filename)
        assert obj.clube(entrance) == expected
