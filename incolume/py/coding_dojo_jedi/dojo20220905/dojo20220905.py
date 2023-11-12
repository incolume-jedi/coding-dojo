"""Dojo."""

import logging

from unidecode import unidecode

logging.basicConfig(level=logging.DEBUG)


def stream(st: str) -> float:
    """Valores de streams."""
    streams = {
        'deezer': {
            'family': 34.9,
            'premium': 19.9,
            'hifi': 34.9,
            'student': 9.9,
            'free': 0.0,
        },
        'spotify': {
            'free': 0.0,
            'individual': 19.90,
            'duo': 24.9,
            'familia': 34.9,
            'universitario': 9.9,
        },
        'netflix': {
            'basico': 25.90,
            'padrao': 39.90,
            'premium': 55.90,
        },
        'disney': {
            'disney+': 27.90,
            'combo+': 45.90,
            'starzplay': 55.90,
        },
    }
    logging.debug('st=%s', st)
    pack, combo = unidecode(st).casefold().split()
    logging.debug('pack=%s combo=%s')
    return streams.get(pack, {'err': ''}).get(  # type: ignore[return-value]
        combo,
        'Plano Indisponível',  # type: ignore[arg-type]
    )


if __name__ == '__main__':    # pragma: no cover
    stream('disney combo+')
