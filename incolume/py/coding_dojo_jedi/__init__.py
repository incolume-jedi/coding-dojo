"""Principal Module."""

from icecream import ic
from incolume.py.coding_dojo_jedi.core import (
    __author__,
    __version__,
    configfile,
    is_debug_enabled,
    logger,
    module_name,
    project,
    versionfile,
)

__all__ = [
    '__author__',
    '__version__',
    'configfile',
    'is_debug_enabled',
    'logger',
    'module_name',
    'project',
    'versionfile',
]

is_debug_enabled()

if __name__ == '__main__':
    logger.debug(ic('%s, %s', configfile, versionfile))
    logger.debug(ic('Version load: %s', __version__))
    logger.debug(ic('Project: %s', project))
    logger.debug(ic('Module name: %s', module_name))
