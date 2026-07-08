"""Module."""

import re

from click.testing import CliRunner
from incolume.py.coding_dojo_jedi import cli
from tempfile import gettempdir
from incolume.py.coding_dojo_jedi.utils import pseudo_filename
import pytest

__author__ = '@britodfbr'  # pragma: no cover


class TestCaseCLI:
    """Test case CLI."""

    runner = CliRunner()

    def test_dojo_show(self):
        """Test dojo show."""
        result = self.runner.invoke(
            cli.dojo,
            ['show'],
        )
        assert result.exit_code == 0
        assert re.search("{'debug': False}\nDebug is off\n", result.output)

    def test_dojo_init(self):
        """Test dojo init."""
        result = self.runner.invoke(
            cli.dojo,
            ['init', '-p', gettempdir()],
        )
        assert result.exit_code == 0
        assert 'Boilerplate para dojo criado com sucesso em' in result.output

    @pytest.mark.parametrize(
        'entrance',
        [
            pytest.param(
                pseudo_filename().as_posix(),
                id='valid_file',
            ),
        ],
    )
    def test_dojo_sumary(self, entrance):
        """Test dojo sumary."""
        result = self.runner.invoke(
            cli.dojo,
            ['sumary', '-f', entrance],
        )
        assert result.exit_code == 0
        assert re.search(
            r'Sumário em (.*) .. criado com sucesso!',
            result.output,
        )

    @pytest.mark.parametrize(
        'entrance',
        [
            pytest.param(
                pseudo_filename().as_posix(),
                id='valid_file',
            ),
        ],
    )
    def test_sumary(self, entrance):
        """Test sumary."""
        result = self.runner.invoke(
            cli.sumary,
            ['-f', entrance],
        )
        assert result.exit_code == 0
        assert re.search(
            r'Sumário em (.*) .. criado com sucesso!',
            result.output,
        )
