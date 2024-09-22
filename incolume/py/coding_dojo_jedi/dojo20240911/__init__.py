"""dojo module."""

from collections import defaultdict
from enum import Enum, auto
from itertools import chain

from unidecode import unidecode


class Chess(Enum):
    """Chess bits."""

    vazio = 0
    peão = 1  # noqa: PLC2401
    bispo = auto()
    cavalo = auto()
    torre = auto()
    dama = auto()
    rei = auto()

    @classmethod
    def _missing_(cls, value):
        for member in cls:
            if (
                unidecode(value).casefold()
                == unidecode(member.name).casefold()
            ):
                return member
            if (value.isdigit() or isinstance(value, int)) and int(
                value,
            ) == member.value:
                return member
        return None


def dojo(tabuleiro: list[list]) -> str:
    """Tabuleiro."""
    result = defaultdict(int)
    for x in chain(*tabuleiro):
        result[Chess(x).name] += 1
    del result[Chess(0).name]
    msg = ''
    for key, value in result.items():
        msg += (
            f'{key.capitalize()}: {value} {"peça" if value < 2 else "peças"}; '  # noqa: PLR2004
        )
    return msg
