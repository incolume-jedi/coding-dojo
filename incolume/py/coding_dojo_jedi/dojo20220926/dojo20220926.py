"""Dojo."""


def protein0(chain: str) -> str:
    """Primeira solução.

    Implementação com função aninhada.
    Tecnica de desenvolvimento indesejada, e contra as boas práticas de
    desenvolvimento.
    """
    codons = {
        'UUC': 'F',
        'UUU': 'F',
        'UUA': 'L',
        'UUG': 'L',
        'CUU': 'L',
        'CUC': 'L',
        'CUA': 'L',
        'CUG': 'L',
        'AUU': 'I',
        'AUC': 'I',
        'AUA': 'I',
        'AUG': 'M',
        'GUU': 'V',
        'GUC': 'V',
        'GUA': 'V',
        'GUG': 'V',
        'UCU': 'S',
        'UCC': 'S',
        'UCA': 'S',
        'UCG': 'S',
        'AGU': 'S',
        'AGC': 'S',
        'CCU': 'P',
        'CCC': 'P',
        'CCA': 'P',
        'CCG': 'P',
        'ACU': 'T',
        'ACC': 'T',
        'ACA': 'T',
        'ACG': 'T',
        'GCU': 'A',
        'GCC': 'A',
        'GCA': 'A',
        'GCG': 'A',
        'UAU': 'Y',
        'UAC': 'Y',
        'CAU': 'H',
        'CAC': 'H',
        'CAA': 'Q',
        'CAG': 'Q',
        'AAU': 'N',
        'AAC': 'N',
        'AAA': 'K',
        'AAG': 'K',
        'GAU': 'D',
        'GAC': 'D',
        'GAA': 'E',
        'GAG': 'E',
        'UGU': 'C',
        'UGC': 'C',
        'UGG': 'W',
        'CGU': 'R',
        'CGC': 'R',
        'CGA': 'R',
        'CGG': 'R',
        'AGA': 'R',
        'AGG': 'R',
        'GGU': 'G',
        'GGC': 'G',
        'GGA': 'G',
        'GGG': 'G',
        'UAA': '',
        'UGA': '',
        'UAG': '',
    }

    def aminoacid(string: str) -> str:
        """Transforma cadeia de códon em aminoacido."""
        if len(string) <= 3:  # noqa: PLR2004
            return codons[string]
        return f'{codons.get(string[:3])}{aminoacid(string[3:])}'

    return aminoacid(chain.upper())


def aminoacid1(string: str, codons: dict) -> str:
    """Transforma cadeia de códon em aminoacido."""
    if len(string) <= 3:  # noqa: PLR2004
        return str(codons.get(string))
    return f'{codons.get(string[:3])}{aminoacid1(string[3:], codons)}'


def protein1(chain: str) -> str:
    """Exemplo aplicado com correção de função aninha.

    função aninha extraída.
    """
    codons = {
        'UUC': 'F',
        'UUU': 'F',
        'UUA': 'L',
        'UUG': 'L',
        'CUU': 'L',
        'CUC': 'L',
        'CUA': 'L',
        'CUG': 'L',
        'AUU': 'I',
        'AUC': 'I',
        'AUA': 'I',
        'AUG': 'M',
        'GUU': 'V',
        'GUC': 'V',
        'GUA': 'V',
        'GUG': 'V',
        'UCU': 'S',
        'UCC': 'S',
        'UCA': 'S',
        'UCG': 'S',
        'AGU': 'S',
        'AGC': 'S',
        'CCU': 'P',
        'CCC': 'P',
        'CCA': 'P',
        'CCG': 'P',
        'ACU': 'T',
        'ACC': 'T',
        'ACA': 'T',
        'ACG': 'T',
        'GCU': 'A',
        'GCC': 'A',
        'GCA': 'A',
        'GCG': 'A',
        'UAU': 'Y',
        'UAC': 'Y',
        'CAU': 'H',
        'CAC': 'H',
        'CAA': 'Q',
        'CAG': 'Q',
        'AAU': 'N',
        'AAC': 'N',
        'AAA': 'K',
        'AAG': 'K',
        'GAU': 'D',
        'GAC': 'D',
        'GAA': 'E',
        'GAG': 'E',
        'UGU': 'C',
        'UGC': 'C',
        'UGG': 'W',
        'CGU': 'R',
        'CGC': 'R',
        'CGA': 'R',
        'CGG': 'R',
        'AGA': 'R',
        'AGG': 'R',
        'GGU': 'G',
        'GGC': 'G',
        'GGA': 'G',
        'GGG': 'G',
        'UAA': '',
        'UGA': '',
        'UAG': '',
    }
    return aminoacid1(chain.upper(), codons)


def protein(chain: str) -> str:
    """Fatoração com recursividade integrada."""
    codons = {
        'UUC': 'F',
        'UUU': 'F',
        'UUA': 'L',
        'UUG': 'L',
        'CUU': 'L',
        'CUC': 'L',
        'CUA': 'L',
        'CUG': 'L',
        'AUU': 'I',
        'AUC': 'I',
        'AUA': 'I',
        'AUG': 'M',
        'GUU': 'V',
        'GUC': 'V',
        'GUA': 'V',
        'GUG': 'V',
        'UCU': 'S',
        'UCC': 'S',
        'UCA': 'S',
        'UCG': 'S',
        'AGU': 'S',
        'AGC': 'S',
        'CCU': 'P',
        'CCC': 'P',
        'CCA': 'P',
        'CCG': 'P',
        'ACU': 'T',
        'ACC': 'T',
        'ACA': 'T',
        'ACG': 'T',
        'GCU': 'A',
        'GCC': 'A',
        'GCA': 'A',
        'GCG': 'A',
        'UAU': 'Y',
        'UAC': 'Y',
        'CAU': 'H',
        'CAC': 'H',
        'CAA': 'Q',
        'CAG': 'Q',
        'AAU': 'N',
        'AAC': 'N',
        'AAA': 'K',
        'AAG': 'K',
        'GAU': 'D',
        'GAC': 'D',
        'GAA': 'E',
        'GAG': 'E',
        'UGU': 'C',
        'UGC': 'C',
        'UGG': 'W',
        'CGU': 'R',
        'CGC': 'R',
        'CGA': 'R',
        'CGG': 'R',
        'AGA': 'R',
        'AGG': 'R',
        'GGU': 'G',
        'GGC': 'G',
        'GGA': 'G',
        'GGG': 'G',
        'UAA': '',
        'UGA': '',
        'UAG': '',
    }
    chain = chain.upper()
    if len(chain) <= 3:  # noqa: PLR2004
        return f'{codons.get(chain)}'
    return f'{codons.get(chain[:3])}{protein(chain[3:])}'


if __name__ == '__main__':  # pragma: no cover
    print(  # noqa: T201
        protein('CAU'),
        protein('CAUAAAGAA'),
        protein('CAUAAAUAGGAA'),
        protein('cauaaagaauaa'),
    )
