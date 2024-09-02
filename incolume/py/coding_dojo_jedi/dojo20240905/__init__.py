"""dojo module."""

import logging


def check_luhn0(card_num):
    """Dojo solution.

    Python3 program to implement
    Luhn algorithm
    Returns true if given card
    number is valid

    This code is contributed by rutvik_56
    """
    q_digits = len(card_num)
    n_sum = 0
    is_second = False

    for i in range(q_digits - 1, -1, -1):
        d = ord(card_num[i]) - ord('0')

        if is_second is True:
            d = d * 2

        n_sum += d // 10
        n_sum += d % 10
        is_second = not is_second
        if n_sum % 10 == 0:
            return True
    return False


def check_luhn(card_num: int | str) -> bool:
    """Dojo solution."""
    card_num = str(card_num)
    q_digits = len(card_num)
    n_sum = 0
    is_second = False

    for i in range(q_digits - 1, -1, -1):
        d = ord(card_num[i]) - ord('0')

        if is_second:
            d = d * 2

        n_sum += d // 10
        n_sum += d % 10
        is_second = not is_second
    return n_sum % 10 == 0


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    card_num = '79927398713'
    msg = f'This is {"" if check_luhn(card_num) else "not"} a valid card'
    logging.debug(msg)
