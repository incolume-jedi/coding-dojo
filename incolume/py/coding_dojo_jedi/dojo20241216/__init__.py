"""dojo module."""

import base64
import json
from dataclasses import asdict, dataclass
from pathlib import Path

import httpx
from icecream import ic

url: str = (
    'https://www.python.org/static/community_logos/python-powered-h-50x65.png'
)


@dataclass
class ImageFile:
    """Image representation."""

    filename: str
    content: str

    def to_dict(self):
        """Return self dict."""
        return asdict(self)

    def to_json(self):
        """Return self json."""
        return json.dumps(self.to_dict())


def download_file(link: str = '', fout: Path | None = None) -> httpx.Response:
    """Donwnload files.

    link: string link for donwload file
    fout: full path for output file.
    """
    ans = httpx.get(link, follow_redirects=True)
    filename = url.split('/')[-1]
    fout = fout or filename
    fout = Path(fout)
    fout.write_bytes(ans.content)
    return ans


def dojo(**kwargs: str) -> Path:
    """Dojo solution.

    link: string link for donwload file
    fout: full path for output file.
    """
    response = download_file(**kwargs)
    result = base64.encodebytes(response.content)

    return result
