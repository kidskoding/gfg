import pytest
from helpers import load

longest_k_unique = load("05_sliding_window.25_longest_k_unique").longest_k_unique


@pytest.mark.parametrize(
    "s, k, expected",
    [
        ("aabacbebebe", 3, 7),
        ("aabaaab", 2, 7),
        ("eceba", 2, 3),
        ("abcabc", 3, 6),
        ("abc", 1, 1),
        ("aaaa", 2, -1),  # fewer than k distinct
        ("", 1, -1),
    ],
)
def test_longest_k_unique(s, k, expected):
    assert longest_k_unique(s, k) == expected
