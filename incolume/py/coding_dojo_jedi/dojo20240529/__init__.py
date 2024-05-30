"""Module."""

import logging

# !/usr/bin/env python
# -*- coding: utf-8 -*-
import tarfile
from pathlib import Path


def create_tar_gz(filename: Path | None = None) -> None:
    """Example to create tar.gz file."""
    filename = filename or Path('file.tar.gz')
    filename.cwd()
    with tarfile.open(filename, 'w:gz') as f:
        [f.add(file) for file in Path(__file__).parent.rglob('*.md')]
        logging.info(f.getnames())


def read_tar_gz(filename: Path | None = None) -> str:
    """Example to read tar.gz file."""
    filename = filename or Path(__file__).parent / 'pi-1M.tar.gz'
    with tarfile.open(filename, mode='r:gz') as f:
        return f.getnames()


def info_tar_gz(filename: Path | None = None) -> None:
    """Info tar.gz."""
    filename = filename or Path(__file__).parent / 'pi-1M.tar.gz'

    with tarfile.open(filename, 'r:gz') as tar_handler:
        for tarinfo in tar_handler:
            print(  # noqa: T201
                tarinfo.name,
                'is',
                tarinfo.size,
                'bytes in size and is ',
                end='',
            )
            if tarinfo.isreg():
                print('a regular file.')  # noqa: T201
            elif tarinfo.isdir():
                print('a directory.')  # noqa: T201
            else:
                print('something else.')  # noqa: T201


def get_content_tar_gz(filename: Path | None = None) -> str:
    """Get content."""
    filename = filename or Path(__file__).parent / 'pi-1M.tar.gz'
    with tarfile.open(filename, mode='r:gz') as handler:
        file = handler.extractfile(handler.getnames()[0])
        with open(file.name, mode='rb') as outfile:
            return outfile.name
