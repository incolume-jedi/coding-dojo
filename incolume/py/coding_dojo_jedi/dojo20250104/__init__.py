"""dojo module."""

import inspect

import httpx
from icecream import ic

URL: str = 'https://osprogramadores.com/files/d11/pi-1M.tar.gz'


def download_file(url: str = '') -> bool:
    """Download file."""
    url = url or URL
    response = httpx.get(url)
    filename = url.split('/')[-1]
    return filename


def handler_file(fin, chunk: int) -> bool:
    """Handler file."""


def dojo(**kwargs: str) -> dict[str]:
    """Dojo solution."""
    ic(inspect.stack()[0][3], kwargs)
    return kwargs
