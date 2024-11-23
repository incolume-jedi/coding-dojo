"""Test module for utils."""

import datetime as dt
import logging
from pathlib import Path
from typing import NoReturn
import tempfile
import pytest
import pytz

from incolume.py.coding_dojo_jedi.utils import (
    MD_DIR,
    filesmd,
    generator_sumary,
    dojo_init,
    pseudo_filename,
)
from tests.conftest import py310, not_win


@pytest.fixture
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

    tz: str = 'America/Sao_Paulo'
    timestamp = dt.datetime(1978, 6, 20, tzinfo=pytz.timezone(tz))
    filename = pseudo_filename()

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

    @pytest.mark.skip
    @py310
    @not_win
    def test_quantia(self, filemd) -> None:  # pylint: disable=redefined-outer-name
        """Testar se a quantidade de links e dojos são iguais."""
        arq = next(
            Path(__file__).absolute().parents[1].rglob('coding_dojo_jedi'),
        )
        c_links = count_links(generator_sumary(filemd))
        c_dirs = len(filesmd())
        logging.debug('%s %s %s', arq, c_dirs, c_links)
        assert c_links == c_dirs

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            ({'fout': filename.with_name('sumario.md')}, 'sumario.md'),
            (
                {
                    'fout': filename.with_name('dojos-resolvidos.md'),
                    'is_doc': True,
                },
                'dojos-resolvidos.md',
            ),
        ],
    )
    def test_sumary_name(self, entrance, expected) -> NoReturn:
        """Test sumary name."""
        assert expected in generator_sumary(**entrance).as_posix()

    @pytest.mark.skip
    @py310
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

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            (
                {
                    'dojo_path': tempfile.gettempdir(),
                    'dojo_date': timestamp,
                },
                Path(tempfile.gettempdir())
                / f'dojo{timestamp:%Y%m%d}'
                / 'README.md',
            ),
            (
                {
                    'dojo_path': tempfile.gettempdir(),
                    'dojo_date': timestamp,
                },
                Path(tempfile.gettempdir())
                / f'dojo{timestamp:%Y%m%d}'
                / '__init__.py',
            ),
            (
                {
                    'dojo_path': tempfile.gettempdir(),
                    'dojo_date': timestamp,
                },
                Path(tempfile.gettempdir())
                / f'dojo{timestamp:%Y%m%d}'
                / 'test_19780620.py',
            ),
        ],
    )
    def test_dojo_init(self, entrance, expected) -> NoReturn:
        """Test dojo init."""
        assert expected in dojo_init(**entrance)
