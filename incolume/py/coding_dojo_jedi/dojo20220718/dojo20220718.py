"""Dojo."""


def get_char(num: int) -> str:
    """Retorna um Unicode do parametro em num."""
    # Tratamento exceção
    endchar: int = 0x10FFFF
    try:
        num = int(num)
        if not 0 <= num <= endchar:
            msg = '0 <= num <= 0x10ffff.'
            raise ValueError(msg)
    except ValueError as err:
        msg = 'num deve ser um número entre 0 e 0x10ffff.'
        raise ValueError(msg) from err

    return chr(num)
