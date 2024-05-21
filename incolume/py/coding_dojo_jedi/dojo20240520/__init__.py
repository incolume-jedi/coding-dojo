"""Dojo module."""


def rot13a(texto: str) -> str:
    """Rot13."""
    d = {}
    for c in (65, 97):
        for i in range(26):
            d[chr(i + c)] = chr((i + 13) % 26 + c)

    return ''.join([d.get(c, c) for c in texto])


def rot13(texto: str) -> str:
    """Rot13."""
    encode = str.maketrans(
        'ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz',
        'NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm',
    )
    return texto.translate(encode)
