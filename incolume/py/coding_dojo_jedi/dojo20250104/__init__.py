"""dojo module."""

import inspect
import tarfile
from collections.abc import Iterator
from functools import lru_cache
from pathlib import Path
from typing import Final

import filetype
import httpx
from icecream import ic

URL_TAR_FILE: Final[str] = 'https://osprogramadores.com/files/d11/pi-1M.tar.gz'
URL_RAW_FILE: Final[str] = 'https://pastebin.com/raw/Ak8TCbJk'
LOCAL_FILE: Path = Path(*__package__.split('.')) / 'pi-1M.tgz'


def download_file(
    url: str = '',
    dir_output: Path | None = None,
    fout: Path | None = None,
) -> Path:
    """Download file."""
    ic(inspect.stack()[0][3])
    dir_output = dir_output or Path()
    url = url or URL_TAR_FILE
    ic(url)
    response = httpx.get(url)
    filename = fout or dir_output / url.split('/')[-1]
    ic(filename)
    filename.parent.mkdir(exist_ok=True)
    filename.write_bytes(response.content)
    return filename


def handler_file(*, fin: Path | None = None, chunk: int = 0) -> bytes:
    """Handler file."""
    ic(inspect.stack()[0][3])
    chunk = (
        -1 if (not isinstance(chunk, int) or chunk < 0) else max(chunk + 2, 22)
    )

    fin = fin or LOCAL_FILE
    ic(fin)
    with tarfile.open(fin, mode='r:gz') as handler:
        file = handler.extractfile(handler.getnames()[0])
        if chunk == -1:
            return file.readline()
        return file.read(chunk)


def handler_stream(*, url: str = '', chunk: int = 0) -> bytes:
    """Handler stream."""
    ic(inspect.stack()[0][3])
    chunk = (
        -1 if (not isinstance(chunk, int) or chunk < 0) else max(chunk + 2, 22)
    )

    url = url or URL_RAW_FILE
    response = httpx.get(url)
    content = response.content
    if chunk == -1:
        return content
    return content[:chunk]


def iterator_handler_file(*, fin: Path | None = None) -> Iterator[bytes]:
    """Iterator of bytes."""
    fin = fin or LOCAL_FILE
    kind = filetype.guess(fin)
    ic(fin)
    try:
        if kind.mime == 'application/gzip':
            with tarfile.open(fin, mode='r:gz') as handler:
                file = handler.extractfile(handler.getnames()[0])
                file.read(2)
                while char := file.read(1):
                    yield char
    except AttributeError:
        ...

    with fin.open('rb') as file:
        file.read(2)
        while char := file.read(1):
            yield char


@lru_cache
def is_prime(num: int) -> bool:
    """Check if prime number."""
    if not isinstance(num, int) or num <= 1 or (num > 2 and num % 2 == 0):  # noqa: PLR2004
        return False
    return all(num % n != 0 for n in range(2, num // 2 + 1))


def dojo(**kwargs: str) -> dict[str]:
    """Dojo solution."""
    result = {}
    ic(inspect.stack()[0][3], kwargs)
    sequence = handler_file().split(b'.')[-1]
    result = {}
    # for num in sequence:
    #     result

    return result
