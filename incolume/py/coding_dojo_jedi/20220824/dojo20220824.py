"""
Validação de custo computacional:

from dis import dis

dis(dna_complementary0)
dis(dna_complementary)
"""


def dna_complementary0(dna_string: str) -> str:
    """Problema 1."""
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    return ''.join(complement.get(x) for x in dna_string)


def dna_complementary(dna_string: str) -> str:
    """Problema 1."""
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    return dna_string.translate(dna_string.maketrans(complement))


def millisseconds(*, h: int = 0, m: int = 0, s: int = 0) -> int:
    """Problema 2."""
    if not (0 <= h <= 23):
        raise ValueError('0 <= h <= 23')

    if not (0 <= m < 60):
        raise ValueError('0 <= m <= 59')

    if not (0 <= s < 60):
        raise ValueError('0 <= s <= 59')

    return (h * 3600 + m * 60 + s) * 1000
