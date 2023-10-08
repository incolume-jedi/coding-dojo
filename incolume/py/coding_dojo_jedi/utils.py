"""utils module."""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'  # pragma: no cover

import requests


def check_connectivity(
    url: str = 'https://google.com',
    timeout: float = 1.8,
) -> bool:
    """Check web connectivity."""
    req = requests.get(url, timeout=timeout)
    http_ok: int = 200
    if req.status_code == http_ok:
        return True
    return False
