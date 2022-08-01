def square(num: int):
    result = num ** (1/2)
    if num < 0:
        return False
    return  result == int(result)
