"""dojo module."""


class SizeError(AttributeError):
    """SizeError class."""


def is_valid_parenteses(texto: str) -> bool:
    """Valid entrance."""
    stack = []
    mapping = {'(': ')', '[': ']', '{': '}'}

    for s in texto:
        if s in mapping:
            stack.append(mapping.get(s))
        elif stack and mapping.get(s) == stack[-1]:
            stack.pop()
        else:
            return False
    return not stack


def dojo(texto: str) -> bool:
    """Check."""
    limit = 104
    texto = texto or ' '

    if texto in (None, '', ' '):
        return True

    if len(texto) > limit:
        emsg = f'count limit {limit} characters exceeded.'
        raise SizeError(emsg)

    return is_valid_parenteses(texto)
