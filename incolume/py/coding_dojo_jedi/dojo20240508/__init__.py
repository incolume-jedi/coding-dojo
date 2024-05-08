"""Module."""

# !/usr/bin/env python
# -*- coding: utf-8 -*-
from itertools import count

from incolume.py.coding_dojo_jedi.dojo20240507 import is_feliz

__author__ = '@britodfbr'  # pragma: no cover


def double_minor_feliz():
    """Felizes consecutivos."""
    num = count(1)
    while True:
        n = next(num)
        if is_feliz(n) and is_feliz(n + 1):
            return n, n + 1


def trio_minor_feliz():
    """Felizes consecutivos."""
    num = count(1)
    while True:
        n = next(num)
        if is_feliz(n) and is_feliz(n + 1) and is_feliz(n + 2):
            return n, n + 1, n + 2
