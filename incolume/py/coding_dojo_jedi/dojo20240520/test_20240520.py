"""Test module."""

import pytest
from . import rot13


@pytest.mark.parametrize(
    'entrance expected'.split(),
    [
        ('EBG13 rknzcyr.', 'ROT13 example.'),
        (
            'This is my first ROT13 excercise!',
            'Guvf vf zl svefg EBG13 rkprepvfr!',
        ),
        (
            "Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE thl'f fubrf.",
            "In the elevators, the extrovert looks at the OTHER guy's shoes.",
        ),
    ],
)
def test_rot13(entrance, expected):
    """Test."""
    assert rot13(entrance) == expected
