import pytest 
from incolume.py.coding_dojo_jedi.dojo20231130.dojo import boyermoore


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
