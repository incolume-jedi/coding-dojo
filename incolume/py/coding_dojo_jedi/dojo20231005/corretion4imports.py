"""Solução para demanda #116."""
from pathlib import Path



def tratativa0():
    """Exibir arquivos com problemas de import."""
    print(arquivos)
    

def tratativa1():
    """Tratativa 1"""
    file_csv = Path(__file__).with_name('list_error_import.csv')
    print(file_csv.read_text())


def tratativa2()-> None:
    """"""
    with Path(__file__).with_name('list_error_import.csv').open() as file_csv:
        for linha in file_csv:
            print(linha)
            

if __name__ == "__main__":
    tratativa1()
