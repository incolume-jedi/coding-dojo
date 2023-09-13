from dojo import tabuada
import pytest


@pytest.mark.parametrize(
    "entrance expected".split(),
    (
        (
            (10),
            [
                "10 X 1 = 10",
                "10 X 2 = 20",
                "10 X 3 = 30",
                "10 X 4 = 40",
                "10 X 5 = 50",
                "10 X 6 = 60",
                "10 X 7 = 70",
                "10 X 8 = 80",
                "10 X 9 = 90",
                "10 X 10 = 100",
            ],
        ),
        ((5, 4, 7), ["5 X 4 = 20", "5 X 5 = 25", "5 X 6 = 30", "5 X 7 = 35"]),
        ((5, 7, 4), ["5 X 4 = 20", "5 X 5 = 25", "5 X 6 = 30", "5 X 7 = 35"]),
        (
            (10, 6, 3),
            [
                "10 X 3 = 30",
                "10 X 4 = 40",
                "10 X 5 = 50",
                "10 X 6 = 60",
            ],
        ),
        (
            (10, 3, 6),
            [
                "10 X 3 = 30",
                "10 X 4 = 40",
                "10 X 5 = 50",
                "10 X 6 = 60",
            ],
        ),
        (
            (10, 10, 7),
            [
                "10 X 7 = 70",
                "10 X 8 = 80",
                "10 X 9 = 90",
                "10 X 10 = 100",
            ],
        ),
        (
            (10, 7, 10),
            [
                "10 X 7 = 70",
                "10 X 8 = 80",
                "10 X 9 = 90",
                "10 X 10 = 100",
            ],
        ),
        (
            {'tabuada': 10, 'inicial': 10, 'final': 7},
            [
                "10 X 7 = 70",
                "10 X 8 = 80",
                "10 X 9 = 90",
                "10 X 10 = 100",
            ],
        ),
        (
            {'tabuada': 10, 'inicial': 7, 'final': 10},
            [
                "10 X 7 = 70",
                "10 X 8 = 80",
                "10 X 9 = 90",
                "10 X 10 = 100",
            ],
        ),
    ),
)
def test_tabuada(entrance, expected):
    if isinstance(entrance, dict):
        assert tabuada(**entrance) == expected
    if isinstance(entrance, tuple):
        assert tabuada(*entrance) == expected
