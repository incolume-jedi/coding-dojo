"""Test remove anchor."""

import pytest

from incolume.py.coding_dojo_jedi.dojo20231109.dojo20231109 import (
    remove_url_anchor,
    remove_url_anchor0,
    remove_url_anchor1,
    remove_url_anchor2,
    remove_url_anchor3,
)


class TestCase:
    """Test case dojo."""

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            ('www.codewars.com#about', 'www.codewars.com'),
            ('http://www.codewars.com#about', 'http://www.codewars.com'),
            ('https://www.codewars.com#about', 'https://www.codewars.com'),
            ('ftp://www.codewars.com#about', 'ftp://www.codewars.com'),
            ('ftps://www.codewars.com#about', 'ftps://www.codewars.com'),
            ('www.codewars.com?page=1', 'www.codewars.com?page=1'),
            (
                'www.codewars.com/katas/?page=1#about',
                'www.codewars.com/katas/?page=1',
            ),
            ('www.codewars.com/katas/', 'www.codewars.com/katas/'),
            (
                'https://drive.google.com/open?id=10koZnSvaSLgGo-'
                'YVkYZmLER4XXScE6Rq#usp=drive_copy',
                'https://drive.google.com/open?id=10koZnSvaSLgGo-'
                'YVkYZmLER4XXScE6Rq',
            ),
        ],
    )
    def test_remove_url_anchor0(self, entrance, expected) -> None:
        """Test this."""
        assert remove_url_anchor0(entrance) == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            ('www.codewars.com#about', 'www.codewars.com'),
            ('http://www.codewars.com#about', 'http://www.codewars.com'),
            ('https://www.codewars.com#about', 'https://www.codewars.com'),
            ('ftp://www.codewars.com#about', 'ftp://www.codewars.com'),
            ('ftps://www.codewars.com#about', 'ftps://www.codewars.com'),
            ('www.codewars.com?page=1', 'www.codewars.com?page=1'),
            (
                'www.codewars.com/katas/?page=1#about',
                'www.codewars.com/katas/?page=1',
            ),
            ('www.codewars.com/katas/', 'www.codewars.com/katas/'),
            (
                'https://drive.google.com/open?id=10koZnSvaSLgGo-'
                'YVkYZmLER4XXScE6Rq#usp=drive_copy',
                'https://drive.google.com/open?id=10koZnSvaSLgGo-'
                'YVkYZmLER4XXScE6Rq',
            ),
        ],
    )
    def test_remove_url_anchor1(self, entrance, expected) -> None:
        """Test this."""
        assert remove_url_anchor1(entrance) == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            ('www.codewars.com#about', 'www.codewars.com'),
            ('http://www.codewars.com#about', 'http://www.codewars.com'),
            ('https://www.codewars.com#about', 'https://www.codewars.com'),
            ('ftp://www.codewars.com#about', 'ftp://www.codewars.com'),
            ('ftps://www.codewars.com#about', 'ftps://www.codewars.com'),
            ('www.codewars.com?page=1', 'www.codewars.com?page=1'),
            (
                'www.codewars.com/katas/?page=1#about',
                'www.codewars.com/katas/?page=1',
            ),
            ('www.codewars.com/katas/', 'www.codewars.com/katas/'),
            (
                'https://drive.google.com/open?id=10koZnSvaSLgGo-'
                'YVkYZmLER4XXScE6Rq#usp=drive_copy',
                'https://drive.google.com/open?id=10koZnSvaSLgGo-'
                'YVkYZmLER4XXScE6Rq',
            ),
        ],
    )
    def test_remove_url_anchor2(self, entrance, expected) -> None:
        """Test this."""
        assert remove_url_anchor2(entrance) == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            ('www.codewars.com#about', 'www.codewars.com'),
            ('http://www.codewars.com#about', 'http://www.codewars.com'),
            ('https://www.codewars.com#about', 'https://www.codewars.com'),
            ('ftp://www.codewars.com#about', 'ftp://www.codewars.com'),
            ('ftps://www.codewars.com#about', 'ftps://www.codewars.com'),
            ('www.codewars.com?page=1', 'www.codewars.com?page=1'),
            (
                'www.codewars.com/katas/?page=1#about',
                'www.codewars.com/katas/?page=1',
            ),
            ('www.codewars.com/katas/', 'www.codewars.com/katas/'),
            (
                'https://drive.google.com/open?id=10koZnSvaSLgGo-'
                'YVkYZmLER4XXScE6Rq#usp=drive_copy',
                'https://drive.google.com/open?id=10koZnSvaSLgGo-'
                'YVkYZmLER4XXScE6Rq',
            ),
        ],
    )
    def test_remove_url_anchor3(self, entrance, expected) -> None:
        """Test this."""
        assert remove_url_anchor3(entrance) == expected

    @pytest.mark.parametrize(
        'entrance expected'.split(),
        [
            ('www.codewars.com#about', 'www.codewars.com'),
            ('http://www.codewars.com#about', 'http://www.codewars.com'),
            ('https://www.codewars.com#about', 'https://www.codewars.com'),
            ('ftp://www.codewars.com#about', 'ftp://www.codewars.com'),
            ('ftps://www.codewars.com#about', 'ftps://www.codewars.com'),
            ('www.codewars.com?page=1', 'www.codewars.com?page=1'),
            (
                'www.codewars.com/katas/?page=1#about',
                'www.codewars.com/katas/?page=1',
            ),
            ('www.codewars.com/katas/', 'www.codewars.com/katas/'),
            (
                'https://drive.google.com/open?id=10koZnSvaSLgGo-'
                'YVkYZmLER4XXScE6Rq#usp=drive_copy',
                'https://drive.google.com/open?id=10koZnSvaSLgGo-'
                'YVkYZmLER4XXScE6Rq',
            ),
        ],
    )
    def test_remove_url_anchor(self, entrance, expected) -> None:
        """Test this."""
        assert remove_url_anchor(entrance) == expected
