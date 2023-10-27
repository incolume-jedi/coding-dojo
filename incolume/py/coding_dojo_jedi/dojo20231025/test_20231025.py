"""Test module for dojo."""
import re
from pathlib import Path
from tempfile import NamedTemporaryFile

import pytest

from incolume.py.coding_dojo_jedi.dojo20231025.dojo import generator_sumary


@pytest.fixture()
def filemd() -> Path:
    """Retornar arquivo MD."""
    return Path(NamedTemporaryFile(suffix='.md', prefix='File-').name)


def count_links(arq_entrada: Path) -> int:
    """Contar os links do sumario.md."""
    contagem = 0
    with arq_entrada.open() as f:
        for line in f:
            if line.startswith('1'):
                contagem += 1
    return contagem


def count_dojos(path_dojos: Path) -> int:
    """Contar os dojos no Sistema de Arquivos."""
    regex = r'## Problema\s*\*\*((\w+\s*)+)\*\*'
    total = 0
    for file in path_dojos.rglob('**/*.md'):
        result = re.search(regex, file.read_text(), flags=re.I)
        if result:
            total += 1
    return total


def test_quantia(filemd) -> None:  # pylint: disable=redefined-outer-name
    """Testar se a quantidade de links e dojos são iguais."""
    c_links = count_links(generator_sumary(filemd))
    c_dirs = count_dojos(Path(__file__).absolute().parents[1])
    assert c_links == c_dirs


@pytest.mark.parametrize(
    'entrance',
    [
        r'# Coding Dojo',
        r'**Guilda JEDI Incolume - Grupo Python Incolume**',
        r'- [Seja membro da Guilda JEDI Incolume]'
        r'(https://discord.gg/eBNamXVtBW)',
        r'## Sumário dos dojos',
        r'&copy; **Incolume.com.br**',
    ],
)
def test_content_sumary(
    filemd,  # pylint: disable=redefined-outer-name
    entrance,
) -> None:
    """Teste para escopo do sumário."""
    file = generator_sumary(filemd)
    assert entrance in file.read_text()
