from itertools import pairwise

import pytest
from helpers import load

alien_order = load("graphs.38_alien_dictionary").alien_order


def _is_valid(order, words):
    if sorted(order) != sorted({ch for w in words for ch in w}):
        return False
    pos = {ch: i for i, ch in enumerate(order)}
    for a, b in pairwise(words):
        for x, y in zip(a, b):
            if x != y:
                if pos[x] > pos[y]:
                    return False
                break
    return True


@pytest.mark.parametrize(
    "words",
    [
        ["baa", "abcd", "abca", "cab", "cad"],
        ["caa", "aaa", "aab"],
        ["wrt", "wrf", "er", "ett", "rftt"],
        ["ab", "ab"],
        ["ab", "abc"],
        ["abc"],
    ],
)
def test_alien_order_valid(words):
    assert _is_valid(alien_order(words), words)


@pytest.mark.parametrize(
    "words, expected",
    [
        (["wrt", "wrf", "er", "ett", "rftt"], "wertf"),
        (["z", "x"], "zx"),
        (["baa", "abcd", "abca", "cab", "cad"], "bdac"),
    ],
)
def test_alien_order_unique(words, expected):
    assert alien_order(words) == expected


@pytest.mark.parametrize(
    "words",
    [
        ["z", "x", "z"],
        ["ab", "cd", "ef", "ad"],  # a < c < e < a
        ["abc", "ab"],  # longer word before its prefix
    ],
)
def test_alien_order_invalid(words):
    assert alien_order(words) == ""
