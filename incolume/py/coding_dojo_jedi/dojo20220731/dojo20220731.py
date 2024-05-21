"""Dojo 2022-07-31."""


def show_table_ascii0() -> list:
    """Exibe a tabela ascii."""
    lista = []
    for code in range(256):
        letra = chr(code)
        lista.append((code, letra))
    return lista


def show_table_ascii() -> list:
    """Exibe a tabela ascii."""
    return [(code, chr(code)) for code in range(256)]
