"""Module."""

# !/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import ClassVar
import pytest
from . import alt_num_feliz, double_minor_feliz, trio_minor_feliz, NFeliz


__author__ = '@britodfbr'  # pragma: no cover


class TestDojoFeliz:
    """Test case class."""

    altura_feliz: ClassVar = [
        (1, 1),
        (7, 5),
        (13, 2),
        (15, -1),
        (19, 4),
        (68, 2),
        (97, 3),
    ]

    def test_double_menor_feliz(self):
        """Test it."""
        assert double_minor_feliz() == (31, 32)

    def test_trio_menor_feliz(self):
        """Test it."""
        assert trio_minor_feliz() == (1880, 1881, 1882)

    @pytest.mark.skip(reason='fail coding.')
    @pytest.mark.parametrize(
        'entrance expected'.split(),
        altura_feliz,
    )
    def test_nfeliz(self, entrance, expected):
        """Test it."""
        obj = NFeliz(entrance)
        assert obj.height == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        altura_feliz,
    )
    def test_alt_num_feliz(self, entrance, expected):
        """Test it."""
        assert alt_num_feliz(entrance) == expected
