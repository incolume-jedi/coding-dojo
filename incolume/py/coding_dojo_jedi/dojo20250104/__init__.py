"""dojo module."""

import inspect
import logging
import tarfile
from collections.abc import Iterator
from functools import lru_cache
from pathlib import Path
from typing import Final

import filetype
import httpx
from icecream import ic

URL_TAR_FILE: Final[str] = 'https://osprogramadores.com/files/d11/pi-1M.tar.gz'
URL_RAW_FILE: Final[str] = 'https://pastebin.com/raw/Ak8TCbJk'
LOCAL_FILE: Path = Path(__file__).parent / 'pi-1M.tgz'


def download_file(
    url: str = '',
    dir_output: Path | None = None,
    fout: Path | None = None,
) -> Path:
    """Download file."""
    ic(inspect.stack()[0][3])
    dir_output = dir_output or Path()
    url = url or URL_TAR_FILE
    ic(url)
    response = httpx.get(url)
    filename = fout or dir_output / url.split('/')[-1]
    ic(filename)
    filename.parent.mkdir(exist_ok=True)
    filename.write_bytes(response.content)
    return filename


def handler_file(*, fin: Path | None = None, chunk: int = 0) -> bytes:
    """Handler file."""
    ic(inspect.stack()[0][3])
    chunk = (
        -1 if (not isinstance(chunk, int) or chunk < 0) else max(chunk + 2, 22)
    )

    fin = fin or LOCAL_FILE
    ic(fin)
    with tarfile.open(fin, mode='r:gz') as handler:
        file = handler.extractfile(handler.getnames()[0])
        if chunk == -1:
            return file.readline()
        return file.read(chunk)


def handler_stream(*, url: str = '', chunk: int = 0) -> bytes:
    """Handler stream."""
    ic(inspect.stack()[0][3])
    chunk = (
        -1 if (not isinstance(chunk, int) or chunk < 0) else max(chunk + 2, 22)
    )

    url = url or URL_RAW_FILE
    response = httpx.get(url)
    content = response.content
    if chunk == -1:
        return content
    return content[:chunk]


def iterator_handler_file(
    *,
    fin: Path | None = None,
    chunk_size: int = 1,
) -> Iterator[bytes]:
    """Iterator of bytes."""
    fin = fin or LOCAL_FILE
    kind = filetype.guess(fin)
    ic(fin)
    try:
        if kind.mime == 'application/gzip':
            with tarfile.open(fin, mode='r:gz') as handler:
                file = handler.extractfile(handler.getnames()[0])
                file.read(2)
                while char := file.read(chunk_size):
                    yield char
    except AttributeError:
        ...

    with fin.open('rb') as file:
        file.read(2)
        while char := file.read(chunk_size):
            yield char


@lru_cache
def is_prime(num: int) -> bool:
    """Check if prime number."""
    if not isinstance(num, int) or num <= 1 or (num > 2 and num % 2 == 0):  # noqa: PLR2004
        return False
    return all(num % n != 0 for n in range(2, num // 2 + 1))


def find_longest_prime_sequence(
    begin: int,
    seq: str,
    longer_seq: list[str | bytes] | None = None,
) -> str:
    """Find Longest Prime Sequence.

    Função para encontrar a maior sequência de dígitos
     que formam números primos.
    """
    longer_seq = longer_seq or ['']
    primes = [x for x in range(10**4, -1, -1) if is_prime(x)]
    char: str = ''
    current_sequence: str = ''
    pi_digits: str = ''
    num: int = 0
    for i in range(begin, begin + 4):
        try:
            char += pi_digits[i]
            num = int(char)
        except IndexError:
            break

        if num in primes:
            current_sequence = seq + char
            find_longest_prime_sequence(i + 1, current_sequence, longer_seq)

    if len(current_sequence) > len(longer_seq[0]):
        longer_seq.clear()
        longer_seq.append(current_sequence[::])

    return ''.join(longer_seq)


def dojo(**kwargs: dict[str, Any]) -> dict[str]:
    """Dojo solution."""
    logging.info(ic(inspect.stack()[0][3], kwargs))
    fin = kwargs.get('fin')
    chunk = kwargs.get('chunk')
    logging.debug(ic(fin, chunk))
    result = {}
    count: int = 0
    primes = [x for x in range(10**4, -1, -1) if is_prime(x)]
    sequence = iterator_handler_file(fin=fin)

    while 1:
        num = int(next(sequence))
        if count > chunk:
            break

        logging.debug(ic(count, num))

        count += 1

    return primes
