"""Dojo."""


def boyermoore(palavra: str, texto: str) -> dict[str,int]:
    """Algoritmo boyer-moore."""
    m = len(palavra)
    n = len(texto)
    if m > n: return -1
    pulo = [m for k in range(256)]
    for k in range(m - 1): 
        pulo[ord(palavra[k])] = m-k-1
    pulo = tuple(pulo)
    print(pulo)
    k = m - 1
    while k < n:
        j = m -1
        i = k
        while j >= 0 and texto[i] == palavra[j]:
            j -= 1
            i -= 1
        if j == -1: 
            return i + 1
        k += pulo[ord(texto[k])]
    return -1

