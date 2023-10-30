"""Dojo20231030."""

from typing import Self


class NewPoint:
    """Classe NewPoint."""
    lat: float
    long: float
    def __init__(self, lat: float, long: float) -> None:
        self.lat = lat
        self.long = long


class Point:
    """Classe Point."""
    def __init__(self, latitude: float, longitude: float) -> Self:
        # self.__annotations__['latitude'] = float
        # self.__annotations__['longitude'] = float
        self.latitude = latitude
        self.longitude = longitude


def locate(latitude: float, longitude: float) -> Point:
    """Função locate."""
    return Point(latitude, longitude)


if __name__ == '__main__':
    print(Point.__annotations__)
