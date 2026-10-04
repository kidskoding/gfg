import pytest
from helpers import load

count_distinct_subsequences = load(
    "02_strings.47_distinct_subsequences"
).count_distinct_subsequences


@pytest.mark.parametrize(
    "s, expected",
    [
        ("gfg", 7),
        ("abc", 8),
        ("aba", 7),
        ("abab", 12),
        ("ggg", 4),
        ("a", 2),
        ("", 1),  # just the empty subsequence
    ],
)
def test_count_distinct_subsequences(s, expected):
    assert count_distinct_subsequences(s) == expected
