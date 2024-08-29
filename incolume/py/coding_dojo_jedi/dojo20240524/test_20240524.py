"""Module."""

from typing import ClassVar

from . import gen_playlist, playlist
import pytest

__author__ = '@britodfbr'  # pragma: no cover


class Testcase:
    """TEst case."""

    tests_0: ClassVar = [
        [1, 2, 3, 4],
        [6, 1, 2, 3, 4],
    ]
    size = 5
    mult = 3

    @pytest.mark.parametrize(
        'entrance',
        tests_0,
    )
    def test_playlist0(self, entrance):
        """Test it."""
        size = len(entrance)
        pl = gen_playlist(entrance)
        expected = next(pl)
        faixas = [next(pl) for _ in range(size)]
        assert faixas[-1] == expected

    @pytest.mark.parametrize(
        'entrance',
        tests_0,
    )
    def test_playlist(self, entrance):
        """Test it."""
        size = len(entrance)
        pl = playlist(entrance)
        expected = next(pl)
        faixas = [next(pl) for _ in range(size)]
        assert faixas[-1] == expected

    def test_pl0_size(self):
        """Size list."""
        pl = gen_playlist(range(self.size))
        faixas = [next(pl) for _ in range(self.size * self.mult + 1)]
        assert len(faixas) == self.size * self.mult + 1

    def test_pl_size(self):
        """Size list."""
        pl = playlist(range(self.size))
        faixas = [next(pl) for _ in range(self.size * self.mult + 1)]
        assert len(faixas) == self.size * self.mult + 1

    def test_pl0_count(self):
        """Count elements."""
        pl = gen_playlist(range(self.size))
        faixas = [next(pl) for _ in range(self.size * self.mult + 1)]
        assert faixas.count(faixas[0]) == self.mult + 1

    def test_pl_count(self):
        """Count elements."""
        pl = playlist(range(self.size))
        faixas = [next(pl) for _ in range(self.size * self.mult + 1)]
        assert faixas.count(faixas[0]) == self.mult + 1
