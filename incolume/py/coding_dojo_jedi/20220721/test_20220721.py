import requests


def saudacao():

    r = requests.get('https://swapi.dev/api/people/1/', timeout=1.5)

    name = r.json()['name']
    print('Hello,', name + '!')


saudacao()
