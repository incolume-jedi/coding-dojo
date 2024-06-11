"""Test module."""

from pathlib import Path
from typing import NoReturn
import incolume.py.coding_dojo_jedi.dojo20240608 as pkg
from tempfile import NamedTemporaryFile


class TestCase:
    """Test case class."""

    def test_0(self) -> NoReturn:
        """Unittest."""
        entrance = Path(NamedTemporaryFile().name)
        entrance = None
        assert pkg.set_compose_file(entrance)
