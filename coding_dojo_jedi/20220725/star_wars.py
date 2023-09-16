import requests
from pprint import pprint
import logging
import json
import dotenv
import os
from pathlib import Path
from tempfile import gettempdir


dotenv.load_dotenv()
logging.basicConfig(level=int(os.environ.get('LOGGING-LEVEL', logging.WARNING)))


def research(name: str = "", url: str = "", pagina=0) -> list[dict]:
    resposta = []
    personagens = {}
    name = name or "Luke Skywalker"
    pagina = pagina or 1
    url = url or "https://swapi.dev/api/people/?page={}"
    # cache_file = Path(__file__).parent.joinpath('personagens.json').resolve()
    cache_file = Path(gettempdir()).joinpath('personagens.json')
    logging.info(f'{cache_file=}')
    logging.info(f'{cache_file.is_file()=}')

    if cache_file.is_file():
        with cache_file.open() as f:
            personagens = json.load(f)
    elif not cache_file.is_file():
        while True:
            try:
                r = requests.get(url.format(pagina))
                sleep(5)
                logging.info(f"{pagina}, {r}")
                x = r.json()
                resposta += x["results"]
                pagina += 1
            except KeyError:
                break
        personagens = {p.get("name").casefold(): p for p in resposta}
        logging.info(f'{personagens=}')
        with cache_file.open('w') as f:
            json.dump(personagens, f, indent=4)

        logging.info(f"{len(resposta)} registros")
    # for person in resposta:
    #     logging.info(person.get('name'))

    elif not personagens:
        with cache_file.open() as f:
            personagens = json.load(f)

    logging.info(f">>> {personagens=}")
    logging.info(f">>> {personagens.get(name)=}")

    result = personagens.get(name.casefold())
    if result:
        return [result]
    else:
        return [
            personagem for key, personagem in personagens.items()
            if name.casefold() in key.split()
        ]


if __name__ == "__main__":
    pass
    print(research("Tion Medon"), end='\n\n')
    print(research("Luke Skywalker"), end='\n\n')
    print(research("Obi-Wan Kenobi"), end='\n\n')
    print(research("Skywalker"), end='\n\n')
    print(research("jinn"), end='\n\n')
