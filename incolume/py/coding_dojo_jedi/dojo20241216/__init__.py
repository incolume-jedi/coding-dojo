"""dojo module."""

from pathlib import Path

import httpx

url: str = (
    'https://www.python.org/static/community_logos/python-powered-h-50x65.png'
)


def download_file(link: str = '') -> Path:
    """Donwnload files."""
    ans = httpx.get(link, follow_redirects=True)
    return ans.status_code


def dojo(*args: str, **kwargs: str) -> dict[str]:
    """Dojo solution."""
    kwargs['args'] = args
    return kwargs
