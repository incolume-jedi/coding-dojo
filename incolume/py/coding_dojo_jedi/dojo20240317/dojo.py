"""Dojo realizado em 17 Mar 2024."""

from dataclasses import dataclass, field
from math import ceil

__author__ = '@britodfbr'  # pragma: no cover


def perimeter(matriz: list[list, ...]) -> int:
    """Perimeter for matrix."""
    limits = 2, 100

    if len(matriz) == 0:
        return 0

    n, m = len(matriz), len(matriz[0])

    if n < limits[0]:
        raise ValueError

    if m > limits[-1]:
        raise ValueError

    perim = sum(matriz[0][1:-1]) + sum(matriz[-1][1:-1])

    for i in range(n):
        perim += matriz[i][0] + matriz[i][-1]

    return perim


@dataclass
class RecipienteTinta:
    """Recipiente tinta."""

    volume: float
    valor: float


@dataclass
class Orcamento:
    """Orçamento de tintas."""

    area: float
    rendimento: float = 6
    folga: float = field(repr=False, default=1.1)
    litros: float = 0
    litros_total: float = field(init=False)
    latas: int = 0
    galon: int = 0

    def __post_init__(self):
        """Post init."""
        self.litros = self.area / self.rendimento
        self.litros_total = self.litros * self.folga

    def calc_vol_simples(self, capacidade: float):
        """Calcula volume de latas."""
        return ceil(self.litros_total * self.folga / capacidade)

    def calc_volume(self):
        """Calcula volume de latas."""
        result, resto = 0, 0


def qlatas(area: float, recipiente: list[RecipienteTinta] | None = None):
    """Calcula quantia de latas."""
    recipiente = recipiente or [
        RecipienteTinta(3.6, 25),
        RecipienteTinta(18, 80),
    ]
    orc = Orcamento(area)

    return (
        f'Area: {area} m2;'
        f' Galão(ões): {orc.calc_vol_simples(recipiente[0].volume)}'
        f' ({recipiente[0].volume})L'
        f' x R${recipiente[0].valor}'
        f' = R$ {
            orc.calc_vol_simples(recipiente[0].volume) * recipiente[0].valor
        };'
        f' Lata(s): {orc.calc_vol_simples(recipiente[1].volume)}'
        f' ({recipiente[1].volume})L'
        f' x R${recipiente[1].valor}'
        f' = R$ {
            orc.calc_vol_simples(recipiente[1].volume) * recipiente[1].valor
        }'
    )
