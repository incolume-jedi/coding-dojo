"""Unittest TDD for dojo."""

# !/usr/bin/env python
from os import environ
import respx
import pytest
import httpx
import incolume.py.coding_dojo_jedi.dojo20220721 as pkg
from http import HTTPStatus
from typing import NoReturn
import json


class TestMocked:
    """Mock Test case class."""

    def test_0(self) -> NoReturn:
        """Unittest."""

    def test_context(self) -> NoReturn:
        """Unittest."""
        with respx.mock() as respx_mock:
            my_route = respx_mock.get('https://example.org/')
            response = httpx.get('https://example.org/')
            assert my_route.called
            assert response.status_code == HTTPStatus.OK

    def test_context_1(self) -> NoReturn:
        """Unittest."""
        with respx.mock() as respx_mock:
            my_route = respx_mock.get(pkg.url)
            response = httpx.get(pkg.url)
            assert my_route.called
            assert response.status_code == HTTPStatus.OK

    def test_context_2(self) -> NoReturn:
        """Unittest."""
        with respx.mock() as respx_mock:
            my_route = respx_mock.get(pkg.url).mock(
                return_value=httpx.Response(
                    200,
                    text='Baz',
                    json=json.loads(json.dumps({'b': 'Baz'})),
                ),
            )
            response = httpx.get(pkg.url)
            assert my_route.called
            assert response.status_code == HTTPStatus.OK
            assert response.text == 'Baz'
            assert response.content == b'Baz'
            assert response.json() == ''


@pytest.mark.webtest
def test_saudacao(capsys) -> None:
    """Test saudacao."""
    timeout = float(environ.get('TIMEOUT', '9'))
    pkg.saudacao(timeout)
    output = capsys.readouterr()
    assert output.out.strip() == 'Hello, Luke Skywalker!'
