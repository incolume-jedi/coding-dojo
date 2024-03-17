"""Dojo."""

import json
import logging
import os
from typing import Any

import dotenv
import requests
from incolume.py.coding_dojo_jedi.utils import genfile

dotenv.load_dotenv()
logging.basicConfig(
    level=int(os.environ.get('LOGGING-LEVEL', logging.WARNING)),
)


def research(
    name: str = '',
    url: str = '',
    pagina: int = 0,
    timeout: float = 0.5,
) -> dict[Any, Any]:
    """Research API."""
    resposta = []
    personagens = {}
    name = name or 'Luke Skywalker'
    pagina = pagina or 1
    url = url or 'https://swapi.dev/api/people/?page={}'
    cache_file = genfile().with_name('personagens-20220722.json')
    logging.info('cache_file=%s', cache_file)
    logging.info('cache_file.is_file()=%s', cache_file.is_file())
    if not cache_file.is_file():
        while True:
            try:
                r = requests.get(url.format(pagina), timeout=timeout)
                logging.info('%s, %s', pagina, r)
                x = r.json()
                resposta += x['results']
                pagina += 1
            except KeyError:
                break
        personagens = {p.get('name'): p for p in resposta}
        with cache_file.open('w') as f:
            json.dump(personagens, f, indent=4)

        logging.info('%s registros', len(resposta))
    # for person in resposta:

    if not personagens:
        with cache_file.open() as f:
            personagens = json.load(f)

    logging.info(personagens)
    logging.info(personagens.get(name))

    return personagens[name]


if __name__ == '__main__':
    print(research('Tion Medon'), end='\n\n')    # noqa: T201
    print(research('Luke Skywalker'), end='\n\n')    # noqa: T201
    print(research('Obi-Wan Kenobi'), end='\n\n')    # noqa: T201
