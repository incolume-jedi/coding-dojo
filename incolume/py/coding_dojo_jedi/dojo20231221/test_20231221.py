"""Test module."""

from pathlib import Path
from tempfile import gettempdir
from typing import ClassVar, NoReturn
import incolume.py.coding_dojo_jedi.dojo20231221 as pkg
import pytest


class TestCase:
    """Test case class."""

    t0: ClassVar = None

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            ({}, 'dojo.json'),
            (
                {
                    'output': (
                        file := Path(gettempdir(), 'presidente.json').resolve()
                    ),
                },
                file.as_posix(),
            ),
        ],
    )
    def test_0(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert pkg.dojo(**entrance).as_posix() == expected
