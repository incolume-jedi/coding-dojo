"""Testing dojo."""

import pytest

from incolume.py.coding_dojo_jedi.dojo20220910.dojo20220910 import (
    weekday,
    weekday0,
    weekday1,
)
from tests.conftest import py310


@pytest.mark.parametrize(
    'entrance expected'.split(),
    [
        (1, 'Domingo'),
        (2, 'Segunda'),
        (3, 'Terça'),
        (4, 'Quarta'),
        (5, 'Quinta'),
        (6, 'Sexta'),
        (7, 'Sábado'),
        (8, 'Valor inválido'),
        (9, 'Valor inválido'),
        (0, 'Valor inválido'),
    ],
)
def test_weekday0(entrance, expected) -> None:
    """Unittest for this function."""
    assert weekday0(entrance) == expected


@pytest.mark.parametrize(
    'entrance expected'.split(),
    [
        (1, 'Domingo'),
        (2, 'Segunda'),
        (3, 'Terça'),
        (4, 'Quarta'),
        (5, 'Quinta'),
        (6, 'Sexta'),
        (7, 'Sábado'),
        (8, 'Valor inválido'),
        (9, 'Valor inválido'),
        (0, 'Valor inválido'),
    ],
)
def test_weekday1(entrance, expected) -> None:
    """Unittest for weekday1."""
    assert weekday1(entrance) == expected


@py310
@pytest.mark.parametrize(
    'entrance expected'.split(),
    [
        (1, 'Domingo'),
        (2, 'Segunda'),
        (3, 'Terça'),
        (4, 'Quarta'),
        (5, 'Quinta'),
        (6, 'Sexta'),
        (7, 'Sábado'),
        (8, 'Valor inválido'),
        (9, 'Valor inválido'),
        (0, 'Valor inválido'),
    ],
)
def test_weekday(entrance, expected) -> None:
    """Unittest for weekday."""
    assert weekday(entrance) == expected
