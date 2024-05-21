"""Module."""


def check_fizz_buzz(num: int, razao: int = 3) -> bool:
    """Check fizz buzz."""
    return num % razao == 0


def romeu_julieta(num: int) -> str:
    """FizzBuzz abrasileirado."""
    result = str(num)
    if num % 3 == 0 and num % 5 == 0:
        result = 'romeu e julieta'
    elif num % 3 == 0:
        result = 'queijo'
    elif num % 5 == 0:
        result = 'goiabada'
    return result


def fizzbuzz0(num: int) -> str:
    """Fizzbuzz."""
    return 'Fizz' * (not num % 3) + 'Buzz' * (not num % 5) or str(num)


def fizzbuzz(num: int) -> str:
    """Fizzbuzz."""
    return 'FizzBuzz'[num % -3 & 4 : 12 & 8 - (num % -5 & 4)] or str(num)
