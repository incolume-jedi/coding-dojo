"""dojo module."""

import dataclasses
import pickle
from pathlib import Path
from typing import Literal, TypeAlias

from bs4 import BeautifulSoup
from icecream import ic

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

Extentions: TypeAlias = Literal['doc', 'docx', 'rtf', 'xls', 'xlsx', 'nsf']


def get_list_html(path_dir: Path | None = None) -> map:
    """Return list HTML files."""
    path_dir = path_dir or directory[0]
    return ic(path_dir.rglob(pattern='**/*.htm*', case_sensitive=False))


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
    ext: Extentions[str] = 'rtf',
) -> list[str, str]:
    """Return a[href]."""
    ext = ext.casefold()
    ext = ext if ext in Extentions else Extentions['rtf']
    result = []
    result.extend(soup.select(f'a[href*={ext}]'))
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
