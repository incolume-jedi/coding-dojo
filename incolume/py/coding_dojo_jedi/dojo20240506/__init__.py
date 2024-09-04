"""Module."""

# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'  # pragma: no cover


def is_feliz(num: int) -> bool:
    """Verifica se número é feliz."""
    nums = [pow(int(n), 2) for n in str(num)]
    if (snum := sum(nums)) == 1:
        return True
    try:
        return is_feliz(snum)
    except RecursionError:
        return False
