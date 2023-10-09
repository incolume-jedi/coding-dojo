"""Dojo."""

import json
import logging
import os
from pathlib import Path
from tempfile import gettempdir

import dotenv
import requests
from fuzzywuzzy import fuzz  # type: ignore

dotenv.load_dotenv()
logging.basicConfig(
    level=int(os.environ.get('LOGGING-LEVEL', logging.WARNING)),
)


def research(
    name: str = '',
    url: str = '',
    pagina: int = 0,
    timeout: float = 9,
) -> list[dict]:
    """Return result of research."""
    resposta = []
    personagens = {}
    name = name or 'Luke Skywalker'
    pagina = pagina or 1
    url = url or 'https://swapi.dev/api/people/?page={}'
    cache_file = Path(gettempdir()).joinpath('20220727_personagens.json')
    logging.info('%s', cache_file)
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
        personagens = {p.get('name').casefold(): p for p in resposta}
        logging.info('personagens=%s', personagens)
        with cache_file.open('w') as f:
            json.dump(personagens, f, indent=4)

        logging.info('%s registros', len(resposta))
    # for person in resposta:

    if not personagens:
        with cache_file.open() as f:
            personagens = json.load(f)

    logging.info('>>> personagens=%s', personagens)
    logging.info('>>> personagens.get(name)=%s', personagens.get(name))

    result = personagens.get(name.casefold())
    if result:
        return [result]

    result = [
        personagem
        for key, personagem in personagens.items()
        if name.casefold() in key.split()
    ]
    if result:
        return result

    return [
        personagem.get('name')
        for key, personagem in personagens.items()
        if fuzz.partial_ratio(name.casefold(), key) > 75
    ]


if __name__ == '__main__':
    print(research('Tion Medon'), end='\n\n')
    print(research('Luke Skywalker'), end='\n\n')
    print(research('Obi-Wan Kenobi'), end='\n\n')
