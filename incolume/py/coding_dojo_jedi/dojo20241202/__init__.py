"""dojo module."""

import dataclasses
import pickle
from pathlib import Path

from bs4 import BeautifulSoup
from icecream import ic

directory: list[Path] = [
    Path('z:', 'acervo-legis'),
    Path(
        'castelo',
        'saj',
        'CENTRO DE ESTUDOS',
        'EQUIPE CEJ',
        'BRITO',
        'projetos',
        'acervo-legis',
    ),
]


def get_list_html(path_dir: Path | None = None) -> map:
    """Return list HTML files."""
    path_dir = path_dir or directory[0]
    return path_dir.rglob(pattern='*.htm?', case_sensitive=False)


def get_content_html(filename: Path) -> BeautifulSoup:
    """Return HTML content."""
    with filename.open('rb') as f:
        return BeautifulSoup(f.read(), 'html5lib')


def find_list_ahref(soup: BeautifulSoup) -> list[str, str]:
    """Return a[href]."""
    return soup.select('a[href]')


def find_list_ahref_files(soup: BeautifulSoup) -> list[str, str]:
    """Return a[href]."""
    ext = ['doc', 'docx', 'rtf', 'xls', 'xlsx']

    return soup.select('a[href="docx"]')


@dataclasses.dataclass
class Item:
    """Item."""

    file: Path
    items: list[str]


def dojo() -> list[Item]:
    """Dojo solution."""
    result: list[Item] = []
    for idx, file in enumerate(get_list_html()):
        if idx % 10**5:
            with Path(f'result{idx:0>5}.pkl').open('wb') as f:
                pickle.dump(result, f)
                ic(f.name)
            result.clear()
        soup = get_content_html(file)
        res = soup.select('a[href]')
        result.append(Item(file, res))
        ic(result[-1])
    return result
