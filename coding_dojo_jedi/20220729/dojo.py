def dna2rna(dna: str) -> str:
    return dna.translate(dna.maketrans({'T': 'U'}))
