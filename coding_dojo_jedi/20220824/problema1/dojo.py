"""
Validação de custo computacional:

from dis import dis

dis(dna_complementary0)
dis(dna_complementary)

"""

def dna_complementary0(dna_string: str)->str:
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    return ''.join(complement.get(x) for x in dna_string)


def dna_complementary(dna_string: str)->str:
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    return dna_string.translate(dna_string.maketrans(complement))
