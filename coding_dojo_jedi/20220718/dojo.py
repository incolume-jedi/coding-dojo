
def get_char(num: int):
    """Retorna um Unicode do parametro em num;"""

    # Tratamento exceção
    try:
        num = int(num)
        if not (0 <= num <= 0x10ffff):
            raise ValueError('0 <= num <= 0x10ffff.')
    except ValueError:
        raise ValueError('num deve ser um número entre 0 e 0x10ffff.')

    return chr(num)
