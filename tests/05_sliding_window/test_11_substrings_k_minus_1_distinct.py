import pytest
from helpers import load

count_k_minus_1_distinct = load(
    "05_sliding_window.11_substrings_k_minus_1_distinct"
).count_k_minus_1_distinct


@pytest.mark.parametrize(
    "s, k, expected",
    [
        ("abcc", 2, 1),
        ("aabab", 3, 3),
        ("aaaa", 2, 3),
        ("abca", 4, 1),
        ("abcd", 2, 0),
        ("aaaa", 1, 0),
        ("ab", 3, 0),  # k longer than s
    ],
)
def test_count_k_minus_1_distinct(s, k, expected):
    assert count_k_minus_1_distinct(s, k) == expected
