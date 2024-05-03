"""Dojo."""


def cavaleiro0(balas: int, dragoes: int) -> bool:
    """Calcula vida cavaleiro/dragão."""
    return balas // 2 >= dragoes


def cavaleiro1(balas: int, dragoes: int) -> bool:
    """Calcula vida cavaleiro/dragão."""
    if (balas // 2) >= dragoes:  # noqa: SIM103
        return True
    return False


def cavaleiro(balas: int, dragoes: int) -> bool:
    """Calcula vida cavaleiro/dragão."""
    return (balas // 2) >= dragoes
