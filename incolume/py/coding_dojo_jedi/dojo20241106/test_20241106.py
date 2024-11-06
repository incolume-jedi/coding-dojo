"""Test module."""

from typing import ClassVar, NoReturn
import incolume.py.coding_dojo_jedi.dojo20241106 as pkg
import pytest
import respx
import httpx
from http import HTTPStatus


class TestRESPX:
    """Examples for respx."""

    @respx.mock
    def test_decorator(self):
        """Example."""
        my_route = respx.get('https://example.org/')
        response = httpx.get('https://example.org/')
        assert my_route.called
        assert response.status_code == HTTPStatus.OK

    def test_ctx_manager(self):
        """Example."""
        with respx.mock:
            my_route = respx.get('https://example.org/')
            response = httpx.get('https://example.org/')
            assert my_route.called
            assert response.status_code == HTTPStatus.OK

    def test_fixture(self, respx_mock):
        """Example."""
        my_route = respx_mock.get('https://example.org/')
        response = httpx.get('https://example.org/')
        assert my_route.called
        assert response.status_code == HTTPStatus.OK

    @pytest.mark.respx(base_url='https://foo.bar')
    def test_with_marker(self, respx_mock):
        """Example."""
        respx_mock.get('/baz/').mock(return_value=httpx.Response(204))
        response = httpx.get('https://foo.bar/baz/')
        assert response.status_code == HTTPStatus.NO_CONTENT


class TestCase:
    """Test case class."""

    t0: ClassVar = None

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            (
                'MDT',
                "Código de moeda inválido. Use ('USD', 'EUR', 'ETH', 'BTC')",
            ),
            (
                '\x11',
                "Código de moeda inválido. Use ('USD', 'EUR', 'ETH', 'BTC')",
            ),
        ],
    )
    def test_0(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert pkg.quotation(entrance) == expected

    @respx.mock
    def test_1(self) -> NoReturn:
        """Unittest."""
        entrance = 'USD'
        expected = 'Última cotação: 5.7721'
        mocked_resp = httpx.Response(
            200,
            json={
                'USDBRL': {
                    'ask': 5.7721,
                },
            },
        )
        respx.get(pkg.URL_API.format(entrance)).mock(mocked_resp)
        result = pkg.quotation(entrance)

        assert result == expected

    @respx.mock
    def test_2(self) -> NoReturn:
        """Unittest."""
        entrance = 'USD'
        expected = 'Erro de conexão com a rede.'
        respx.get(pkg.URL_API.format(entrance)).mock(
            side_effect=httpx.ConnectError,
        )
        result = pkg.quotation(entrance)

        assert result == expected

    def test_3(self, respx_mock) -> NoReturn:
        """Unittest."""
        entrance = 'USD'
        expected = 'Tempo de conexão expirou, tente mais tarde.'
        respx_mock.get(pkg.URL_API.format(entrance)).mock(
            side_effect=httpx.TimeoutException,
        )
        result = pkg.quotation(entrance)

        assert result == expected

    @pytest.mark.parametrize(
        'entrance json expected'.split(),
        [
            pytest.param(
                'usd',
                {
                    'USDBRL': {
                        'code': 'USD',
                        'codein': 'BRL',
                        'name': 'Dólar Americano/Real Brasileiro',
                        'high': '5.8604',
                        'low': '5.739',
                        'varBid': '0.039',
                        'pctChange': '0.68',
                        'bid': '5.7892',
                        'ask': '5.7905',
                        'timestamp': '1730900947',
                        'create_date': '2024-11-06 10:49:07',
                    },
                },
                'Última cotação: 5.7905',
            ),
            pytest.param(
                'USD',
                {},
                5.7821,
            ),
            pytest.param(
                'eur',
                {
                    'EURBRL': {
                        'code': 'USD',
                        'codein': 'BRL',
                        'name': 'Dólar Americano/Real Brasileiro',
                        'high': '5.8604',
                        'low': '5.739',
                        'varBid': '0.039',
                        'pctChange': '0.68',
                        'bid': '5.7892',
                        'ask': '5.7905',
                        'timestamp': '1730900947',
                        'create_date': '2024-11-06 10:49:07',
                    },
                },
                0,
            ),
            pytest.param(
                'eth',
                {
                    'ETHBRL': {
                        'code': 'USD',
                        'codein': 'BRL',
                        'name': 'Dólar Americano/Real Brasileiro',
                        'high': '5.8604',
                        'low': '5.739',
                        'varBid': '0.039',
                        'pctChange': '0.68',
                        'bid': '5.7892',
                        'ask': '5.7905',
                        'timestamp': '1730900947',
                        'create_date': '2024-11-06 10:49:07',
                    },
                },
                0,
            ),
            pytest.param(
                'btc',
                {
                    'BTCBRL': {
                        'code': 'USD',
                        'codein': 'BRL',
                        'name': 'Dólar Americano/Real Brasileiro',
                        'high': '5.8604',
                        'low': '5.739',
                        'varBid': '0.039',
                        'pctChange': '0.68',
                        'bid': '5.7892',
                        'ask': '5.7905',
                        'timestamp': '1730900947',
                        'create_date': '2024-11-06 10:49:07',
                    },
                },
                0,
            ),
        ],
    )
    def test_4(self, entrance, json, expected) -> NoReturn:
        """Unittest."""
        url = pkg.URL_API.format(entrance)
        mocked_resp = httpx.Response(
            HTTPStatus.OK,
            json=json,
        )
        assert (
            url == f'https://economia.awesomeapi.com.br/json/last/{entrance}'
        )

        with respx.mock:
            my_route = respx.get(url)
            my_route.mock(mocked_resp)
            result = pkg.quotation(entrance)

            assert my_route.called
            assert result == expected
