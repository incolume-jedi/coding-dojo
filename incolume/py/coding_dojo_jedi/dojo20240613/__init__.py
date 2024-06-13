"""dojo module."""

from __future__ import annotations

from pathlib import Path

import pandas as pd
from faker import Faker
from icecream import ic
import datetime as dt
import random
import secrets

Faker.seed(1061)
fake = Faker('pt_BR')


def data_fake():
    """Gen data fake for XLSX files."""
    return (
        (name := f'{fake.first_name()} {fake.last_name()} {fake.last_name()}'),
        fake.cpf(),
        f'{fake.slug(name)}@correios.com.br',
    )


def generate_dataframe(count: int = 0) -> pd.DataFrame:
    """Generate dataframe."""
    count = count or 10
    title = 'nome cpf email'.split()
    users = (data_fake() for _ in range(count))
    df0 = pd.DataFrame(users, columns=title)
    ic(df0)
    return df0


def write_xlsx(data: pd.DataFrame, filename: Path | None = None) -> bool:
    """Write xlsx file."""
    filename = filename or Path(__file__).parent / 'empregados.xlsx'
    data.to_excel(filename, index=False)
    return filename.is_file()


def sorteio(filename: Path|None = None) -> Path:
    """Lotery by xlsx file."""
    filename = filename or Path(__file__).parent / 'empregados.xlsx'
    ext = {'.xlsx': pd.read_excel}
    fout: Path = filename.with_name(f'{filename.stem}{dt.datetime.now(tz=None).isoformat()}.xlsx')
    df0 = ext.get(ic(filename.suffix))(filename)
    ic(df0)

    itens = list(df0.index)
    random.shuffle(itens)
    ic(itens)
    ic(random.sample(list(df0.index), k=3))

    return fout

