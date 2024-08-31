"""Test for dojo."""

import pytest

from incolume.py.coding_dojo_jedi.dojo20220808.dojo20220808 import is_par
from tests import Py310


@Py310
@pytest.mark.parametrize(
    ['entrance', 'expected'],
    [
        (5, 'Ímpar'),
        (56, 'Par'),
        (567, 'Ímpar'),
        (568, 'Par'),
        (13, 'Ímpar'),
        (17, 'Ímpar'),
        (0, 'Par'),
        (-34, 'Par'),
        (-13, 'Ímpar'),
    ],
)
def test_is_par(entrance, expected) -> None:
    """Test is_par."""
    assert is_par(entrance) == expected


@Py310
@pytest.mark.parametrize(
    ['entrance', 'exception', 'msg'],
    [
        (None, ValueError, 'Valor inválido.'),
        ('a', TypeError, 'Somente números inteiros.'),
        ((3 + 0j), TypeError, 'Somente números inteiros.'),
        (3.141592, TypeError, 'Somente números inteiros.'),
    ],
)
def test_is_par_except(entrance, exception, msg) -> None:
    """Test exceptions is_par."""
    with pytest.raises(exception, match=msg):
        assert is_par(entrance)
