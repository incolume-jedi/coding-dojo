def get_char(num: int):
    """Retorna um Unicode do parametro em num;"""
    # Tratamento exceção
    try:
        num = int(num)
        if not (0 <= num <= 0x10FFFF):
            msg = '0 <= num <= 0x10ffff.'
            raise ValueError(msg)
    except ValueError:
        msg = 'num deve ser um número entre 0 e 0x10ffff.'
        raise ValueError(msg)

    return chr(num)
