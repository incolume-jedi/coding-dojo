"""Module."""

from pathlib import Path
from typing import ClassVar

import pytest

from . import CBF

__author__ = '@britodfbr'  # pragma: no cover


class TestCaseCBF:
    """Test case."""

    url: ClassVar = 'http://localhost:8000'
    test_case_0: ClassVar = [
        pytest.param(
            'http://localhost:8000',
            '',
            marks=[pytest.mark.webtest, pytest.mark.offci],
        ),
        pytest.param(
            Path(__file__).parent.joinpath('index.html').as_posix(),
            '',
        ),
    ]

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        test_case_0,
    )
    def test_content(self, entrance, expected):
        """Test content."""
        expected = True
        obj = CBF(entrance)
        assert isinstance(obj.content, dict) == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        test_case_0,
    )
    def test_sort_by_name(self, entrance, expected):
        """Test sort."""
        obj = CBF(entrance)
        expected = [
            'América-MG',
            'Athletico-PR',
            'Atlético-GO',
            'Atlético-MG',
            'Bahia',
            'Bragantino',
            'Ceará SC',
            'Chapecoense',
            'Corinthians',
            'Cuiabá',
            'Flamengo',
            'Fluminense',
            'Fortaleza',
            'Grêmio',
            'Internacional',
            'Juventude',
            'Palmeiras',
            'Santos',
            'Sport Recife',
            'São Paulo',
        ]
        assert obj.sort_by_name() == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        test_case_0,
    )
    def test_sort_by_point(self, entrance, expected):
        """Test sort."""
        obj = CBF(entrance)
        expected = [
            'Chapecoense',
            'Sport Recife',
            'Bahia',
            'Grêmio',
            'Juventude',
            'Athletico-PR',
            'Cuiabá',
            'São Paulo',
            'Internacional',
            'Santos',
            'Ceará SC',
            'Atlético-GO',
            'América-MG',
            'Fluminense',
            'Bragantino',
            'Corinthians',
            'Fortaleza',
            'Palmeiras',
            'Flamengo',
            'Atlético-MG',
        ]
        assert obj.sort_by_point() == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        test_case_0,
    )
    def test_classify(self, entrance, expected):
        """Test classify."""
        obj = CBF(entrance)
        expected = [
            'Atlético-MG',
            'Flamengo',
            'Palmeiras',
            'Fortaleza',
            'Corinthians',
            'Bragantino',
            'Fluminense',
            'América-MG',
            'Atlético-GO',
            'Ceará SC',
            'Santos',
            'Internacional',
            'São Paulo',
            'Cuiabá',
            'Athletico-PR',
            'Juventude',
            'Grêmio',
            'Bahia',
            'Sport Recife',
            'Chapecoense',
        ]
        assert obj.classify() == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        test_case_0,
    )
    def test_libertadores(self, entrance, expected):
        """Test classify."""
        obj = CBF(entrance)
        expected = [
            'Atlético-MG',
            'Flamengo',
            'Palmeiras',
            'Fortaleza',
        ]
        assert obj.classify_libertadores() == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        test_case_0,
    )
    def test_qualific_libertadores(self, entrance, expected):
        """Test classify."""
        obj = CBF(entrance)
        expected = [
            'Corinthians',
            'Bragantino',
        ]
        assert obj.qualify_libertadores() == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        test_case_0,
    )
    def test_sulamericana(self, entrance, expected):
        """Test classify."""
        obj = CBF(entrance)
        expected = [
            'Fluminense',
            'América-MG',
            'Atlético-GO',
            'Ceará SC',
            'Santos',
            'Internacional',
        ]
        assert obj.select_sulamericana() == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        test_case_0,
    )
    def test_rebaixados(self, entrance, expected):
        """Test classify."""
        obj = CBF(entrance)
        expected = ['Grêmio', 'Bahia', 'Sport Recife', 'Chapecoense']
        assert obj.rebaixados() == expected

    @pytest.mark.parametrize(
        'url_path entrance expected'.split(),
        [
            pytest.param(
                'http://localhost:8000',
                'Chapecoense',
                15,
                marks=[pytest.mark.webtest, pytest.mark.offci],
            ),
            pytest.param(
                'http://localhost:8000',
                'Grêmio',
                43,
                marks=[pytest.mark.webtest, pytest.mark.offci],
            ),
            pytest.param(
                'http://localhost:8000',
                'Bahia',
                43,
                marks=[pytest.mark.webtest, pytest.mark.offci],
            ),
            pytest.param(
                'http://localhost:8000',
                'Sport Recife',
                38,
                marks=[pytest.mark.webtest, pytest.mark.offci],
            ),
            (
                Path(__file__).parent.joinpath('index.html').as_posix(),
                'Chapecoense',
                15,
            ),
            (
                Path(__file__).parent.joinpath('index.html').as_posix(),
                'Grêmio',
                43,
            ),
            (
                Path(__file__).parent.joinpath('index.html').as_posix(),
                'Bahia',
                43,
            ),
            (
                Path(__file__).parent.joinpath('index.html').as_posix(),
                'Sport Recife',
                38,
            ),
            (
                Path(__file__).parent.joinpath('index.html').as_posix(),
                'flamengo',
                71,
            ),
            (
                Path(__file__).parent.joinpath('index.html').as_posix(),
                'atletico-mg',
                84,
            ),
        ],
    )
    def test_por_nome(self, url_path, entrance, expected):
        """Test classify."""
        obj = CBF(url_path)
        assert obj.clube(entrance) == expected
