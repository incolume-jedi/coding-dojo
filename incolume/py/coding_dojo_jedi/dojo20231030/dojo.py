"""Dojo20231030."""
import logging
from typing import Self


class NewPoint:
    """Classe NewPoint."""

    lat: float
    long: float

    def __init__(self: Self, lat: float, long: float) -> None:
        """Init da classe NewPoint."""
        self.lat = lat
        self.long = long


class Point:
    """Classe Point."""

    def __init__(self: Self, latitude: float, longitude: float) -> None:
        """Init da class."""
        self.latitude = latitude
        self.longitude = longitude


def locate(latitude: float, longitude: float) -> Point:
    """Função locate."""
    return Point(latitude, longitude)


if __name__ == '__main__':
    logging.debug(Point.__annotations__)
