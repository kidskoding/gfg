import pytest
from helpers import load

count_k_distinct = load("02_strings.31_count_k_distinct_substrings").count_k_distinct


@pytest.mark.parametrize(
    "s, k, expected",
    [
        ("abcbaa", 3, 8),
        ("abc", 2, 2),
        ("aba", 2, 3),
        ("aa", 1, 3),  # counted by position
        ("aaa", 2, 0),
        ("", 1, 0),
    ],
)
def test_count_k_distinct(s, k, expected):
    assert count_k_distinct(s, k) == expected
