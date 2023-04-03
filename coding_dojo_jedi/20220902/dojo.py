import logging
import inspect

MOEDAS = [1.00, .5, .25, .10, .05, .01]
CEDULAS = [200, 100, 50, 20, 10, 5, 2]
logging.basicConfig(level=logging.DEBUG)


def calcular(valor, base_monetaria):
    logging.debug(f'{inspect.stack()[0][3]}({valor}, {base_monetaria})')
    result = [0] * len(base_monetaria)
    for i, base in enumerate(base_monetaria):
        result[i] = int(valor / base)
        valor = round(valor % base, 2)
        logging.debug(f'{valor}; {result[i]}: {base}')
    logging.debug(f'{valor}, {result}')
    return valor, result


def trocar_dinheiro(valor: float) -> tuple[list, list]:
    """Calcula o menor número de notas e moedas possíveis
    no qual o valor pode ser decomposto.
    """
    valor, cedulas = calcular(valor, CEDULAS)
    valor, moedas = calcular(valor, MOEDAS)
    # if valor:
    #     raise ValueError(f'{valor}')
    return cedulas, moedas


if __name__ == '__main__':    # pragma: no cover
    trocar_dinheiro(386.96)
    trocar_dinheiro(576.73)
    trocar_dinheiro(6)