"""Test module."""

from __future__ import annotations
from typing import ClassVar, NoReturn
import incolume.py.coding_dojo_jedi.dojo20250110 as pkg
import pytest


class TestCase:
    """Test case class."""

    t0: ClassVar = None

    def test_upper(self) -> NoReturn:
        """Unit test."""

        @pkg.upper
        def fx(x: str) -> str:
            return x

        assert fx('a') == 'A'

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param('joão da silva e silva', 'João da Silva e Silva'),
            pytest.param(
                'a casa da benção do senhor',
                'A Casa da Benção do Senhor',
            ),
        ],
    )
    def test_capitalizer(self, entrance, expected) -> NoReturn:
        """Unit test."""

        @pkg.capitalizer
        def fx(x: str) -> str:
            return x

        assert fx(entrance) == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(
                'joão da silva e silva',
                'j-o-ã-o d-a s-i-l-v-a e s-i-l-v-a',
            ),
            pytest.param(
                'a casa da benção do senhor',
                'a c-a-s-a d-a b-e-n-ç-ã-o d-o s-e-n-h-o-r',
            ),
        ],
    )
    def test_speller(self, entrance, expected) -> NoReturn:
        """Unit test."""

        @pkg.speller
        def fx(x: str) -> str:
            return x

        assert fx(entrance) == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            pytest.param(
                'a casa da benção do senhor',
                'A C-a-s-a d-a B-e-n-ç-ã-o d-o S-e-n-h-o-r',
                marks=[
                    pytest.mark.xpass(
                        reason='Implementation failing (but shoulded ran)',
                    ),
                ],
            ),
        ],
    )
    def test_0(self, entrance, expected) -> NoReturn:
        """Unittest."""
        assert pkg.dojo(entrance) == expected
