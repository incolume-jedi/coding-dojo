"""Test dojo20231129."""
import pytest
from incolume.py.coding_dojo_jedi.dojo20231129.dojo import landPermetercal

@pytest.mark.parametrize(
    'entrance expected'.split(),
    [
        (
            [
                'XOOXO',
                'XOOXO',
                'OOOXO',
                'XXOXO',
                'OXOOO',
            ],
            24,
        ),
        (
            [
                'XOOO',
                'XOXO',
                'XOXO',
                'OOXX',
                'OOOO',
            ],
            18,
        ),
    ],
)
def test_perimetro_terrestre(entrance, expected) -> None:
    """Test it."""
    assert landPermetercal(entrance) == expected