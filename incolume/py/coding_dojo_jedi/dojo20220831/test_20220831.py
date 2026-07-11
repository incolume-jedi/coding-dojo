"""Unittest for dojo."""

import pytest

from incolume.py.coding_dojo_jedi.dojo20220831.dojo20220831 import (
    conceito,
    conceito0,
    conceito1,
)

test_values = [
    ((10, 10), 'Média 10.0, "A", APROVADO'),
    ((1, 1), 'Média 1.0, "E", REPROVADO'),
    ((10, 5), 'Média 7.5, "B", APROVADO'),
    ((9, 5), 'Média 7.0, "C", APROVADO'),
    ((6, 4), 'Média 5.0, "D", REPROVADO'),
]


@pytest.mark.parametrize(
    ['entrance', 'expected'],
    test_values,
)
def test_conceito(entrance, expected) -> None:
    """Teste conceito."""
    assert conceito(*entrance) == expected


@pytest.mark.parametrize(
    ['entrance', 'expected'],
    test_values,
)
def test_conceito0(entrance, expected) -> None:
    """Teste conceito."""
    assert conceito0(*entrance) == expected


@pytest.mark.skip
@pytest.mark.parametrize(
    ['entrance', 'expected'],
    test_values,
)
def test_conceito1(entrance, expected) -> None:
    """Teste conceito."""
    assert conceito1(*entrance) == expected
