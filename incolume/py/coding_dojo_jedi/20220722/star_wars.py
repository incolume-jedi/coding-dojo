import json
import logging
import os
from pathlib import Path
from pprint import pprint
from tempfile import gettempdir

import dotenv
import requests

dotenv.load_dotenv()
logging.basicConfig(
    level=int(os.environ.get('LOGGING-LEVEL', logging.WARNING))
)


def research(name: str = '', url: str = '', pagina=0) -> None:
    resposta = []
    personagens = {}
    name = name or 'Luke Skywalker'
    pagina = pagina or 1
    url = url or 'https://swapi.dev/api/people/?page={}'
    # cache_file = Path(__file__).parent.joinpath('personagens.json').resolve()
    cache_file = Path(gettempdir()).joinpath('20220722_personagens.json')
    logging.info(f'{cache_file=}')
    logging.info(f'{cache_file.is_file()=}')
    if not cache_file.is_file():
        while True:
            try:
                r = requests.get(url.format(pagina))
                logging.info(f'{pagina}, {r}')
                x = r.json()
                resposta += x['results']
                pagina += 1
            except KeyError:
                break
        personagens = {p.get('name'): p for p in resposta}
        with cache_file.open('w') as f:
            json.dump(personagens, f, indent=4)

        logging.info(f'{len(resposta)} registros')
    # for person in resposta:
    #     logging.info(person.get('name'))

    if not personagens:
        with cache_file.open() as f:
            personagens = json.load(f)

    logging.info(personagens)
    logging.info(personagens.get(name))

    # print(len(personagens.get(name)['films']))
    # print("* Nome: {name}\n* Altura: {height}\n* Ano de Nascimento: {birth_year}\n* Filmes: {films}\n".format(**personagens.get(name)))
    # print('''* Nome: {name}\n* Altura: {height}cm\n* Ano de nascimento: {birth_year}\n* Quantidade de filmes: {len(films)}'''.format(**personagens.get(name)))
    return personagens.get(name)


if __name__ == '__main__':
    pass
    print(research('Tion Medon'), end='\n\n')
    print(research('Luke Skywalker'), end='\n\n')
    print(research('Obi-Wan Kenobi'), end='\n\n')
