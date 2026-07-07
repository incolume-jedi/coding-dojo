"""Core module for coding dojo."""

import contextlib
import logging
from os import getenv
from pathlib import Path

from icecream import ic
from toml import load

__author__ = '@britodfbr'

logger = logging.getLogger(__name__)

def is_debug_var_actived() -> bool:
    """Check environment variables for debug mode."""
    debug: bool = any(
        getenv(x, '').casefold() in {'1', 'true', 'on'}
        for x in ('INCOLUME_DEBUG_MODE', 'DEBUG_MODE', 'DEBUG')
    )

    logger.debug(ic(f'Var Debug Mode: {debug}'))

    return debug


def is_debug_enabled() -> bool:
    """Enable debug mode."""
    debug: bool = is_debug_var_actived()
    ic.disable()  # Disable by default

    if debug:
        ic.enable()
        logging.basicConfig(level=logging.DEBUG)
    logger.debug(ic(f'Debug mode {"enabled" if debug else "disabled"}.'))
    return debug


configfile = Path(__file__).parents[3].joinpath('pyproject.toml')
versionfile = Path(__file__).parent.joinpath('version.txt')

with contextlib.suppress(FileNotFoundError):
    versionfile.write_text(
        f'{load(configfile)["tool"]["poetry"]["version"]}\n',
    )

with contextlib.suppress(FileNotFoundError):
    versionfile.write_text(
        f'{load(configfile)["project"]["version"]}\n',
    )

__version__ = versionfile.read_text(encoding='utf-8').strip()
module_name = __name__.split('.')[0]
project = Path(__file__).parents[3].name


if __name__ == '__main__':
    is_debug_enabled()
