"""Teste dojo contagem de nucleotídeos."""

import sys

import pytest

from incolume.py.coding_dojo_jedi.dojo20231019.dojo20231019 import (
    complemento_fita_dna,
    contador_nucleotideos,
)


@pytest.mark.skipif(
    sys.version_info < (3, 10),
    reason='requires python3.10 or higher',
)
@pytest.mark.parametrize(
    ['entrance', 'expected'],
    [
        ('ATCG', '1 1 1 1'),
        ('ATATGGCC', '2 2 2 2'),
        ('ATGCTTCAGAAAGGTCTTACG', '6 4 5 6'),
        (
            'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCT'
            'CTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC',
            '20 12 16 20',
        ),
        ('AAAAACCCCGGGTT', '5 4 3 2'),
    ],
)
def test_contador_nucleotideos(entrance, expected) -> None:
    """Testar a função contador_nucleotideos."""
    assert contador_nucleotideos(entrance) == expected


@pytest.mark.skipif(
    sys.version_info < (3, 10),
    reason='requires python3.10 or higher',
)
@pytest.mark.parametrize(
    ['entrance', 'expected'],
    [
        ('AAAACCCGGT', 'ACCGGGTTTT'),
    ],
)
def test_complemento_fita_dna(entrance, expected) -> None:
    """Testar a função complemento_fita_dna."""
    assert complemento_fita_dna(entrance) == expected
