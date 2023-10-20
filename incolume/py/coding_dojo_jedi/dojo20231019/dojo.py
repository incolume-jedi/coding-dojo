"""Dojo contagem de nucleotídeos."""


def contador_nucleotideos(nucleotideo: str) -> str:
    """Contar nucleotídeos."""
    a, c, g, t = 0, 0, 0, 0

    for codigo in nucleotideo:
        if codigo == 'A':
            a += 1
        elif codigo == 'C':
            c += 1
        elif codigo == 'G':
            g += 1
        elif codigo == 'T':
            t += 1

    return str(a) + ' ' + str(c) + ' ' + str(g) + ' ' + str(t)



def complemento_fita_dna(fita: str) -> str:
    """Complementar fita."""
    sc = ''
    for s in fita.upper()[::-1]:
        if s == 'A':
            sc += 'T'
        if s == 'T':
            sc += 'A'
        if s == 'G':
            sc += 'C'
        if s == 'C':
            sc += 'G'
    return sc


    