"""Test Get Planet Name By ID"""
import pytest
from incolume.py.coding_dojo_jedi.dojo20231127.dojo import get_planet_name0, get_planet_name, boyermoore


@pytest.mark.parametrize(
    'entrance expected'.split(),
    [
        (2, 'Venus'),
        (5, 'Jupiter'),
        (3, 'Earth'),
        (4, 'Mars'),
        (8, 'Neptune'),
        (1, 'Mercury'),
    ]
)
def test_get_planet_name0(entrance, expected) -> None:
    """Test it."""
    assert get_planet_name0(entrance) == expected


@pytest.mark.parametrize(
    'entrance expected'.split(),
    [
        (2, 'Venus'),
        (5, 'Jupiter'),
        (3, 'Earth'),
        (4, 'Mars'),
        (8, 'Neptune'),
        (1, 'Mercury'),
    ]
)
def test_get_planet_name(entrance, expected) -> None:
    """Test it."""
    assert get_planet_name(entrance) == expected



@pytest.mark.parametrize(
    'entrance expected'.split(),
    [
        (('algoritmo', 'Os algoritmos de ordenação, são algoritmos eficazes.'), {'algoritmo': [3,20]}),
        (('THIS', "THIS IS A TEST TEXT"), {'THIS': 0}),
        (("AABA", 'AABAACAADAABAABA'), {'AABA': [0, 9,12]}),
        (("1234", '012342798123468791251234'), {'1234': [1, 10, 21]}),
    ],
)
def test_boyermoore(entrance, expected) -> None:
    """Test boyer moore."""
    assert boyermoore(*entrance) == expected