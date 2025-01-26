"""Example 1.

autor: James Stuart
disponivel em: https://github.com/OsProgramadores/op-desafios/blob/master/desafio-11/JamesStewart-314/python/solution.py
"""

import math
import sys
from collections import defaultdict
from itertools import count
from pathlib import Path

from icecream import ic


def get_set_primes(num_digits: int, upper_limit: int) -> set[str]:
    """Get set primes."""
    primes_set: set[str] = set()
    primes_set.update('2'.zfill(z_qty) for z_qty in range(1, num_digits + 1))
    sieve_dict: dict[int, int] = {}
    num_counter: count = count(start=3, step=2)

    for current_num in num_counter:
        if current_num >= upper_limit:
            break
        if current_num not in sieve_dict:
            sieve_dict[current_num * current_num] = current_num
            current_num: str = str(current_num)  # noqa: PLW2901
            primes_set.update(
                current_num.zfill(z_qty) for z_qty in range(1, num_digits + 1)
            )
        else:
            current_num_key: int = current_num + (sieve_dict[current_num] << 1)
            while sieve_dict.get(current_num_key):
                current_num_key += sieve_dict[current_num] << 1
            sieve_dict[current_num_key] = sieve_dict[current_num]
            del sieve_dict[current_num]

    return primes_set


def ic_biggest_seq(file_path: Path, upper_limit: int = 10**4) -> str:  # noqa: C901
    """Print biggest sequense."""
    try:
        with file_path.open() as fl:
            pi_digits: str = (t := fl.readline().rstrip())[t.index('.') + 1 :]
    except FileNotFoundError as error:
        msg = f"Error: Could open file '{file_path}'."
        raise ValueError(msg) from error
    except ValueError:
        pi_digits: str = t

    prime_numbers: set[str] = get_set_primes(
        int(math.log10(upper_limit)) + 1,
        upper_limit,
    )

    prim_seq: defaultdict[int, str] = defaultdict(str)
    for idx in range(len(pi_digits)):
        current_num: str = ''
        for qty in range(4):
            try:
                current_num += pi_digits[(s := idx + qty)]
            except IndexError:
                break
            if current_num not in prime_numbers:
                continue
            if len(prim_seq[(t := s + 1)]) < len(prim_seq[idx]) + len(
                current_num,
            ):
                prim_seq[t] = prim_seq[idx] + current_num

    return ic(max(prim_seq.values(), key=len, default=''))


if __name__ == '__main__':
    pi_digits_file_path: Path = Path(__file__) / 'pi-1M.txt'

    try:
        ic_biggest_seq(pi_digits_file_path)
    except ValueError:
        ic(sys.exc_info())
