"""dojo module."""

import itertools
import logging
from collections import defaultdict


def anagrams_gen(word):
    """Gerador de anagramas."""
    perms = [''.join(p) for p in itertools.permutations(word)]
    return list(set(perms))  # Remove duplicates


def group_anagram(anagram_list: list[str]) -> list[list[str]]:
    """Dojo solution."""
    result = defaultdict(list)
    for anagram in sorted(anagram_list):
        result[''.join(sorted(anagram))].append(anagram)
    return sorted(result.values())


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    word = 'abcd'
    anagrams_list = anagrams_gen(word)
    logging.debug(anagrams_list)
