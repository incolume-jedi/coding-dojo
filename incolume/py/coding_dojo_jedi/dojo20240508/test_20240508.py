"""Module."""

# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'  # pragma: no cover
from . import double_minor_feliz, trio_minor_feliz


class TestDoubleMenorFeliz:
    """Test case class."""

    def test_double_menor_feliz(self):
        """Test it."""
        assert double_minor_feliz() == (31, 32)

    def test_trio_menor_feliz(self):
        """Test it."""
        assert trio_minor_feliz() == (1880, 1881, 1882)
