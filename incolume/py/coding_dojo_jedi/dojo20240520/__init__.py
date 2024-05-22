"""Dojo module."""

from codecs import encode
from functools import partial


def rot13a(texto: str) -> str:
    """Rot13."""
    d = {}
    for c in (65, 97):
        for i in range(26):
            d[chr(i + c)] = chr((i + 13) % 26 + c)

    return ''.join([d.get(c, c) for c in texto])


def rot13b(texto: str) -> str:
    """Rot13."""
    encode = str.maketrans(
        'ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz',
        'NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm',
    )
    return texto.translate(encode)


rot13c = partial(encode, encoding='rot_13')


def rot13(texto: str) -> str:
    """Rot13."""
    encode = {
        (i + c): ((i + 13) % 26 + c) for i in range(26) for c in (65, 97)
    }
    return texto.translate(encode)
