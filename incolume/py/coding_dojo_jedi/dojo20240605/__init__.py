"""dojo module."""

from pathlib import Path

import httpx
import pandas as pd
from bs4 import BeautifulSoup
from icecream import ic
from unidecode import unidecode

url_default: str = 'https://www.todamateria.com.br/estados-do-brasil/'
dir_report: Path = Path(__file__).parent
regioes_estados: dict[str, list[str]] = {
    'Norte': 'AC AP AM PA RO RR TO'.split(),
    'Nordeste': 'MA PI CE RN PB PE AL SE BA'.split(),
    'Centro-Oeste': 'DF GO MT MS'.split(),
    'Sul': 'PR SC RS'.split(),
    'Suldeste': 'SP RJ MG ES'.split(),
}
estados_regioes = {e: r for r, v in regioes_estados.items() for e in v}


def scrap_estados(page: str = '', json_out: Path | None = None) -> bool:
    """Raspagem da lista de estados no site todamateria."""
    page = page or url_default
    json_out = json_out or dir_report / 'report.json'
    response = pd.read_html(page)
    estados = response[0]
    ic(estados.tail())
    estados = estados.rename({'Estado': 'unidade federativa'}, axis=1)
    estados.loc[len(estados)] = ['Distrito Federal', 'DF', 'Brasília']

    estados.columns = estados.columns.str.upper().map(unidecode)
    estados['REGIAO'] = estados.SIGLA.map(estados_regioes.get)

    estados.to_json(json_out, orient='records', indent=2)

    return json_out.is_file()


def scrap_bandeiras(page: str) -> dict:
    """Raspagem de bandeiras no site todamateria."""
