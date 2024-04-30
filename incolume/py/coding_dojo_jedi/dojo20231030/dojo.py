"""Dojo20231030."""

import logging


class NewPoint:
    """Classe NewPoint."""

    lat: float
    long: float

    def __init__(self: 'NewPoint', lat: float, long: float) -> None:
        """Init da classe NewPoint."""
        self.lat = lat
        self.long = long


class Point:
    """Classe Point."""

    def __init__(self: 'Point', latitude: float, longitude: float) -> None:
        """Init da class."""
        self.latitude = latitude
        self.longitude = longitude


def locate(latitude: float, longitude: float) -> Point:
    """Função locate."""
    return Point(latitude, longitude)


def int_reverso(inteiro: int) -> int:
    """Reverso de inteiro."""
    base = 10
    result = 0
    cdu: list = []
    sinal = 1 if inteiro > 0 else -1
    inteiro = abs(inteiro)

    while inteiro > 0:
        cdu.insert(0, inteiro % base)
        inteiro //= base

    for i, num in enumerate(cdu):
        result += num * 10**i
    return result * sinal


if __name__ == '__main__':
    logging.debug(Point.__annotations__)
    logging.debug(int_reverso(12345))
