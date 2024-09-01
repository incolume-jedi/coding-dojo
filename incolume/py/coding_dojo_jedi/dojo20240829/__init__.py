"""dojo module."""

import datetime as dt
from dataclasses import asdict, dataclass, field


@dataclass
class Pessoa:
    """Pessoa class."""

    full_name: str
    born_date: dt.datetime
    city: str
    first_name: str = field(default='', init=False)
    last_name: str = field(default='', init=False)

    def __post_init__(self):
        """Post init."""
        self.first_name = self.full_name.split()[0]
        self.last_name = self.full_name.split()[-1]

    def asdict(self):
        """As dict self."""
        return asdict(self)


def dojo0(pessoa: Pessoa) -> str:
    """Dojo solution."""
    return (
        'Meu nome é "{first_name}"'
        ' nascido em "{born_date:%A %d de %B do ano %Y}"'
        ' na cidade de "{city}"'
    ).format(
        **pessoa.asdict(),
    )


def dojo(pessoa: Pessoa) -> str:
    """Dojo solution."""
    return (
        'Meu nome é "{first_name}"'
        ' nascido em "{born_date:%A %d de %B do ano %Y}"'
        ' na cidade de "{city}"'
    ).format_map(
        pessoa.asdict(),
    )
