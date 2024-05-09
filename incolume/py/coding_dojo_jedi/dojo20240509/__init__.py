"""Module dojo."""

from typing import ClassVar


class Numeros:
    """Converte numeros para romanos e arabicos."""

    romanos: ClassVar = [
        'M',
        'CM',
        'D',
        'CD',
        'C',
        'XC',
        'L',
        'XL',
        'X',
        'IX',
        'V',
        'IV',
        'I',
    ]
    arabicos: ClassVar = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

    def __init__(self):
        """Init it."""

    def from_roman(self, numero_romano: str) -> int:
        """Transforma número romanos em arábicos."""
        result = 0
        qnt = len(numero_romano)
        for idx in range(qnt):
            if idx + 1 < qnt and (
                self.arabicos[self.romanos.index(numero_romano[idx])]
                < self.arabicos[self.romanos.index(numero_romano[idx + 1])]
            ):
                result -= self.arabicos[self.romanos.index(numero_romano[idx])]
            else:
                result += self.arabicos[self.romanos.index(numero_romano[idx])]

        return result

    def to_roman(self, num: int) -> str:
        """Transforma número arábico para romano."""
        result = ''
        for idx, i in enumerate(self.arabicos):
            while num >= i:
                num = num - i
                result = result + self.romanos[idx]
        return result
