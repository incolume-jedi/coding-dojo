"""dojo module."""

from __future__ import annotations

from icecream import ic


def dojo(*args: str, **kwargs: str) -> dict[str]:
    """Dojo solution."""
    kwargs['args'] = args
    return kwargs


def main():
    """Main function."""
    ic('Hello from dojo20260620!')


if __name__ == '__main__':
    main()
