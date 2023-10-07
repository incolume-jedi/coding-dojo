import re
from pathlib import Path
from typing import ClassVar

import pytest


class TestCase:
    """Caso de teste para este dojo."""

    directories: ClassVar = list(Path(__file__).parents[1].iterdir())

    def test_path(self):
        """Test path."""
        assert all(d.parts[-2] == 'coding_dojo_jedi' for d in self.directories)

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            ('20190129', True),
            ('20220714', True),
            ('20220717', True),
            ('20220718', True),
            ('20220720', True),
            ('20220721', True),
            ('20220722', True),
            ('20220723', True),
            ('20220725', True),
            ('20220727', True),
            ('20220729', True),
            ('20220731', True),
            ('20220801', True),
            ('20220803', True),
            ('20220805', True),
            ('20220808', True),
            ('20220809', True),
            ('20220810', True),
            ('20220811', True),
            ('20220812', True),
            ('20220815', True),
            ('20220817', True),
            ('20220819', True),
            ('20220822', True),
            ('20220824', True),
            ('20220826', True),
            ('20220831', True),
            ('20220902', True),
            ('20220905', True),
            ('20220907', True),
            ('20220909', True),
            ('20220910', True),
            ('20220912', True),
            ('20220914', True),
            ('20220919', True),
            ('20220921', True),
            ('20220926', True),
            ('20220928', True),
            ('20220929', False),
            ('20231005', True),
        ],
    )
    def test_corretion_datas(self, entrance, expected) -> None:
        """Verifica se os diretórios no formato anterior estão presentes."""
        result = None
        for directory in self.directories:
            result = re.search(f'{entrance}', directory.as_posix())
            if result:
                break
        assert bool(result) == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            ('20190129', True),
            ('20220714', True),
            ('20220717', True),
            ('20220718', True),
            ('20220720', True),
            ('20220721', True),
            ('20220722', True),
            ('20220723', True),
            ('20220725', True),
            ('20220727', True),
            ('20220729', True),
            ('20220731', True),
            ('20220801', True),
            ('20220803', True),
            ('20220805', True),
            ('20220808', True),
            ('20220809', True),
            ('20220810', True),
            ('20220811', True),
            ('20220812', True),
            ('20220815', True),
            ('20220817', True),
            ('20220819', True),
            ('20220822', True),
            ('20220824', True),
            ('20220826', True),
            ('20220831', True),
            ('20220902', True),
            ('20220905', True),
            ('20220907', True),
            ('20220909', True),
            ('20220910', True),
            ('20220912', True),
            ('20220914', True),
            ('20220919', True),
            ('20220921', True),
            ('20220926', True),
            ('20220928', True),
            ('20220929', False),
            ('20231005', True),
        ],
    )
    def test_formato_novo(self, entrance, expected):
        """Test para nova formação da estrutura de pastas."""
        for directory in self.directories:
            if value := re.search(f'dojo{entrance}', directory.as_posix()):
                break
        assert bool(value) == expected
