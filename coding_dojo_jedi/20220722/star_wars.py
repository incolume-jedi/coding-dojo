import requests
from pprint import pprint
import logging
import json
import dotenv
import os


dotenv.load_dotenv()
logging.basicConfig(level=int(os.environ.get('LOGGING-LEVEL', logging.INFO)))


def research(name: str = "", url: str = "", pagina=0) -> None:
    resposta = []
    name = name or "Luke Skywalker"
    pagina = pagina or 1
    url = url or "https://swapi.dev/api/people/?page={}"

    if not resposta:
        while True:
            try:
                r = requests.get(url.format(pagina))
                logging.info(f"{pagina}, {r}")
                x = r.json()
                resposta += x["results"]
                pagina += 1
            except KeyError:
                break
    logging.info(f"{len(resposta)} registros")
    # for person in resposta:
    #     logging.info(person.get('name'))

    personagens = {p.get("name"): p for p in resposta}
    logging.info(personagens)
    logging.info(personagens.get(name))
    print("* Nome: {name}\n* Altura: {height}\n* Ano de Nascimento: {birth_year}\n* Filmes: {films}\n".format(**personagens.get(name)))
    # print('''* Nome: {name}\n* Altura: {height}cm\n* Ano de nascimento: {birth_year}\n* Quantidade de filmes: {len(films)}'''.format(**personagens.get(name)))


if __name__ == "__main__":
    # research("Tion Medon")
    research("Luke Skywalker")
