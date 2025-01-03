"""dojo module."""

import dataclasses
import inspect
import logging
import pickle
import sys
from pathlib import Path
from typing import Any

from bs4 import BeautifulSoup
from icecream import ic
from tqdm import tqdm

if sys.version_info >= (3, 11):
    from typing import Literal, TypeAlias, get_args
else:
    from typing_extensions import Literal, TypeAlias, get_args  # noqa: UP035


msg = sys.platform.casefold()
logging.info(msg)
ic(msg)

directory: list[Path] = [
    Path('z:', 'acervo-legis'),
    Path(
        '//',
        'castelo',
        'saj',
        'CENTRO DE ESTUDOS',
        'EQUIPE CEJ',
        'BRITO',
        'projetos',
        'acervo-legis',
    ),
]

Extentions: TypeAlias = Literal[
    'doc',
    'docx',
    'nsf',
    'pdf',
    'rtf',
    'xls',
    'xlsx',
]


def get_list_html(path_dir: Path | None = None) -> map:
    """Return list HTML files."""
    path_dir = path_dir or directory[0]
    result = path_dir.rglob(pattern='**/*.htm*', case_sensitive=False)
    ic(result)
    return result


def get_content_html(filename: Path) -> BeautifulSoup:
    """Return HTML content."""
    with filename.open('rb') as f:
        return BeautifulSoup(f.read(), 'html5lib')


def find_list_ahref(soup: BeautifulSoup) -> list[str, str]:
    """Return a[href]."""
    return soup.select('a[href]')


def find_list_ahref_files_0(soup: BeautifulSoup) -> list[str, str]:
    """Return a[href]."""
    exts = ['doc', 'docx', 'rtf', 'xls', 'xlsx', 'nsf']
    result = []

    for ext in exts:
        result.extend(soup.select(f'a[href*={ext}]'))
    return result


def find_list_ahref_files(
    soup: BeautifulSoup,
    ext: Extentions = '',
    on_raise: Extentions = 'doc',
) -> list[str, str]:
    """Return a[href]."""
    try:
        ext = ext if ext.casefold() in get_args(Extentions) else on_raise
    except AttributeError:
        ext = on_raise
    ic(inspect.stack()[0][3], ext)
    result = []
    result.extend(soup.select(f'a[href*=".{ext}" i]'))
    return result


@dataclasses.dataclass
class Item:
    """Item."""

    file: Path
    items: list[str]


def dojo0(*, junk: int = 0, **kwargs: dict[str:Path]) -> list[Item]:
    """Dojo solution."""
    junk = max(junk, 10**5)
    result: list[Item] = []
    for idx, file in enumerate(get_list_html(kwargs.get('path_dir')), 1):
        if not idx % junk:
            f = Path(f'result{idx:0>5}.pkl')
            pickle.dump(result, f.open('wb'))
            ic(f.name)
        soup = get_content_html(file)
        res = soup.select('a[href]')
        result.append(Item(file, res))
        ic(idx, result[-1])
    return result


def dojo(**kwargs: dict[str:Any]) -> list[Item]:
    """Dojo solution."""
    result: list[Item] = []
    extentions = kwargs.get('extentions', get_args(Extentions))
    for idx, file in tqdm(enumerate(get_list_html(kwargs.get('path_dir')), 1)):
        ic(idx, file)
        soup = get_content_html(file)
        for ext in extentions:
            result.extend(find_list_ahref_files(soup, ext=ext))
    return result
