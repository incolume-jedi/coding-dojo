"""Unittest TDD for dojo."""

# !/usr/bin/env python
from os import environ
import respx
import pytest
import httpx
import incolume.py.coding_dojo_jedi.dojo20220721 as pkg
from http import HTTPStatus
from typing import NoReturn


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


@pytest.mark.webtest
def test_saudacao(capsys) -> None:
    """Test saudacao."""
    timeout = float(environ.get('TIMEOUT', '9'))
    pkg.saudacao(timeout)
    output = capsys.readouterr()
    assert output.out.strip() == 'Hello, Luke Skywalker!'
