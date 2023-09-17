def cavaleiro0(balas: int, dragoes: int)-> bool:
    if (balas // 2) >= dragoes:
        return True
    else:
        return False


def cavaleiro1(balas: int, dragoes: int)-> bool:
    if (balas // 2) >= dragoes:
        return True
    return False


def cavaleiro(balas: int, dragoes: int)-> bool:
    return (balas // 2) >= dragoes


