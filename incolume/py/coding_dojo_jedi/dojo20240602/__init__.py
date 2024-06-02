"""Module."""

# !/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from collections import OrderedDict
from inspect import stack
from pathlib import Path

import httpx
from bs4 import BeautifulSoup
from icecream import ic

__author__ = '@britodfbr'  # pragma: no cover


ic.disable()
if os.getenv('DEBUG_MODE'):
    ic.enable()


class CBF:
    """Campeonato Brasileiro de Futebol."""

    def __init__(self, url_or_path: str) -> None:
        """Init."""
        self.url_or_path: str = ic(url_or_path)
        self.content: OrderedDict = OrderedDict()
        self.scrap()

    def scrap(self) -> None:
        """Scrap content."""
        try:
            response = httpx.get(self.url_or_path)
            soup = BeautifulSoup(response.content, 'html5lib')
        except httpx.UnsupportedProtocol:
            with Path(self.url_or_path).open('rb') as f:
                soup = BeautifulSoup(f.read(), 'html5lib')
        result = soup.table

        d = OrderedDict()
        for th, td in zip(
            soup.select('th')[::2],
            soup.select('td'),
        ):
            d[th.text.strip()] = td.text.strip().splitlines()

        # title = [th.text for th in result.select('th span:nth-of-type(1)')]
        # content = [td.text for td in result.select('td')]
        # content = len(result.select('td'))
        # title = [th.text for th in result.select('th div:nth-of-type(1)')]
        # content = title
        content = d
        self.content = content

    def sort_by_name(self, *, reverse: bool = False) -> list:
        """Sort by name."""

    def sort_by_point(self, *, reverse: bool = False) -> list:
        """Sort by point."""

    def classify_libertadores(self):
        """Classificado para fase de grupo da libertadores."""

    def qualify_libertadores(self):
        """Selecionados para Qualificatórias da libertadores."""

    def select_sulamericana(self):
        """Selecionados para fase de grupos da copa sulamericana."""

    def rebaixados(self):
        """Clubes rebaixados."""

    def classify(self, clube: str) -> int:
        """Classificação por pontos no Campeonato brasileiro de futebol."""
