"""dojo module."""


def dojo(*args: str, **kwargs: str) -> dict[str]:
    """Dojo solution."""
    kwargs['args'] = args
    return kwargs
