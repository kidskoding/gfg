import pytest
from helpers import load

longest_k_unique = load("02_strings.27_longest_k_unique_substring").longest_k_unique


@pytest.mark.parametrize(
    "s, k, expected",
    [
        ("aabacbebebe", 3, 7),
        ("aabaaab", 2, 7),
        ("abc", 1, 1),
        ("abc", 3, 3),
        ("aaaa", 2, -1),
        ("abc", 4, -1),
        ("", 1, -1),
    ],
)
def test_longest_k_unique(s, k, expected):
    assert longest_k_unique(s, k) == expected
