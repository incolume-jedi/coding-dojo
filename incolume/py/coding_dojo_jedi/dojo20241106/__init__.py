"""dojo module."""

from typing import Literal, TypeAlias, get_args

import httpx

URL_API = 'https://economia.awesomeapi.com.br/json/last/{}'

Moeda: TypeAlias = Literal['USD', 'EUR', 'ETH', 'BTC']


def quotation(moeda: Moeda) -> str:
    """Dojo solution."""
    code = f'{moeda.upper()}-BRL'
    try:
        response = httpx.get(URL_API.format(moeda))
        result = response.json()[code.replace('-', '')]
        return f'Última cotação: {result["ask"]}'
    except (KeyError, httpx.InvalidURL):
        return f'Código de moeda inválido. Use {get_args(Moeda)}'
    except httpx.ConnectError:
        return 'Erro de conexão com a rede.'
    except httpx.TimeoutException:
        return 'Tempo de conexão expirou, tente mais tarde.'
