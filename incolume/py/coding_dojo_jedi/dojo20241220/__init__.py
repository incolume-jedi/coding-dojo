"""dojo module."""

import base64
import json
from pathlib import Path

import httpx
import incolume.py.coding_dojo_jedi.dojo20241216 as dojo147
from icecream import ic


def download_file(
    link: str = '',
    fout: Path | None = None,
) -> dojo147.ImageFile:
    """Donwnload files.

    link: string link for donwload file
    fout: full path for output file.
    """
    ans = httpx.get(link, follow_redirects=True)
    filename = dojo147.url.split('/')[-1]
    fout = filename or fout
    fout = Path(fout)
    b64 = base64.b64encode(ans.content).decode()
    return dojo147.ImageFile(filename=fout.as_posix(), content=b64)


def write_json(**kwargs: str) -> Path:
    """Write a json file.

    link: string link for donwload file
    fout: full path for output file.
    """
    obj_img = download_file(**kwargs)
    ic(obj_img)

    json_fout = Path(obj_img.filename).with_suffix('.json')
    with json_fout.open('w') as f:
        json.dump(obj_img.to_dict(), f)

    return json_fout


def recover_image(**kwargs: str) -> Path:
    """Dojo solution.

    json_file: filename for json file.
    """
    json_file = Path(kwargs.get('json_file'))
    with json_file.open() as f:
        result = json.load(f)
    obj_img = dojo147.ImageFile(**result)
    img_file = Path(obj_img.filename)
    img_file.write_bytes(base64.b64decode(obj_img.content.encode()))
    return img_file
