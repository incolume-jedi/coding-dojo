"""Configure switch test."""
import pytest


@pytest.fixture(scope='session')
def semver_regex():
    """Fixture para regex de validação do Versionamento Semântico."""
    return r'^\d+(\.\d+){2}((-\w+\.\d+)|(\w+\d+))?$'
