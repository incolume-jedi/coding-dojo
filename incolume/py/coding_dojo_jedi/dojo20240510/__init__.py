"""Module."""

# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'  # pragma: no cover


def is_narcisist(num: int) -> bool:
    """Check if number is narcisist number."""
    result = sum(pow(int(n), len(str(num))) for n in str(num) if n.isdigit())
    return num == result
