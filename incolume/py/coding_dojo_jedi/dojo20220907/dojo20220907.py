"""Dojo."""


def fizzbuzz0(num: int) -> str:
    """Calcula fizzbuzz."""
    if num % 3 == 0 and num % 5 == 0:
        return 'FizzBuzz'
    if num % 3 == 0:
        return 'Fizz'
    if num % 5 == 0:
        return 'Buzz'
    return str(num)


def fizzbuzz(num: int) -> str:
    """Calcula fizzbuzz."""
    result = str(num)
    if num % 3 == 0 and num % 5 == 0:
        result = 'FizzBuzz'
    elif num % 3 == 0:
        result = 'Fizz'
    elif num % 5 == 0:
        result = 'Buzz'
    return result


def fizzbuzz2(num: int) -> str:
    """FAIL.

    Fizz e Buzz ficam na mesma posição.
    """
    result = [str(num), 'Fizz', 'Buzz', 'FizzBuzz']
    return result[
        (num % 3 == 0) + (num % 5 == 0) + (num % 3 == 0 and num % 5 == 0)
    ]


if __name__ == '__main__':  # pragma: no cover
    from dis import dis

    dis(fizzbuzz0)
    dis(fizzbuzz)
