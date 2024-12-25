"""dojo module."""

import base64
import inspect
import itertools
from pathlib import Path
from typing import Final, Literal, TypeAlias
from urllib.parse import urljoin

import httpx
import pandas as pd
from bs4 import BeautifulSoup
from icecream import ic
from incolume.py.coding_dojo_jedi.dojo20231221 import dojo as v1

Types: TypeAlias = Literal['excel', 'csv', 'json']
Fotos: TypeAlias = list[str]
URL: Final[str] = (
    'https://pt.wikipedia.org/wiki/Lista_de_presidentes_do_Brasil'
)
SOURCE: Final[Path] = (
    Path(__file__)
    .parents[1]
    .joinpath('dojo20231221', 'presidentes_brasileiros_wikipedia.html')
)


def valid_url_or_path(
    url_or_path: str | Path = '',
    default: str | Path = SOURCE,
) -> str | Path:
    """Identify path or URL."""
    if not url_or_path:
        url_or_path = default

    if isinstance(url_or_path, str) and 'http' in url_or_path:
        return url_or_path

    url_or_path = Path(url_or_path)
    ic(url_or_path)
    return url_or_path


def dojo_review(
    url_or_path: str | Path = '',
    output: Path | str = '',
) -> dict[str]:
    """Dojo review."""
    url_or_path = Path(url_or_path or SOURCE)
    ic(url_or_path)
    output = Path(output or f'{inspect.stack()[0][3]}.json')
    ic(output)
    return v1(url_or_path, output=output)


title: Final[list[str]] = [
    'NR',
    'PRESIDENTE',
    'FOTOGRAFIA',
    'MANDATO',
    'PARTIDO',
    'VICE-PRESIDENTE(S)',
    'REFERÊNCIAS E NOTAS',
    'ELEIÇÃO',
]


def content_to_dataframe(
    url_or_path: str | Path = '',
    output: str | Path = '',
) -> pd.DataFrame:
    """Dojo solution."""
    url_or_path = valid_url_or_path(url_or_path)
    ic(url_or_path)

    output = Path(output or f'{inspect.stack()[0][3]}.json')
    ic(output)

    dataframe = pd.read_html(url_or_path)[0]
    dataframe.columns = title

    # Sanitização
    q = dataframe[
        dataframe.PRESIDENTE.str.lower().str.contains('república')
    ].index
    ic(q)
    dataframe = dataframe.drop(q)

    dataframe = dataframe.drop_duplicates(
        subset=['PRESIDENTE', 'MANDATO'],
        ignore_index=True,
        keep='last',
    )

    ic(dataframe)
    ic(dataframe.columns)
    ic(dataframe.shape)

    return dataframe


def get_foto(url_or_path: str | Path = '') -> Fotos:
    """Get presidente fotograph."""
    url_or_path = valid_url_or_path(url_or_path)
    result, fotos = [], []
    try:
        response = httpx.get(url_or_path)
        content = response.content
    except TypeError:
        content = url_or_path.read_bytes()

    soup = BeautifulSoup(content, 'html5lib')
    ic(soup.table)

    fotos.extend(x.get('src') for x in soup.table.select('img'))
    ic(fotos)

    result.extend(map(urljoin, itertools.cycle([url_or_path]), fotos))
    ic(result)

    return result


def fotos2string(url_fotos: list[str]) -> list[str]:
    """Download fotos and encoded base64 format."""
    fotos = [httpx.get(foto).content for foto in url_fotos[:]]
    ic(fotos)
    result = [base64.b64encode(foto).decode() for foto in fotos]
    ic(result)
    return result


def dojo(
    url_or_path: str | Path = '',
    output: str | Path = '',
    file_type: Types = 'json',
) -> Path:
    """Dojo solution."""
    output = Path(output or f'{inspect.stack()[0][3]}')
    output = output.with_suffix(
        f'.{"xlsx" if file_type == "excel" else file_type}',
    )
    ic(output)

    presidentes = content_to_dataframe(url_or_path, output)
    ic(f'>>>>>>>>>>>>>>>>>>>{len(presidentes)}')

    fotos = fotos2string(get_foto(url_or_path))
    ic(f'>>>>>>>>>>>>>>>>>>>{len(fotos)}')

    presidentes.FOTOGRAFIA = fotos
    ic(presidentes.FOTOGRAFIA)

    fields = [
        'PRESIDENTE',
        'VICE-PRESIDENTE(S)',
        'FOTOGRAFIA',
        'MANDATO',
        'PARTIDO',
    ]

    match file_type:
        case 'excel':
            with pd.ExcelWriter(output, engine='openpyxl') as writer:
                presidentes[fields].to_excel(writer, index=False)
        case 'csv':
            presidentes[fields].to_csv(output, index=False)
        case 'json':
            presidentes[fields].to_json(output, indent=2, orient='records')
        case _:
            msg = 'Invalid Type.'
            raise TypeError(msg)
    return output
