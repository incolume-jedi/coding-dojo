"""dojo module."""

from __future__ import annotations

from pathlib import Path
from tempfile import NamedTemporaryFile

import qrcode
from icecream import ic


def gen_qrcode(url: str = '', flout: Path | str = '') -> Path:
    """Gerador de QR code."""
    # Cria o QR code com a url informada ou com a url padrão
    url = url or 'http://brito.blog.incolume.com.br'
    imagem = qrcode.make(url)

    flout: Path = (
        Path(flout)
        if flout
        else Path(NamedTemporaryFile(prefix='qrcode_', suffix='.png').name)
    )

    # Salva o arquivo gerado
    imagem.save(flout)

    return flout


def dojo(**kwargs: str) -> Path:
    """Dojo solution."""
    return gen_qrcode(**kwargs)

def main():
    """Main function."""
    ic('Hello from dojo20260622!')
    ic(gen_qrcode())


if __name__ == '__main__':
    main()
