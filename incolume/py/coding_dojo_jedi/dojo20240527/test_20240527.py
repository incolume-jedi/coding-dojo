"""Module."""

import pytest

from . import gen_4prime, is_prime

__author__ = '@britodfbr'  # pragma: no cover


@pytest.mark.parametrize(
    'entrance expected'.split(),
    [
        (1, False),
        (1065, False),
        (1061, True),
        (9973, True),
    ],
)
def test_not_prime(entrance, expected):
    """Test not prime."""
    assert is_prime(entrance) == expected


def test_prime():
    """Teste para primos de 4 algarismos."""
    expected = 1061
    assert len(list(gen_4prime())) == expected
