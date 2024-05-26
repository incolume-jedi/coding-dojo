"""Module dojo."""

import logging
from http import HTTPStatus
from os import environ
from pathlib import Path

import deepl
import httpx
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent / '.env')
url_api = 'https://api-free.deepl.com/v2/translate'


def translate_deepl_api(text: str, lang: str = 'EN', url: str = '') -> dict:
    """Translate with deepl API."""
    url = url or url_api
    header: dict = {
        'Content-Type': 'application/json',
        'Authorization': f'DeepL-Auth-Key {environ.get("DEEPL_API_KEY")}',
    }
    data: dict = {
        'text': [text],
        'target_lang': lang,
    }
    resp = httpx.post(url, headers=header, json=data)
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
    r = translate_deepl_api('boa noite', lang='FR')
    logging.debug(r)
    s = translate_deepl('boa noite', 'IT')
    logging.debug(s)


if __name__ == '__main__':
    run()
