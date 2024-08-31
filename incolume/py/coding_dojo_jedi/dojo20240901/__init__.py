"""Dojo module."""


def dojo(num: int) -> str:
    """Dojo implementation."""
    num_map = {
        0: 'zero',
        1: 'um',
        2: 'dois',
        3: 'três',
        4: 'quatro',
        5: 'cinco',
        6: 'seis',
        7: 'sete',
        8: 'oito',
        9: 'nove',
        10: 'dez',
        11: 'onze',
        12: 'doze',
        13: 'treze',
        14: 'quatorze',
        15: 'quinze',
        16: 'dezesseis',
        17: 'dezessete',
        18: 'dezoito',
        19: 'dezenove',
        20: 'vinte',
        30: 'trinta',
        40: 'quarenta',
        50: 'cinquênta',
        60: 'sessenta',
        70: 'setenta',
        80: 'oitenta',
        90: 'noventa',
        100: 'cem',
        200: 'duzentos',
        300: 'trezentos',
        400: 'quatrocentos',
        500: 'quinhentos',
        600: 'seiscentos',
        700: 'setecentos',
        800: 'oitocentos',
        900: 'novecentos',
        1000: 'mil',
        2000: 'dois mil',
        3000: 'três mil',
        4000: 'quatro mil',
        5000: 'cinco mil',
        6000: 'seis mil',
        7000: 'sete mil',
        8000: 'oito mil',
        9000: 'nove mil',
        10000: 'dez mil',
    }
    result = num_map.get(num)
    if not result:
        result = ' e '.join(
            [
                num_map.get(int(x) * 10**idx)
                for idx, x in enumerate(str(num)[::-1])
                if int(x) > 0
            ][::-1],
        )

    return result
