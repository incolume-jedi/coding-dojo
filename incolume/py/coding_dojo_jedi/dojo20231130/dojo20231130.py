"""Dojo."""

# ruff: noqa: C901


def boyermoore_0(palavra: str, texto: str) -> int:
    """Algoritmo boyer-moore.

    Primeira ocorrência
    """
    m = len(palavra)
    n = len(texto)
    if m > n:
        return -1

    _pulo = [m for k in range(256)]
    for k in range(m - 1):
        _pulo[ord(palavra[k])] = m - k - 1

    pulo = tuple(_pulo)
    k = m - 1
    while k < n:
        j = m - 1
        i = k
        while j >= 0 and texto[i] == palavra[j]:
            j -= 1
            i -= 1
        if j == -1:
            return i + 1
        k += pulo[ord(texto[k])]
    return -1


def boyermoore_1(word: str, text: str) -> dict[str, list]:
    """Algoritmo boyer-moore.

    Todas ocorrências
    """
    len_w = len(word)
    len_t = len(text)
    results: dict[str, list] = {word: []}
    if len_w > len_t:
        return results

    _pulo = [len_w for _ in range(256)]
    for k in range(len_w - 1):
        _pulo[ord(word[k])] = len_w - k - 1

    pulo = tuple(_pulo)
    k = len_w - 1
    while k < len_t:
        j = len_w - 1
        i = k
        while j >= 0 and text[i] == word[j]:
            j -= 1
            i -= 1
        if j == -1:
            results[word].append(i + 1)
        k += pulo[ord(text[k])]
    return results
