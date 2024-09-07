"""dojo module."""

import logging
import re
from enum import Enum, auto
from typing import ClassVar

ALPHABET = (
    'abcdefghijklmnopqrstuvwyzàáãâéêóôõíúç'
    'ABCDEFGHIJKLMNOPQRSTUVWYZÀÁÃÂÉÊÓÔÕÍÚÇ'
)


class Mode(Enum):
    """Class mode."""

    DECRYPT = 0
    ENCRYPT = auto()

    @classmethod
    def _missing_(cls, value):
        """On missing."""
        logging.debug('%s', value)
        return cls.ENCRYPT


class Caesar:
    """Cesar cypher."""

    simbols: ClassVar = {
        ' ': 'WBRW',
        ',': 'WVRW',
        '.': 'WPTW',
        ';': 'WPVW',
        ':': 'WDPW',
        '!': 'WEXW',
        '?': 'WINW',
        '-': 'WHFW',
    }

    def __init__(
        self,
        key: int = 0,
        alphabet: str = '',
    ) -> None:
        """Init class."""
        try:
            self.key: int = int(key) or 23
            self.alphabet = alphabet or ALPHABET
        except (TypeError, ValueError):
            self.key = 23

    def prepara_frase(self, frase: str) -> str:
        """Prepara frase."""
        result = [frase]
        if any(x in frase for x in self.simbols.values()):
            for simbol, cod in self.simbols.items():
                result.append(re.sub(cod, simbol, result[-1]))
            return result[-1]
        return ''.join(self.simbols.get(x, x) for x in frase)

    def apply(self, data: str, mode: Mode = Mode.ENCRYPT) -> str:
        """Apply cesar."""
        new_data = ''
        for c in self.prepara_frase(data):
            index = self.alphabet.find(c)
            if index == -1:
                new_data += c
            else:
                new_index = (
                    index + self.key
                    if mode == Mode.ENCRYPT
                    else index - self.key
                )
                new_index = new_index % len(self.alphabet)
                new_data += self.alphabet[new_index : new_index + 1]
        return self.prepara_frase(new_data)
