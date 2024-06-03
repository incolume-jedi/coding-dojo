"""Module."""

# !/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from collections import OrderedDict
from itertools import count
from pathlib import Path

import httpx
import pandas as pd
from bs4 import BeautifulSoup
from icecream import ic
from unidecode import unidecode

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
        self._scrap()

    def __scrap(self) -> None:
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
            strict=False,
        ):
            d[th.text.strip()] = td.text.strip().splitlines()

        title = [th.text for th in result.select('th span:nth-of-type(1)')]
        content = [td.text for td in result.select('td')]
        content = len(result.select('td'))
        title = [th.text for th in result.select('th div:nth-of-type(1)')]
        content = title
        content = d
        self.content = content

    def _scrap(self):
        """Scrap content."""
        content = pd.read_html(self.url_or_path, encoding='utf-8')
        df: pd.DataFrame = ic(content[0])
        df.drop(df.columns[[0, 11, 12]], axis=1, inplace=True)  # noqa: PD002
        df.columns = df.columns.str.upper()
        df.columns = [
            'RANK',
            'CLUBE',
            'PONTOS',
            'PARTIDAS JOGADAS',
            'VITÓRIAS',
            'EMPATES',
            'DERROTAS',
            'GOLS MARCADOS',
            'GOLS CONTRA',
            'SALDO DE GOLS',
        ]

        df['STATUS'] = df.RANK.apply(
            lambda x: ''.join(n for n in x if not n.isdigit()),
        )
        c = count(1)
        df.RANK = df.RANK.map(lambda x: next(c))  # noqa: ARG005
        ic(df.head())
        self.content = df.to_dict()

    def sort_by_name(self, *, reverse: bool = False) -> list:
        """Sort by name."""
        return sorted((self.content.get('CLUBE').values()), reverse=reverse)

    def sort_by_point(self, *, reverse: bool = False) -> list:
        """Sort by point."""
        rank = sorted(
            (
                (k, v, m)
                for k, v, m in zip(
                    self.content.get('PONTOS').values(),
                    self.content.get('SALDO DE GOLS').values(),
                    self.content.get('CLUBE').values(),
                    strict=False,
                )
            ),
            reverse=reverse,
        )
        return [clube[2] for clube in rank]

    def classify_libertadores(self):
        """Classificado para fase de grupo da libertadores."""
        return self.classify()[:4]

    def qualify_libertadores(self):
        """Selecionados para Qualificatórias da libertadores."""
        return self.classify()[4:6]

    def select_sulamericana(self):
        """Selecionados para fase de grupos da copa sulamericana."""
        return self.classify()[6:12]

    def rebaixados(self):
        """Clubes rebaixados."""
        return self.classify()[-4:]

    def classify(self) -> list:
        """Classificação por pontos no Campeonato brasileiro de futebol."""
        return self.sort_by_point(reverse=True)

    def clube(self, clube_name: str) -> int:
        """Classificação por pontos no Campeonato brasileiro de futebol."""
        clubes = {
            unidecode(v.casefold()): k
            for k, v in self.content.get('CLUBE').items()
        }
        index = clubes.get(unidecode(clube_name.casefold()))
        return self.content.get('PONTOS').get(index)
