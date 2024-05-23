"""Test module for utils."""

import logging
import sys
from pathlib import Path

import pytest

from incolume.py.coding_dojo_jedi.utils import (
    MD_DIR,
    filesmd,
    generator_sumary,
)


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


class TestUtilsModule:
    """Case test utils."""

    def test_md_dir_type(self):
        """Check directory type."""
        assert isinstance(MD_DIR, Path)

    def test_md_dir_value(self):
        """Check directory value."""
        assert MD_DIR.parts[-3:] == (
            'incolume',
            'py',
            'coding_dojo_jedi',
        )

    @pytest.mark.skipif(
        sys.version_info < (3, 10),
        reason='requires python3.10 or higher',
    )
    @pytest.mark.skipif(
        sys.platform.startswith('win'),
        reason='Not available on windows. Requires other Operation System.',
    )
    def test_quantia(self, filemd) -> None:  # pylint: disable=redefined-outer-name
        """Testar se a quantidade de links e dojos são iguais."""
        arq = next(
            Path(__file__).absolute().parents[1].rglob('coding_dojo_jedi'),
        )
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
                b'# Coding Dojo',
            ),
            pytest.param(
                b'**Guilda JEDI Incolume - Grupo Python Incolume**',
            ),
            pytest.param(
                b'- [Seja membro da Guilda JEDI Incolume]'
                b'(https://discord.gg/eBNamXVtBW)',
            ),
            pytest.param(
                bytes('## Sumário dos dojos', encoding='utf-8'),
            ),
            pytest.param(
                b'&copy; **Incolume.com.br**',
            ),
        ],
    )
    def test_content_sumary(
        self,
        filemd,  # pylint: disable=redefined-outer-name
        entrance,
    ) -> None:
        """Teste para escopo do sumário."""
        file = generator_sumary(filemd)
        assert entrance in file.read_bytes()
