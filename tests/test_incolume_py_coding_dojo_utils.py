"""Test module for utils."""

import logging
import sys
from pathlib import Path

import pytest

from incolume.py.coding_dojo_jedi.utils import filesmd, generator_sumary


@pytest.fixture()
def filemd(fakefile) -> Path:
    """Retornar arquivo MD."""
    return fakefile.with_suffix('.md')


def count_links(arq_entrada: Path) -> int:
    """Contar os links do sumario.md."""
    contagem = 0
    with arq_entrada.open() as f:
        for line in f:
            if line.startswith(' -'):
                contagem += 1
    return contagem


@pytest.mark.skipif(
    sys.version_info < (3, 10),
    reason='requires python3.10 or higher',
)
@pytest.mark.skipif(
    sys.platform.startswith('win'),
    reason='Not available on windows.',
)
def test_quantia(filemd) -> None:  # pylint: disable=redefined-outer-name
    """Testar se a quantidade de links e dojos são iguais."""
    arq = next(Path(__file__).absolute().parents[1].rglob('coding_dojo_jedi'))
    c_links = count_links(generator_sumary(filemd))
    c_dirs = len(filesmd())
    logging.debug('%s %s %s', arq, c_dirs, c_links)
    assert c_links == c_dirs


@pytest.mark.skipif(
    sys.version_info < (3, 10),
    reason='requires python3.10 or higher',
)
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
