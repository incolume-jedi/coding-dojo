"""Test module for dojo."""
from pathlib import Path
from tempfile import NamedTemporaryFile

import pytest

from incolume.py.coding_dojo_jedi.dojo20231025.dojo import generator_sumary


@pytest.fixture()
def filemd() -> Path:
    """Retornar arquivo MD."""
    return Path(NamedTemporaryFile(suffix='.md', prefix='File-').name)


@pytest.mark.skip(
    reason='Quantidade de dojos válidos com discrepância '
    'muito alta. Necessários averiguação.',
)
def test_quantia(filemd) -> None:  # pylint: disable=redefined-outer-name
    """Testar se a quantidade de links e dojos são iguais."""

    def count_links(arq_entrada: Path) -> int:
        """Contar os links do sumario.md."""
        contagem = 0
        with arq_entrada.open() as f:
            for line in f:
                if line.startswith('1'):
                    contagem += 1
        return contagem

    assert count_links(generator_sumary(filemd)) == len(
        list(Path(__file__).absolute().parents[1].rglob('**/README.md')),
    )


@pytest.mark.parametrize(
    'entrance',
    [
        '# Coding Dojo',
        '**Guilda JEDI Incolume - Grupo Python Incolume**',
        '- [Seja membro da Guilda JEDI Incolume]'
        '(https://discord.gg/eBNamXVtBW)',
        '## Sumário dos dojos',
        '&copy; Incolume.com.br',
    ],
)
def test_content_sumary(
    filemd,  # pylint: disable=redefined-outer-name
    entrance,
) -> None:
    """Teste para escopo do sumário."""
    file = generator_sumary(filemd)
    assert entrance in file.read_text()


# link correto
