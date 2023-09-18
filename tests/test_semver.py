"""Módulo de testes."""

import re

import pytest

from incolume.py.coding_dojo_jedi import __version__


@pytest.mark.fast()
class TestSemVer:
    """Test case class for Sematic Versions."""

    def test_version(self, semver_regex):
        """Validação de versionamento semântico para versão do pacote."""
        assert re.fullmatch(semver_regex, __version__, re.I)

    @pytest.mark.parametrize(
        ('entrance', 'expected'),
        (
            (__version__, True),
            ('1', False),
            ('1.0', False),
            ('0.1', False),
            ('1.1.1-rc0', False),
            ('1.1.1-rc-0', False),
            ('1.0.1-dev0', False),
            ('1.1.1-a0', False),
            ('1.1.1a.0', False),
            ('1.1.1-a.0', True),
            ('0.0.1', True),
            ('0.1.0', True),
            ('1.0.0', True),
            ('1.0.1', True),
            ('1.1.1', True),
            ('1.1.1-rc.0', True),
            ('1.0.1-dev.0', True),
            ('1.0.1-dev.1', True),
            ('1.0.1-dev.2', True),
            ('1.0.1-alpha.0', True),
            ('1.0.1-alpha.266', True),
            ('1.0.1-beta.0', True),
            ('1.1.1-alpha.99999', True),
            ('11111.1.1-rc.99999', True),
            ('1.1.99999', True),
            ('1.999999.1', True),
            ('1.1.1a0', True),
            ('1.1.1rc0', True),
            ('1.1.1rc1111', True),
        ),
    )
    def test_semantic_version(self, entrance, expected, semver_regex):
        """Test semantic version asserts."""
        assert (
            bool(
                re.fullmatch(
                    semver_regex,
                    entrance,
                    flags=re.I,
                ),
            )
            == expected
        )
