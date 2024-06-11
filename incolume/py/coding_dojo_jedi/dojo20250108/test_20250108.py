"""Test module."""

from __future__ import annotations
from pathlib import Path
from typing import ClassVar, NoReturn
import incolume.py.coding_dojo_jedi.dojo20250108 as pkg
import pytest
from tempfile import NamedTemporaryFile


class TestCase:
    """Test case class."""

    t0: ClassVar = None

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(
                None,
                None,
                marks=[
                    pytest.mark.xpass(
                        reason='Implementation failing (but shoulded ran)',
                    ),
                ],
            ),
        ],
    )
    def test_2(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert pkg.dojo(entrance) == expected

    def test_0(self) -> NoReturn:
        """Unittest."""
        entrance = Path(NamedTemporaryFile().name)
        # entrance = None
        assert pkg.set_compose_file(entrance)

    def test_1(self) -> NoReturn:
        """Unittest."""
        assert isinstance(pkg.connect(), pkg.psycopg2._T_conn)
