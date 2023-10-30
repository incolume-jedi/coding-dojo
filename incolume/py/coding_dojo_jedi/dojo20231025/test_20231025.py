"""Test module for dojo."""
import re
import sys
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


@pytest.mark.skipif(
    sys.platform.startswith('win'), reason='Not available on windows.'
)
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
        pytest.param(
            r'# Coding Dojo',
            marks=pytest.mark.skipif(
                sys.platform.startswith('win'),
                reason='Does not run on windows.',
            ),
        ),
        pytest.param(
            '**Guilda JEDI Incolume - Grupo Python Incolume**',
            marks=pytest.mark.skipif(
                sys.platform.startswith('win'),
                reason='Does not run on windows.',
            ),
        ),
        pytest.param(
            '- [Seja membro da Guilda JEDI Incolume]'
            '(https://discord.gg/eBNamXVtBW)',
            marks=pytest.mark.skipif(
                sys.platform.startswith('win'),
                reason='Does not run on windows.',
            ),
        ),
        pytest.param(
            '## Sumário dos dojos',
            marks=pytest.mark.skipif(
                sys.platform.startswith('win'),
                reason='Does not run on windows.',
            ),
        ),
        pytest.param(
            '&copy; **Incolume.com.br**',
            marks=pytest.mark.skipif(
                sys.platform.startswith('win'),
                reason='Does not run on windows.',
            ),
        ),
    ],
)
def test_content_sumary(
    filemd,  # pylint: disable=redefined-outer-name
    entrance,
) -> None:
    """Teste para escopo do sumário."""
    file = generator_sumary(filemd)
    assert entrance in file.read_text()
