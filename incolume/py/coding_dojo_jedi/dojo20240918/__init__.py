"""dojo module."""

from __future__ import annotations

import base64
import json
import logging
from dataclasses import asdict, dataclass
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

import httpx
import pandas as pd
from bs4 import BeautifulSoup
from icecream import ic
from unidecode import unidecode

url_default: str = 'https://www.todamateria.com.br/estados-do-brasil/'
dir_report: Path = Path(__file__).parent
json_report: Path = dir_report / 'estados.json'
regioes_estados: dict[str, list[str]] = {
    'Norte': 'AC AP AM PA RO RR TO'.split(),
    'Nordeste': 'MA PI CE RN PB PE AL SE BA'.split(),
    'Centro-Oeste': 'DF GO MT MS'.split(),
    'Sul': 'PR SC RS'.split(),
    'Sudeste': 'SP RJ MG ES'.split(),
}
estados_regioes = {e: r for r, v in regioes_estados.items() for e in v}


@dataclass()
class UnidadesFederativas:
    """Estados Brasileiros."""

    UF: str
    SIGLA: str
    CAPITAL: str
    REGIAO: str
    BANDEIRA: bytes = b''

    def as_dict(self):
        """To dict."""
        return asdict(self)


def download_html(page: str = '', fout: Path | None = None) -> bool:
    """Baixar a pagina principal de todamateria."""
    page = page or url_default
    fout = fout or Path(__file__).parent / 'index.html'

    if not fout.is_file():
        response = httpx.get(page)
        soup = BeautifulSoup(response.content, 'html5lib')
        fout.write_bytes(soup.prettify(encoding='utf-8'))

    return fout.is_file()


def scrap_estados(
    page: Path | None = None,
    json_out: Path | None = None,
) -> bool:
    """Raspagem da lista de estados no site todamateria."""
    page = page or Path(__file__).parent / 'index.html'
    json_out = json_out or json_report
    response = pd.read_html(page)
    estados = response[0]
    ic(estados.tail())
    estados = estados.rename({'Estado': 'uf'}, axis=1)
    estados.loc[len(estados)] = ['Distrito Federal', 'DF', 'Brasília']

    estados.columns = estados.columns.str.upper().map(unidecode)
    estados['REGIAO'] = estados.SIGLA.map(estados_regioes.get)

    estados.to_json(json_out, orient='records', indent=2)

    return json_out.is_file()


def identify_bandeiras(page: Path | None = None) -> list[dict[str, str]]:
    """Raspagem de bandeiras no site todamateria."""
    page = page or Path(__file__).parent / 'index.html'
    result: list = []
    soup = BeautifulSoup(page.read_bytes(), 'html5lib')
    figures = soup.select('figure img')
    ic(figures)
    for img in figures:
        element = urlsplit(img.attrs['src'])
        key = img.attrs['alt']

        if 'bandeira' in key.casefold():
            result.append({
                ' '.join(key.split()[2:]): urlunsplit([
                    element.scheme,
                    element.netloc,
                    element.path,
                    'width=150',
                    '',
                ]),
            })
        else:
            result.append({
                ''.join(key.split()[3:]): urlunsplit([
                    element.scheme,
                    element.netloc,
                    element.path,
                    '',
                    '',
                ]),
            })

    return ic(result)


def load_estados_from_json(
    json_filename: Path | None = None,
) -> list[UnidadesFederativas]:
    """Load estrados from json."""
    json_filename = json_filename or json_report
    with json_filename.open('rb') as f:
        result = [UnidadesFederativas(**estado) for estado in json.load(f)]
    logging.debug(result)
    return result


def add_bandeiras(
    estados: list[UnidadesFederativas] | None = None,
    bandeiras: list[dict[str, str]] | None = None,
) -> list[UnidadesFederativas]:
    """Add flags to objects."""
    estados = estados or load_estados_from_json()
    bandeiras = bandeiras or identify_bandeiras()
    for estado in estados:
        for bandeira in bandeiras:
            key = next(iter(bandeira.keys()))
            logging.debug(key)
            if key == estado.UF:
                estado.BANDEIRA = bandeira.get(key)

    df_uf = pd.DataFrame([uf.as_dict() for uf in estados])
    ic(df_uf)
    for idx, item in df_uf.iterrows():
        logging.debug(idx)
        response = httpx.get(ic(item.BANDEIRA))
        base64_bytes = base64.b64encode(response.content)
        obj_b64 = base64_bytes.decode()
        df_uf.loc[df_uf.UF == item.UF].BANDEIRA = obj_b64

    return df_uf.head()
