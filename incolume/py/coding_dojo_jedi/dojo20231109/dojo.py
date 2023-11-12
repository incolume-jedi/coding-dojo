"""Remover anchor."""

import re
from urllib.parse import urlparse, urlunparse


def remove_url_anchor0(url: str) -> str:
    """Remove anchor da url."""
    return url.split('#')[0]


def remove_url_anchor1(url: str) -> str:
    """Remove anchor da url."""
    try:
        return url[: url.index('#')]
    except ValueError:
        return url


def remove_url_anchor2(url: str) -> str:
    """Remove anchor da url."""
    regex = r'((ht|f)tp[s]?://)?[\w\.\/\?\-\=]+'
    result = re.search(regex, url, flags=re.I)
    return result.group(0)  # type: ignore[union-attr]


def remove_url_anchor3(url: str) -> str:
    """Remove anchor da url."""
    regex = r'^(.+)#'
    result = re.search(regex, url, flags=re.I)
    try:
        return result.group(1)  # type: ignore[union-attr]
    except AttributeError:
        return url


def remove_url_anchor(url: str) -> str:
    """Remove anchor da url."""
    result = urlparse(url)._asdict()
    result.update({'fragment': ''})
    return urlunparse(tuple(result.values()))
