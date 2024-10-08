"""dojo module."""

import logging
import re
import string
from enum import Enum, auto
from typing import Final

alphabet = (
    'abcdefghijklmnopqrstuvwyzàáãâéêóôõíúç'
    'ABCDEFGHIJKLMNOPQRSTUVWYZÀÁÃÂÉÊÓÔÕÍÚÇ'
)
MODE_ENCRYPT = 1
MODE_DECRYPT = 0
KEY: Final[int] = 23
SIMBOLS = {
    ' ': 'WBRW',
    ',': 'WVRW',
    '.': 'WPTW',
    ';': 'WPVW',
    ':': 'WDPW',
    '!': 'WEXW',
    '?': 'WINW',
    '-': 'WHFW',
}


class Mode(Enum):
    """Class mode."""

    DECRYPT = 0
    ENCRYPT = auto()

    @classmethod
    def _missing_(cls, value):
        """On missing."""
        logging.debug('%s', value)
        return cls.ENCRYPT


def prepara_frase(frase: str) -> str:
    """Prepara frase."""
    result = [frase]
    if any(x in frase for x in SIMBOLS.values()):
        for simbol, cod in SIMBOLS.items():
            result.append(re.sub(cod, simbol, result[-1]))
        return result[-1]
    return ''.join(SIMBOLS.get(x, x) for x in frase)


def caesar(data: str, key: int, mode: int) -> str:
    """Cifra de caesar.

    Disponível em https://gist.githubusercontent.com/ustropo/4aead578401fe57166a9ce1d45375696/raw/b81dd00c74ccaecd252678ea1353c7ef402a6866/caesar_cypher.py
    """
    alphabet = (
        'abcdefghijklmnopqrstuvwyzàáãâéêóôõíúç'
        'ABCDEFGHIJKLMNOPQRSTUVWYZÀÁÃÂÉÊÓÔÕÍÚÇ'
    )
    new_data = ''
    for c in prepara_frase(data):
        index = alphabet.find(c)
        if index == -1:
            new_data += c
        else:
            new_index = index + key if mode == MODE_ENCRYPT else index - key
            new_index = new_index % len(alphabet)
            new_data += alphabet[new_index : new_index + 1]
    return prepara_frase(new_data)


def cesar(data: str, key: int, *, decrypt_mode: bool = False) -> str:
    """Cifra de caesar."""
    key = key or KEY
    new_data = ''
    for c in prepara_frase(data):
        index = alphabet.find(c)
        if index == -1:
            new_data += c
        else:
            new_index = index + key if decrypt_mode else index - key
            new_index = new_index % len(alphabet)
            new_data += alphabet[new_index : new_index + 1]
    return new_data


def cypher_cesar(
    data: str,
    key: int = KEY,
    *,
    decrypt_mode: bool = False,
    alphabet: str = '',
) -> str:
    """Cifra de caesar."""
    alphabet = alphabet or string.ascii_letters
    new_data = ''
    for c in prepara_frase(data):
        index = alphabet.find(c)
        if index == -1:
            new_data += c
        else:
            new_index = index + key if decrypt_mode else index - key
            new_index = new_index % len(alphabet)
            new_data += alphabet[new_index : new_index + 1]
    return prepara_frase(new_data)
