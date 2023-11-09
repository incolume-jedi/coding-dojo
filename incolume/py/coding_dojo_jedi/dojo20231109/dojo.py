import re
from urllib.parse import urlencode, urlsplit, urljoin


def remove_url_anchor0(url: str) -> str:
    """Remover anchor da url."""
    return url.split('#')[0]


def remove_url_anchor1(url: str) -> str:
    """Remover anchor da url."""
    try:
        return url[:url.index('#')]
    except ValueError:
        return url


def remove_url_anchor2(url: str) -> str:
    """Remover anchor da url."""
    # regex = r'((ht|f)tp[s]?://)?\w+'
    regex = r'((ht|f)tp[s]?://)?[\w\.\/\?\-\=]+'
    return re.search(regex, url, flags=re.I).group(0)


def remove_url_anchor3(url: str) -> str:
    """Remover anchor da url."""
    regex = r'^(.+)#'
    try:
        return re.search(regex, url, flags=re.I).group(1)
    except AttributeError:
        return url


def remove_url_anchor(url: str) -> str:
    """Remover anchor da url."""
    
    # return urlencode(url)
    return urlsplit(url)
    