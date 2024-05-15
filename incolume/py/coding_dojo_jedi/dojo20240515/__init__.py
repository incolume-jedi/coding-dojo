"""Module dojo."""

import logging
from http import HTTPStatus
from os import environ
from pathlib import Path

import deepl
import httpx
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent / '.env')


def translate_deepl0(text: str, lang: str = 'EN') -> dict:
    """Translate with deepl API."""
    header: dict = {
        'Content-Type': 'application/json',
        'Authorization': f'DeepL-Auth-Key {environ.get("DEEPL_API_KEY")}',
    }
    data: dict = {
        'text': [text],
        'target_lang': lang,
    }
    resp = httpx.post('https://api-free.deepl.com', headers=header, data=data)
    if resp.status_code == HTTPStatus.OK:
        return resp.json()
    return {}


def translate_deepl(text: str, lang: str = 'EN-US') -> dict:
    """Translate with deepl API."""
    translator = deepl.Translator(environ.get('DEEPL_API_KEY'))

    result = translator.translate_text(text=text, target_lang=lang)
    return result.text


def run():
    """Run it."""
    s = translate_deepl('Boa Noite', 'IT')
    logging.degub(s)


if __name__ == '__main__':
    run()
