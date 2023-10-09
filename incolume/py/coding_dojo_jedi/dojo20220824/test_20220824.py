from re import escape

import pytest

from incolume.py.coding_dojo_jedi.dojo20220824.dojo20220824 import (
    dna_complementary,
    millisseconds,
)


@pytest.mark.parametrize(
    ('entrance', 'expected'),
    (
        ('ATTGC', 'TAACG'),
        ('GTAT', 'CATA'),
        (
            'TTGGGGGGCGTCAGCTGCTAAGTTGAATATCTTAGAAGTGGTTTATTAGA',
            'AACCCCCCGCAGTCGACGATTCAACTTATAGAATCTTCACCAAATAATCT',
        ),
        (
            'GTATGAGGCTGGATTTGCCGACACCTTCTGCCCCCATAGGCTGTATGGGG',
            'CATACTCCGACCTAAACGGCTGTGGAAGACGGGGGTATCCGACATACCCC',
        ),
        (
            'AGGCAGATACGTCGCGACCATTGTACAAGAATCACTTCACACGGTCTGGA',
            'TCCGTCTATGCAGCGCTGGTAACATGTTCTTAGTGAAGTGTGCCAGACCT',
        ),
        (
            'GATGTCCTGATCTCTACAGTATCGACATGGGTAACCCACCCATGTAAAGG',
            'CTACAGGACTAGAGATGTCATAGCTGTACCCATTGGGTGGGTACATTTCC',
        ),
        (
            'CTAACTCATACACGTACGATGCTGGAGGGATGAATAGCGCGGGCACGTTC',
            'GATTGAGTATGTGCATGCTACGACCTCCCTACTTATCGCGCCCGTGCAAG',
        ),
        (
            'TACCGAGCTCCCTACGCTTGCATCGACAGGACCACGTACGATCCGAGGTC',
            'ATGGCTCGAGGGATGCGAACGTAGCTGTCCTGGTGCATGCTAGGCTCCAG',
        ),
        (
            'CTTATCGTAAGCGGTTACGCCACAGATGTTCTACCTTATCTCTCATTCAC',
            'GAATAGCATTCGCCAATGCGGTGTCTACAAGATGGAATAGAGAGTAAGTG',
        ),
        (
            'CCACGTCCGAATCCAATCCTTATGCGCTTTTTCACAGTTGCATAGGTCTA',
            'GGTGCAGGCTTAGGTTAGGAATACGCGAAAAAGTGTCAACGTATCCAGAT',
        ),
        (
            'GGACGTGTGCGCCGAGAGGCTCGAGGGCGTTAGTCTTGTACCTAGGGGGC',
            'CCTGCACACGCGGCTCTCCGAGCTCCCGCAATCAGAACATGGATCCCCCG',
        ),
        (
            'GCCTTCACGGGTGAAGTATTGTTCCGGGCACGGATAATGACAGTGCTGAG',
            'CGGAAGTGCCCACTTCATAACAAGGCCCGTGCCTATTACTGTCACGACTC',
        ),
        (
            'TAACCCTTGGTCGGAGCAAGCTCTGAGTCACAACATGGCATTACCTTGCG',
            'ATTGGGAACCAGCCTCGTTCGAGACTCAGTGTTGTACCGTAATGGAACGC',
        ),
    ),
)
def test_dna_complementary(entrance, expected):
    assert dna_complementary(entrance) == expected


@pytest.mark.parametrize(
    'entrance expected'.split(),
    (
        ({}, 0),
        ({'s': 1}, 1_000),
        ({'m': 1}, 60_000),
        ({'h': 1}, 3_600_000),
        ({'m': 1, 's': 1}, 61_000),
        ({'h': 1, 's': 1}, 3_601_000),
        ({'h': 1, 'm': 1}, 3_660_000),
        ({'h': 0, 'm': 0, 's': 0}, 0),
        ({'h': 23, 'm': 59, 's': 59}, 86_399_000),
    ),
)
def test_millissenconds(entrance, expected):
    assert millisseconds(**entrance) == expected


@pytest.mark.parametrize(
    'entrance expected'.split(),
    (
        (
            (0, 0, 0),
            {
                'expected_exception': TypeError,
                'match': r'millisseconds\(\) takes 0 positional'
                r' arguments but 3 were given',
            },
        ),
        (
            (1, 1, 1),
            {
                'expected_exception': TypeError,
                'match': escape(
                    'millisseconds() takes 0 positional '
                    'arguments but 3 were given',
                ),
            },
        ),
        (
            {'h': -1, 'm': 0, 's': 0},
            {'expected_exception': ValueError, 'match': '0 <= h <= 23'},
        ),
        (
            {'h': 24, 'm': 0, 's': 0},
            {'expected_exception': ValueError, 'match': '0 <= h <= 23'},
        ),
        (
            {'h': 0, 'm': -1, 's': 0},
            {'expected_exception': ValueError, 'match': '0 <= m <= 59'},
        ),
        (
            {'h': 0, 'm': 60, 's': 0},
            {'expected_exception': ValueError, 'match': '0 <= m <= 59'},
        ),
        (
            {'h': 0, 'm': 0, 's': -2},
            {'expected_exception': ValueError, 'match': '0 <= s <= 59'},
        ),
        (
            {'h': 0, 'm': 0, 's': 60},
            {'expected_exception': ValueError, 'match': '0 <= s <= 59'},
        ),
    ),
)
def test_millissenconds_exception(entrance, expected):
    with pytest.raises(**expected):
        if isinstance(entrance, dict):
            millisseconds(**entrance)
        else:
            millisseconds(*entrance)
