"""Dojo."""


def dna2rna(dna: str) -> str:
    """Transforma cadeia de DNA em RNA."""
    return dna.translate(dna.maketrans({'T': 'U'}))
