"""Module."""

# !/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from collections import Counter, defaultdict

from icecream import ic

__author__ = '@britodfbr'  # pragma: no cover

ic.disable()
if os.getenv('DEBUG_MODE'):
    ic.enable()


def max_letter0(frase: str) -> str:
    """Return max letter counted."""
    dic = defaultdict(int)
    for letter in frase:
        dic[letter] += 1
    dic[' '] = -1
    return sorted(dic.items(), key=lambda d: d[1])[-1][0]


def max_letter1(frase: str) -> str:
    """Return max letter counted."""
    dic = defaultdict(int)
    for letter in frase:
        dic[letter] += 1
    dic[' '] = -1
    return max(dic.items(), key=lambda k: k[1])[0]


def max_letter2(frase: str) -> str:
    """Return max letter counted."""
    counter = Counter(frase)
    counter[' '] = -1
    return ic(counter.most_common(1))[0][0]


def max_letter(frase: str) -> list[str]:
    """Return max letter counted."""
    result = defaultdict(list)

    for letter in frase:
        if (
            letter != ' '
            and letter not in result[(let := frase.count(letter))]
        ):
            result[let].append(letter)

    return max(result.items())[1]
