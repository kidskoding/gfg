import pytest
from helpers import load

subsequence_count = load(
    "18_dynamic_programming.21_count_distinct_occurrences"
).subsequence_count


@pytest.mark.parametrize(
    "s, t, expected",
    [
        ("banana", "ban", 3),
        ("geeksforgeeks", "ge", 6),
        ("rabbbit", "rabbit", 3),
        ("babgbag", "bag", 5),
        ("aaaa", "aa", 6),
        ("abc", "", 1),
        ("", "a", 0),
        ("ab", "abc", 0),
    ],
)
def test_subsequence_count(s, t, expected):
    assert subsequence_count(s, t) == expected
