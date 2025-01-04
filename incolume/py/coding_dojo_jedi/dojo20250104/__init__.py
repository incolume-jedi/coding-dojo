"""dojo module."""

import inspect
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


def handler_file(fin, chunk: int) -> bool:
    """Handler file."""


def dojo(**kwargs: str) -> dict[str]:
    """Dojo solution."""
    ic(inspect.stack()[0][3], kwargs)
    return kwargs
