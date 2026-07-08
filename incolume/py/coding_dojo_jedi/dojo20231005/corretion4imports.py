"""Solução para demanda #116."""

from pathlib import Path


def tratativa0() -> None:
    """Exibir arquivos com problemas de import."""
    arquivos = ''
    print(arquivos)  # noqa: T201


def tratativa1() -> None:
    """Exibir conteúdo do arquivo csv."""
    file_csv = Path(__file__).with_name('list_error_import.csv')
    print(file_csv.read_text())  # noqa: T201


def tratativa2() -> None:
    """Exibir linhas do arquivo csv."""
    with Path(__file__).with_name('list_error_import.csv').open() as file_csv:
        for linha in file_csv:
            print(linha)  # noqa: T201


if __name__ == '__main__':
    tratativa1()
