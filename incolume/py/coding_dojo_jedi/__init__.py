"""Principal Module."""

import logging
from pathlib import Path

from toml import load

__author__ = '@britodfbr'

configfile = Path(__file__).parents[3].joinpath('pyproject.toml')
versionfile = Path(__file__).parent.joinpath('version.txt')

versionfile.write_text(
    f"{load(configfile)['tool']['poetry']['version']}\n",
)

__version__ = versionfile.read_text(encoding='utf-8').strip()

if __name__ == '__main__':
    logging.debug('%s, %s', configfile, versionfile)
    logging.debug('Vesion load: %s', __version__)
