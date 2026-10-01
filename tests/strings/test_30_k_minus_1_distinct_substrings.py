import pytest
from helpers import load

count_k_minus_1_distinct = load(
    "strings.30_k_minus_1_distinct_substrings"
).count_k_minus_1_distinct


@pytest.mark.parametrize(
    "s, k, expected",
    [
        ("abcc", 2, 1),
        ("aabab", 3, 3),
        ("aabbcc", 3, 4),
        ("aaaa", 2, 3),  # counted by position
        ("abcd", 2, 0),
        ("abc", 4, 0),  # k longer than s
        ("a", 1, 0),
    ],
)
def test_count_k_minus_1_distinct(s, k, expected):
    assert count_k_minus_1_distinct(s, k) == expected
