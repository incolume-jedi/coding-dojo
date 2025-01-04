"""Unittest TDD for dojo."""

# !/usr/bin/env python
from os import environ
import respx
import pytest
import httpx
import incolume.py.coding_dojo_jedi.dojo20220721 as pkg
from http import HTTPStatus
from typing import NoReturn
import ast


class TestProspectionMocked:
    """Mock Test case class."""

    def test_0(self) -> NoReturn:
        """Unittest."""

    def test_context_status_code(self) -> NoReturn:
        """Unittest."""
        with respx.mock() as respx_mock:
            my_route = respx_mock.get('https://example.org/')
            response = httpx.get('https://example.org/')
            assert my_route.called
            assert response.status_code == HTTPStatus.OK

    def test_context_url(self) -> NoReturn:
        """Unittest."""
        with respx.mock() as respx_mock:
            my_route = respx_mock.get(pkg.url)
            response = httpx.get(pkg.url)
            assert my_route.called
            assert response.status_code == HTTPStatus.OK

    def test_context_text(self) -> NoReturn:
        """Unittest."""
        with respx.mock() as respx_mock:
            my_route = respx_mock.get(pkg.url).mock(
                return_value=httpx.Response(
                    200,
                    text='Baz',
                ),
            )
            response = httpx.get(pkg.url)
            assert my_route.called
            assert response.status_code == HTTPStatus.OK
            assert response.text == 'Baz'

    def test_context_content(self) -> NoReturn:
        """Unittest."""
        with respx.mock() as respx_mock:
            my_route = respx_mock.get(pkg.url).mock(
                return_value=httpx.Response(
                    200,
                    content=b'Baz',
                ),
            )
            response = httpx.get(pkg.url)
            assert my_route.called
            assert response.status_code == HTTPStatus.OK
            assert response.content == b'Baz'

    def test_context_json(self) -> NoReturn:
        """Unittest."""
        expected = {'b': 'Braz'}
        with respx.mock() as respx_mock:
            my_route = respx_mock.get(pkg.url).mock(
                return_value=httpx.Response(
                    200,
                    json=ast.literal_eval(str(expected)),
                ),
            )
            response = httpx.get(pkg.url)
            assert my_route.called
            assert response.status_code == HTTPStatus.OK
            assert response.json() == expected


class TestCase:
    """Mock Test case class."""

    timeout = float(environ.get('TIMEOUT', '9'))

    def test_mocked_saudation(self, capsys) -> NoReturn:
        """Unittest."""
        expected = {'name': 'Luke Skywalker'}
        with respx.mock() as respx_mock:
            my_route = respx_mock.get(pkg.url).mock(
                return_value=httpx.Response(
                    HTTPStatus.OK,
                    json=ast.literal_eval(str(expected)),
                ),
            )

            pkg.saudacao(self.timeout)
            assert my_route.called
            output = capsys.readouterr()
            assert output.out.strip() == 'Hello, Luke Skywalker!'

    @pytest.mark.webtest
    @pytest.mark.offci
    @pytest.mark.xfail(reason='failing web connection (but shoulded ran)')
    def test_saudacao(self, capsys) -> None:
        """Test saudacao."""
        pkg.saudacao(self.timeout)
        output = capsys.readouterr()
        assert output.out.strip() == 'Hello, Luke Skywalker!'
