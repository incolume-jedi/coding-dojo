"""Unittest for dojo."""

import pytest

from incolume.py.coding_dojo_jedi.dojo20220831.dojo20220831 import conceito


@pytest.mark.parametrize(
    'entrance expected'.split(),
    [
        ((10, 10), 'Média 10.0, "A", APROVADO'),
        ((1, 1), 'Média 1.0, "E", REPROVADO'),
        ((10, 5), 'Média 7.5, "B", APROVADO'),
        ((9, 5), 'Média 7.0, "C", APROVADO'),
        ((6, 4), 'Média 5.0, "D", REPROVADO'),
    ],
)
def test_conceito(entrance, expected) -> None:
    """Teste conceito."""
    assert conceito(*entrance) == expected
