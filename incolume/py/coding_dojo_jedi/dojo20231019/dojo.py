"""Dojo contagem de nucleotídeos."""


def contador_nucleotideos(nucleotideo: str) -> str:
    """Contar nucleotídeos."""
    a = nucleotideo.upper().count('A')
    c = nucleotideo.upper().count('C')
    g = nucleotideo.upper().count('G')
    t = nucleotideo.upper().count('T')

    return f'{a} {c} {g} {t}'

def complemento_fita_dna(fita: str) -> str:
    """Complementar fita."""
    sc = ''
    dic_codon = {
        'A': 'T',
        'T': 'A',
        'G': 'C',
        'C': 'G',
    }
    for s in fita.upper():
        sc = dic_codon[s] + sc
    return sc
