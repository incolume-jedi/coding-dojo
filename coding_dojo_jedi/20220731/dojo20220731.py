def show_table_ascii():
    lista = []
    for code in range(256):
        letra = chr(code)
        lista.append((code, letra))
    return lista
