"""Test module."""

from __future__ import annotations
from typing import ClassVar, NoReturn
import incolume.py.coding_dojo_jedi.dojo20260622 as pkg
import pytest


class TestCase:
    """Test case class."""

    t0: ClassVar = None

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(
                {'url': 'http://brito.blog.incolume.com.br', 'flout': ''},
                True,
                marks=[],
            ),
        ],
    )
    def test_gen_qrcode(self, entrance, expected) -> NoReturn:
        """Test gen_qrcode."""
        result = pkg.gen_qrcode(**entrance)
        assert result.exists() == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(
                None,
                None,
                marks=[
                    pytest.mark.xfail(
                        reason='Implementation failing (but shoulded ran)'
                    )
                ],
            ),
        ],
    )
    def test_0(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert pkg.dojo(entrance) == expected
