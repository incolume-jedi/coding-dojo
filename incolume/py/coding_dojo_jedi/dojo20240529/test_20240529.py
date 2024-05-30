"""Module."""

import logging
from pathlib import Path

from . import create_tar_gz, read_tar_gz, info_tar_gz, get_content_tar_gz

from tempfile import NamedTemporaryFile


__author__ = '@britodfbr'  # pragma: no cover


class TestCase:
    """Test case."""

    filename = Path(NamedTemporaryFile().name)

    def test_create_tar_gz(self):
        """Test create file."""
        create_tar_gz(self.filename)
        assert self.filename.is_file()

    def test_content_tar_gz(self, caplog):
        """Test content create file."""
        with caplog.at_level(logging.INFO):
            create_tar_gz(self.filename)
            assert 'README.md' in caplog.text

    def test_read_tar_gz(self):
        """Test read file."""
        assert read_tar_gz() == ['pi-1M.txt']

    def test_info_tar_gz(self, capsys):
        """Test info."""
        info_tar_gz()
        out, _ = capsys.readouterr()
        assert (
            out
            == 'pi-1M.txt is 1000002 bytes in size and is a regular file.\n'
        )

    def test_get_content(self):
        """Test content."""
        assert get_content_tar_gz() == {}
