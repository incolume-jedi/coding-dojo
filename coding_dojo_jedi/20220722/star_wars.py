import requests
from pprint import pprint


resposta =[]
pagina = 1
url = 'https://swapi.dev/api/people/?page={}'

while True:
    try:
        r = requests.get(url.format(pagina))
        print(pagina, r)
        x = r.json()
        resposta += x['results']
        pagina += 1
    except KeyError:
        break

print(len(resposta))
