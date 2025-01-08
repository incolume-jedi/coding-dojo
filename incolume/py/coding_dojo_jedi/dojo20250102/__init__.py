"""dojo module."""

import copy
import dataclasses
import inspect
import json
import logging
import pickle
import sys
from pathlib import Path
from typing import Any

from bs4 import BeautifulSoup, Tag
from icecream import ic
from tqdm import tqdm

if sys.version_info >= (3, 11):
    from typing import Literal, TypeAlias, get_args
else:
    from typing_extensions import Literal, TypeAlias, get_args  # noqa: UP035


msg = sys.platform.casefold()
logging.info(ic(msg))

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
CHUNK_MIN: int = 10


def get_list_html(path_dir: Path | None = None) -> map:
    """Return list HTML files."""
    path_dir = path_dir or directory[0]
    result = path_dir.rglob(pattern='**/*.htm*', case_sensitive=False)
    logging.info(ic(result))
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
) -> list[Tag]:
    """Return a[href]."""
    try:
        ext = ext if ext.casefold() in get_args(Extentions) else on_raise
    except AttributeError:
        ext = on_raise
    logging.debug(ic(inspect.stack()[0][3], ext))
    result = []
    result.extend(soup.select(f'a[href*=".{ext}" i]'))
    logging.debug(ic(result))
    return result


@dataclasses.dataclass
class Item:
    """Item."""

    file: Path
    items: list[str]

    def to_dict(self) -> str:
        """Serializer self for JSON."""
        obj = copy.copy(self)
        obj.file = self.file.as_posix()
        obj.items = [str(x) for x in self.items]
        logging.debug(ic(self.__class__, inspect.stack()[0][3], obj))
        return obj.__dict__


def dojo0(*, chunk: int = 0, **kwargs: dict[str:Path]) -> list[Item]:
    """Dojo solution."""
    chunk = max(chunk, CHUNK_MIN)
    result: list[Item] = []
    for idx, file in enumerate(get_list_html(kwargs.get('path_dir')), 1):
        if not idx % chunk:
            f = Path(f'result{idx:0>5}.pkl')
            pickle.dump(result, f.open('wb'))
            logging.info(ic(f.name))
        soup = get_content_html(file)
        res = soup.select('a[href]')
        result.append(Item(file, res))
        logging.debug(ic(idx, result[-1]))
    return result


def dojo(**kwargs: dict[str:Any]) -> Path:
    """Dojo solution.

    Args:
        kwargs (dict[str:Any]): can be any these:
          extentions (list[str]): list of extentions for query.
          count (int): countity for query, default 5k.
          fout (Path): Filename output for result

    Returns:
        Path: with result.
        list[Item]: With result.

    Raises:
        MemoryError: occurs when the code requires more
            memory than is available in the system's RAM.
    """
    logging.debug(ic(inspect.stack()[0][3]))
    result: list[Item] = []
    seq = 0
    extentions = kwargs.get('extentions', get_args(Extentions))
    logging.info(ic(extentions))
    count = kwargs.get('count', CHUNK_MIN)
    logging.info(ic(count))
    fout = kwargs.get('fout', Path('result.json')).with_suffix('.json')
    logging.info(ic(fout))

    for idx, file in tqdm(enumerate(get_list_html(kwargs.get('path_dir')), 1)):
        logging.info(ic(idx, file))
        soup = get_content_html(file)
        for ext in extentions:
            result.extend(find_list_ahref_files(soup, ext=ext))
        if seq == count:
            logging.debug(ic(result))
            with fout.open('a') as json_handler:
                json.dump(
                    [obj.to_dict() for obj in result],
                    fp=json_handler,
                    indent=2,
                )
            seq = -1
            result.clear()
        seq += 1
    return fout
