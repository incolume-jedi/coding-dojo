import heapq


def classify0(quantia: int, lista: list)->tuple:
    """ """
    lista.sort()
    if quantia == 1:
        return max(lista), min(lista)
    return tuple(sorted(lista, reverse=True)[:quantia]), tuple(lista[:quantia])


def classify1(quantia: int, lista: list)->tuple:
    if quantia == 1:
        return max(lista), min(lista)
    return tuple(heapq.nlargest(quantia, lista)), tuple(heapq.nsmallest(quantia, lista))


def classify(quantia: int, lista: list)->tuple:
    result = {
        1: (max(lista), min(lista))
    }
    return result.get(quantia, (tuple(heapq.nlargest(quantia, lista)), tuple(heapq.nsmallest(quantia, lista))))
