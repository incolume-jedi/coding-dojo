"""dojo module."""

import inspect
import tarfile
from pathlib import Path

import httpx
from icecream import ic

URL: str = 'https://osprogramadores.com/files/d11/pi-1M.tar.gz'


def download_file(url: str = '', dir_output: Path | None = None) -> Path:
    """Download file."""
    ic(inspect.stack()[0][3])
    dir_output = dir_output or Path()
    url = url or URL
    ic(url)
    response = httpx.get(url)
    filename = dir_output / url.split('/')[-1]
    ic(filename)
    filename.parent.mkdir(exist_ok=True)
    filename.write_bytes(response.content)
    return filename


def handler_file(fin: Path | None = None, chunk: int = 0) -> bool:
    """Handler file."""
    ic(inspect.stack()[0][3])
    chunk = -1 if chunk < 0 else max(chunk, 100)
    fin = fin or Path() / 'pi-1M.tar.gz'
    with tarfile.open(fin, mode='r:gz') as handler:
        file = handler.extractfile(handler.getnames()[0])
        if chunk == -1:
            return file.readline()
        return file.read(chunk)


def dojo(**kwargs: str) -> dict[str]:
    """Dojo solution."""
    ic(inspect.stack()[0][3], kwargs)
    return kwargs
