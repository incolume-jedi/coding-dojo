"""dojo module."""

import asyncio
import http
import os
import urllib
import urllib.parse
from collections.abc import Coroutine
from pathlib import Path

import httpx
import nest_asyncio
from icecream import ic

# permite chamadas async para jupyter
nest_asyncio.apply()

ic.disable()
if os.getenv('DEBUG_MODE'):
    ic.enable()
# ruff: noqa: ERA001

URLS = [
    'https://bd.camara.leg.br/bd/bitstream/handle/bdcamara/18319/colleccao_leis_1808_parte1.pdf?sequence=4&isAllowed=y',
    'https://bd.camara.leg.br/bd/bitstream/handle/bdcamara/18319/colleccao_leis_1808_parte2.pdf?sequence=5',
    'https://bd.camara.leg.br/bd/bitstream/handle/bdcamara/18321/colleccao_leis_1809_parte1.pdf?sequence=1',
    'https://bd.camara.leg.br/bd/bitstream/handle/bdcamara/18325/colleccao_leis_1810_parte1.pdf?sequence=1',
    'https://bd.camara.leg.br/bd/bitstream/handle/bdcamara/18323/colleccao_leis_1811_parte1.pdf?sequence=1',
    'https://bd.camara.leg.br/bd/bitstream/handle/bdcamara/18322/colleccao_leis_1812_parte1.pdf?sequence=1',
    'https://bd.camara.leg.br/bd/bitstream/handle/bdcamara/18324/colleccao_leis_1813_parte1.pdf?sequence=1',
    'https://bd.camara.leg.br/bd/bitstream/handle/bdcamara/18326/colleccao_leis_1814_parte1.pdf?sequence=1',
    'https://bd.camara.leg.br/bd/bitstream/handle/bdcamara/18329/colleccao_leis_1815_parte1.pdf?sequence=1',
    'https://bd.camara.leg.br/bd/bitstream/handle/bdcamara/18330/colleccao_leis_1816_parte1.pdf?sequence=1',
    'https://bd.camara.leg.br/bd/bitstream/handle/bdcamara/18331/colleccao_leis_1817_parte1.pdf?sequence=1',
    'https://bd.camara.leg.br/bd/bitstream/handle/bdcamara/18332/colleccao_leis_1818_parte1.pdf?sequence=1',
    'https://bd.camara.leg.br/bd/bitstream/handle/bdcamara/18333/colleccao_leis_1819_parte1.pdf?sequence=1',
    'https://bd.camara.leg.br/bd/bitstream/handle/bdcamara/18335/colleccao_leis_1820_parte1.pdf?sequence=1',
    'https://bd.camara.leg.br/bd/bitstream/handle/bdcamara/18321/colleccao_leis_1809_parte2.pdf?sequence=2',
    'https://bd.camara.leg.br/bd/bitstream/handle/bdcamara/18325/colleccao_leis_1810_parte2.pdf?sequence=2',
    'https://bd.camara.leg.br/bd/bitstream/handle/bdcamara/18323/colleccao_leis_1811_parte2.pdf?sequence=2',
    'https://bd.camara.leg.br/bd/bitstream/handle/bdcamara/18322/colleccao_leis_1812_parte2.pdf?sequence=2',
    'https://bd.camara.leg.br/bd/bitstream/handle/bdcamara/18324/colleccao_leis_1813_parte2.pdf?sequence=2',
    'https://bd.camara.leg.br/bd/bitstream/handle/bdcamara/18326/colleccao_leis_1814_parte2.pdf?sequence=2',
    'https://bd.camara.leg.br/bd/bitstream/handle/bdcamara/18329/colleccao_leis_1815_parte2.pdf?sequence=2',
    'https://bd.camara.leg.br/bd/bitstream/handle/bdcamara/18330/colleccao_leis_1816_parte2.pdf?sequence=2',
    'https://bd.camara.leg.br/bd/bitstream/handle/bdcamara/18331/colleccao_leis_1817_parte2.pdf?sequence=2',
    'https://bd.camara.leg.br/bd/bitstream/handle/bdcamara/18332/colleccao_leis_1818_parte2.pdf?sequence=2',
    'https://bd.camara.leg.br/bd/bitstream/handle/bdcamara/18333/colleccao_leis_1819_parte2.pdf?sequence=2',
    'https://bd.camara.leg.br/bd/bitstream/handle/bdcamara/18335/colleccao_leis_1820_parte2.pdf?sequence=2',
]


async def async_stream(url: str, output_path: str = '') -> Path:
    """Async Stream download."""
    output_path = Path(output_path) if output_path else Path('files')
    output_path.mkdir(exist_ok=True)
    file = output_path / Path(urllib.parse.urlsplit(url).path).name

    with file.open('wb') as f:
        async with httpx.AsyncClient() as client:
            async with client.stream('GET', url) as r:
                async for chunk in r.aiter_bytes():
                    f.write(chunk)
    return file


def sync_download(url: str, output_path: str = '') -> Path:
    """Dojo solution."""
    output_path = Path(output_path) if output_path else Path('files')
    output_path.mkdir(exist_ok=True)
    file = output_path / Path(urllib.parse.urlsplit(url).path).name
    resp = httpx.get(url)

    ic(resp.status_code)
    ic(type(resp))
    ic(resp.url)
    ic(resp.next_request)
    ic(resp.next_request.url)
    ic(resp.headers)
    ic(resp.headers['location'])

    if resp.status_code == http.HTTPStatus.FOUND.value:
        resp = httpx.get(resp.next_request.url)
    file.write_bytes(resp.content)
    ic(file.absolute())
    return file


async def stream_download(url: str, output_path: Path | None = None) -> Path:
    """Dojo solution."""
    output_path = output_path or Path('files')
    output_path.mkdir(exist_ok=True)
    file = output_path / Path(urllib.parse.urlsplit(url).path).name

    with file.open('wb') as f:
        async with httpx.AsyncClient() as client:
            async with client.stream('GET', url, follow_redirects=True) as r:
                ic(r.is_redirect)
                ic(r.headers)
                async for chunk in r.aiter_bytes():
                    f.write(chunk)

    ic(file.absolute())
    return file


async def async_download(
    *urls: str,
    output_path: Path | None = None,
) -> dict[str]:
    """Dojo solution."""
    output_path = output_path or Path('files')
    output_path.mkdir(exist_ok=True)
    # file = output / Path(urllib.parse.urlsplit(url).path).name

    async def get_async(url: str) -> Coroutine:
        """Get async."""
        async with httpx.AsyncClient() as client:
            return await client.get(url, follow_redirects=True, timeout=3)

    async def launch():
        """Launch async."""
        responses = await asyncio.gather(*map(get_async, urls))
        datas = [resp.content async for resp in responses]

        for data in datas:
            ic(data)

    asyncio.run(launch())


def dojo():
    """Dojo."""
