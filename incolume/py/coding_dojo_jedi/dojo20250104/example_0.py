"""Example 0.

Author: Lucas Turos - @lucasfturos
Description: Descobre a maior sequências de números primos no número de PI
disponível em: https://github.com/OsProgramadores/op-desafios/blob/master/desafio-11/lucasfturos/python/primos_pi.py
"""

import sys
from math import sqrt
from pathlib import Path
from typing import ClassVar

from icecream import ic


# ruff: noqa: PLR2004
class PrimesPi:
    """Class PrimesPi.

    Classe para processar e encontrar a maior
    sequência de números primos em Pi.
    """

    pi_digits = ''
    primes: ClassVar[set] = set()

    def __init__(self, filename: Path) -> None:
        """Inicializador."""
        self.filename: Path = filename

    def is_prime(self, num: int) -> bool:
        """Função para testar se é um número primo."""
        if num < 2 or num % 2 == 0:
            return False
        return all(num % i != 0 for i in range(3, int(sqrt(num)) + 1, 2))

    def generate_primes(self, limit: int) -> None:
        """Função para gerar os números primos."""
        for i in range(2, limit + 1):
            if self.is_prime(i):
                self.primes.add(i)

    def find_longest_prime_sequence(
        self,
        begin: int,
        seq: str,
        longer_seq: list[str],
    ) -> None:
        """Find_longest_prine_sequence.

        Função para encontrar a maior sequência
        de dígitos que formam números primos
        """
        char = ''
        current_sequence = ''
        num = 0
        for i in range(begin, begin + 4):
            try:
                char += self.pi_digits[i]
                num = int(char)
            except IndexError:
                break

            if num in self.primes:
                current_sequence = seq + char
                self.find_longest_prime_sequence(
                    i + 1,
                    current_sequence,
                    longer_seq,
                )

        if len(current_sequence) > len(longer_seq[0]):
            longer_seq.clear()
            longer_seq.append(current_sequence[::])

    def read_file(self) -> None:
        """Função para ler um arquivo."""
        try:
            with self.filename.open(encoding='utf-8') as file:
                self.pi_digits = file.read().strip()
            self.pi_digits = self.pi_digits.removeprefix('3.')
        except FileNotFoundError:
            ic(f'Arquivo: {self.filename.as_posix()} não encontrado.')
            sys.exit(1)

    def run(self) -> list[str]:
        """Função principal da classe.

        onde será feita leitura, busca e imprimir o resultado
        """
        longer_seq = ['']
        self.generate_primes(9973)
        self.read_file()
        for index in range(len(self.pi_digits)):
            self.find_longest_prime_sequence(index, '', longer_seq)
        return ic(longer_seq[0])


if __name__ == '__main__':
    if len(sys.argv) < 2:
        ic('Uso: python primos_pi.py caminho/do/arquivo.txt')
        sys.exit(1)

    prime_finder = PrimesPi(filename=sys.argv[1])
    prime_finder.run()
