import json

import requests

# print(r.json())


def saudacao():

    r = requests.get('https://swapi.dev/api/people/1/')

    name = r.json()['name']
    print('Hello,', name + '!')


saudacao()
