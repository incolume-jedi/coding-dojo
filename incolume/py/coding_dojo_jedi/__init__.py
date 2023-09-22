"""Principal Module."""
import logging
from pathlib import Path

from tomli import load

__author__ = '@britodfbr'

configfile = Path(__file__).parents[3].joinpath('pyproject.toml')
versionfile = Path(__file__).parent.joinpath('version.txt')

with configfile.open('rb') as file:
    versionfile.write_text(
        f"{load(file)['tool']['poetry']['version']}\n",
        encoding='utf-8',
    )

__version__ = versionfile.read_text(encoding='utf-8').strip()

if __name__ == '__main__':
    logging.debug('%s, %s', configfile, versionfile)
    logging.debug('Vesion load: %s', __version__)
