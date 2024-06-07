"""dojo module."""

import os
from itertools import count
from pathlib import Path

import httpx
import pandas as pd
from icecream import ic

ic.disable()
if os.getenv('DEBUG_MODE'):
    ic.enable()


url: str = 'https://pastebin.com/raw/pzwDD2EF'
local_file: Path = Path(__file__).parent / 'index.html'


def download(url: str, fout: Path | None = None) -> bool:
    """Donwload html file."""
    fout = fout or local_file
    if not fout.is_file():
        resp = httpx.get(url=url)
        fout.write_bytes(resp.content)
    return True


class CampionatoBrasileiro:
    """Campionato brasileiro."""

    def __init__(self, url_or_path: str, file_out: Path | None = None) -> None:
        """Init."""
        self.url_or_path: str = url_or_path
        self.fout: Path = file_out or local_file
        self.content: pd.DataFrame | None = None
        self.__scrap()

    def __scrap(self) -> None:
        """Scrap content."""
        if not self.fout.is_file():
            download(self.url_or_path, self.fout)
        self.content = pd.read_html(self.fout, encoding='utf-8')[0]
        self.content = self.content.drop(
            self.content.columns[[0, 11, 12]],
            axis=1,
        )
        self.content.columns = [
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
        self.content['STATUS'] = self.content.RANK.apply(
            lambda x: ''.join(n for n in x if not n.isdigit()),
        )
        c = count(1)
        self.content.RANK = self.content.RANK.map(lambda x: next(c))  # noqa: ARG005
        ic(self.content.head())

    def sort_by_name(self, *, reverse: bool = False) -> list:
        """Sort by name."""
        return self.content.sort_values(
            by=['CLUBE'],
            ascending=not reverse,
        ).CLUBE.tolist()

    def sort_by_point(self, *, reverse: bool = False) -> list:
        """Sort by point."""
        return self.content.sort_values(
            by=['PONTOS', 'SALDO DE GOLS', 'CLUBE'],
            ascending=not reverse,
        ).CLUBE.tolist()

    def classify(self) -> list:
        """Classificação por pontos no Campeonato brasileiro de futebol."""
        return self.sort_by_point(reverse=True)

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

    def clube(self, clube_name: str) -> int:
        """Classificação por pontos no Campeonato brasileiro de futebol."""
        return self.content[
            self.content.CLUBE.str.contains(clube_name, case=False)
        ].PONTOS.last_valid_index()


if __name__ == '__main__':
    download()
