"""dojo module."""

import inspect
from pathlib import Path
from typing import Final, Literal, TypeAlias

import httpx
import pandas as pd
from bs4 import BeautifulSoup
from icecream import ic
from incolume.py.coding_dojo_jedi.dojo20231221 import dojo as v1

Types: TypeAlias = Literal['excel', 'csv', 'json']

SOURCE: Final[Path] = (
    Path(__file__)
    .parents[1]
    .joinpath('dojo20231221', 'presidentes_brasileiros_wikipedia.html')
)


def valid_url_or_path(url_or_path: str | Path = '') -> str | Path:
    """Identify path or URL."""
    if not url_or_path:
        url_or_path = SOURCE
    elif isinstance(url_or_path, Path) or 'http' in url_or_path:
        pass
    else:
        url_or_path = Path(url_or_path)
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
    url_or_path = Path(url_or_path or SOURCE)
    ic(url_or_path)

    output = Path(output or f'{inspect.stack()[0][3]}.json')
    ic(output)

    dataframe = pd.read_html(url_or_path)[0]

    dataframe.columns = title

    ic(dataframe)
    ic(dataframe.columns)

    return dataframe


def get_foto(url_or_path: str | Path = '') -> list[str]:
    """Get presidente fotograph."""
    if not url_or_path:
        url_or_path = SOURCE
    elif isinstance(url_or_path, Path) or 'http' in url_or_path:
        pass
    else:
        url_or_path = Path(url_or_path)

    try:
        response = httpx.get(url_or_path)
        content = response.content
    except TypeError:
        content = url_or_path.read_bytes()

    soup = BeautifulSoup(content, 'html5lib')

    result = [x.get('src') for x in soup.table.select('img')]
    ic(result)
    return result


def dojo(
    url_or_path: str | Path = '',
    output: str | Path = '',
    file_type: Types = 'json',
) -> Path:
    """Dojo solution."""
    url_or_path = Path(url_or_path or SOURCE)

    output = Path(output or f'{inspect.stack()[0][3]}')
    output = output.with_suffix(
        f'.{"xlsx" if file_type == "excel" else file_type}',
    )
    ic(output)

    presidentes = content_to_dataframe(url_or_path, output)
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
