"""Test module."""

import pytest
from . import rot13, rot13a, rot13b


testes = [
    ('EBG13 rknzcyr.', 'ROT13 example.'),
    (
        'This is my first ROT13 excercise!',
        'Guvf vf zl svefg EBG13 rkprepvfr!',
    ),
    (
        "Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE thl'f fubrf.",
        "In the elevators, the extrovert looks at the OTHER guy's shoes.",
    ),
    (
        'Tudo é difícil, até fácil se tornar.',
        'Ghqb é qvsípvy, ngé sápvy fr gbeane.',
    ),
    ('Znl gur sbepr or jvgu lbh', 'May the force be with you'),
]


@pytest.mark.parametrize(
    'entrance expected'.split(),
    testes,
)
def test_rot13a(entrance, expected):
    """Test."""
    assert rot13a(entrance) == expected


@pytest.mark.parametrize(
    'entrance expected'.split(),
    testes,
)
def test_rot13b(entrance, expected):
    """Test."""
    assert rot13b(entrance) == expected


@pytest.mark.parametrize(
    'entrance expected'.split(),
    testes,
)
def test_rot13(entrance, expected):
    """Test."""
    assert rot13(entrance) == expected
