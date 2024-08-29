"""Module."""

import re

from click.testing import CliRunner
from incolume.py.coding_dojo_jedi import cli
from tempfile import NamedTemporaryFile, gettempdir


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

    def test_dojo_sumary(self):
        """Test dojo sumary."""
        result = self.runner.invoke(
            cli.dojo,
            ['sumary', '-f', NamedTemporaryFile().name],
        )
        assert result.exit_code == 0
        assert re.search(
            'Sumário em (.*) .. criado com sucesso!\n',
            result.output,
        )

    def test_sumary(self):
        """Test sumary."""
        result = self.runner.invoke(
            cli.sumary,
            ['-f', NamedTemporaryFile().name],
        )
        assert result.exit_code == 0
        assert re.search(
            'Sumário em (.*) .. criado com sucesso!\n',
            result.output,
        )
