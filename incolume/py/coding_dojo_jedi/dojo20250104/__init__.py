"""dojo module."""

import inspect
import tarfile
from pathlib import Path
from typing import Final

import httpx
from icecream import ic

URL_TAR_FILE: Final[str] = 'https://osprogramadores.com/files/d11/pi-1M.tar.gz'
URL_RAW_FILE: Final[str] = 'https://pastebin.com/raw/Ak8TCbJk'


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


def handler_file(fin: Path | None = None, chunk: int = 0) -> bytes:
    """Handler file."""
    ic(inspect.stack()[0][3])
    chunk = (
        -1 if (not isinstance(chunk, int) or chunk < 0) else max(chunk, 100)
    )

    fin = fin or Path(*__package__.split('.')) / 'pi-1M.tgz'
    ic(fin)
    with tarfile.open(fin, mode='r:gz') as handler:
        file = handler.extractfile(handler.getnames()[0])
        if chunk == -1:
            return file.readline()
        return file.read(chunk)


def handler_stream(url: str = '', chunk: int = 0) -> bytes:
    """Handler stream."""
    ic(inspect.stack()[0][3])
    chunk = (
        -1 if (not isinstance(chunk, int) or chunk < 0) else max(chunk, 100)
    )

    url = url or URL_RAW_FILE
    response = httpx.get(url)
    content = response.content
    if chunk == -1:
        return content
    return content[:chunk]


def dojo(**kwargs: str) -> dict[str]:
    """Dojo solution."""
    ic(inspect.stack()[0][3], kwargs)
    return kwargs
