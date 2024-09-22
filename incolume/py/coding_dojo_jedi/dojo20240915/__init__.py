"""dojo module."""


class SizeError(AttributeError):
    """SizeError class."""


def is_valid_parenteses(texto: str) -> bool:
    """Valid entrance."""
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}

    for s in texto:
        if s in mapping and stack and stack[-1] == mapping.get(s):
            stack.pop()
        elif s in [*mapping, *mapping.values()]:
            stack.append(s)

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
