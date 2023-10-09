"""Dojo."""
import json
import logging
import os
from pathlib import Path
from tempfile import gettempdir

import dotenv
import requests

dotenv.load_dotenv()
logging.basicConfig(
    level=int(os.environ.get('LOGGING-LEVEL', logging.WARNING)),
)


def research(
    name: str = '',
    url: str = '',
    pagina=0,
    timeout: float = 9,
) -> list[dict]:
    """Pesquisa na API."""
    resposta = []
    personagens = {}
    name = name or 'Luke Skywalker'
    pagina = pagina or 1
    url = url or 'https://swapi.dev/api/people/?page={}'
    cache_file = Path(gettempdir()).joinpath('20220725_personagens.json')
    logging.info('cache_file=%s', cache_file)
    logging.info('cache_file.is_file()=%s', cache_file.is_file())
    if not cache_file.is_file():
        while True:
            try:
                r = requests.get(url.format(pagina), timeout=timeout)
                logging.info('%s %s', pagina, r)
                x = r.json()
                resposta += x['results']
                pagina += 1
            except KeyError:
                break
        personagens = {p.get('name').casefold(): p for p in resposta}
        logging.info('personagens=%s', personagens)
        with cache_file.open('w') as f:
            json.dump(personagens, f, indent=4)

        logging.info('%d registros', len(resposta))
    # for person in resposta:

    if not personagens:
        with cache_file.open() as f:
            personagens = json.load(f)

    logging.info('>>> %s', personagens)
    logging.info('>>> personagem: %s', personagens.get(name))

    result = personagens.get(name.casefold())
    if result:
        return [result]

    return [
        personagem
        for key, personagem in personagens.items()
        if name.casefold() in key.split()
    ]


if __name__ == '__main__':
    print(research('Tion Medon'), end='\n\n')
    print(research('Luke Skywalker'), end='\n\n')
    print(research('Obi-Wan Kenobi'), end='\n\n')
