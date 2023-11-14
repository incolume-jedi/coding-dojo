"""Dojo Notas e Moedas POO."""
import inspect
import logging


class TrocaNotas:
    """Classe troca de notas."""

    def __init__(
        self: 'TrocaNotas',
        cedulas: list[float] | None = None,
        moedas: list[float] | None = None,
    ) -> None:
        """Class Init."""
        self.cedulas = cedulas or [200, 100, 50, 20, 10, 5, 2]
        self.moedas = moedas or [1.00, 0.5, 0.25, 0.10, 0.05, 0.01]

    def calcular(
        self: 'TrocaNotas',
        valor: float,
        base_monetaria: list,
    ) -> tuple:
        """Calculadora de notas."""
        logging.info(
            'cedulas default: %s, moedas default: %s',
            self.cedulas,
            self.moedas,
        )
        logging.debug(
            '%s(%s, %s)',
            inspect.stack()[0][3],
            valor,
            base_monetaria,
        )
        result = [0] * len(base_monetaria)
        for i, base in enumerate(base_monetaria):
            result[i] = int(valor / base)
            valor = round(valor % base, 2)
            logging.debug('%s %s %s', valor, result[i], base)
        logging.debug('%s, %s', valor, result)
        return valor, result

    def trocar(self: 'TrocaNotas', valor: float) -> tuple[list[float], ...]:
        """Calcula o menor número de notas e moedas possíveis."""
        valor, cedulas = self.calcular(valor, self.cedulas)
        valor, moedas = self.calcular(valor, self.moedas)
        return cedulas, moedas
