from unidecode import unidecode
import logging


logging.basicConfig(level=logging.DEBUG)


def stream(st: str) -> float:
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
    logging.debug(f'{st=}')
    pack, combo = unidecode(st).casefold().split()
    logging.debug(f'{pack=} {combo=}')
    return streams.get(pack, {'err': 'Ops..'}).get(combo, 'err')


if __name__ == '__main__':    # pragma: no cover
    stream('disney combo+')
