"""Test module."""

from pathlib import Path
from tempfile import gettempdir
from typing import ClassVar, NoReturn
import incolume.py.coding_dojo_jedi.dojo20241215 as pkg
import pytest


class TestPresidenteFoto:
    """Test case class."""

    t0: ClassVar = None

    def test_source(self):
        """Unittest."""
        assert pkg.SOURCE.is_file()

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param({}, 'dojo_review.json'),
            pytest.param(
                {
                    'output': (
                        file := Path(gettempdir(), 'presidente.json').resolve()
                    ),
                },
                file.as_posix(),
            ),
        ],
    )
    def test_review(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert pkg.dojo_review(**entrance).is_file()
        assert pkg.dojo_review(**entrance).as_posix() == expected
