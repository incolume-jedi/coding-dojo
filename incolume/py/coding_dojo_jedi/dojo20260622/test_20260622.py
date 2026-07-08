"""Test module."""

from __future__ import annotations
from typing import ClassVar, NoReturn
import incolume.py.coding_dojo_jedi.dojo20260622 as pkg
import pytest


class TestCase:
    """Test case class."""

    t0: ClassVar = None

    @pytest.mark.parametrize(
        'entrance',
        [
            pytest.param(
                {'url': 'http://brito.blog.incolume.com.br', 'flout': ''},
                marks=[],
            ),
        ],
    )
    def test_gen_qrcode(self, entrance) -> NoReturn:
        """Test gen_qrcode."""
        result = pkg.gen_qrcode(**entrance)
        assert result.exists()

    def test_dojo(self) -> NoReturn:
        """Test dojo."""
        result = pkg.dojo()
        assert result.exists()
