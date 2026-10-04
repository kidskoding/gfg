import pytest
from helpers import load

longest_k_unique = load("04_two_pointers.20_longest_k_unique_substring").longest_k_unique


@pytest.mark.parametrize(
    "s, k, expected",
    [
        ("aabacbebebe", 3, 7),
        ("aabaaab", 2, 7),
        ("abcba", 2, 3),
        ("abc", 3, 3),
        ("abc", 1, 1),
        ("aaaa", 2, -1),
        ("", 1, -1),
    ],
)
def test_longest_k_unique(s, k, expected):
    assert longest_k_unique(s, k) == expected
