import pytest
from helpers import load

longest_distinct_substring = load(
    "05_sliding_window.07_longest_distinct_substring"
).longest_distinct_substring


@pytest.mark.parametrize(
    "s, expected",
    [
        ("geeksforgeeks", 7),
        ("abcdefabcbb", 6),
        ("pwwkew", 3),
        ("abba", 2),
        ("dvdf", 3),
        ("aaa", 1),
        ("", 0),
    ],
)
def test_longest_distinct_substring(s, expected):
    assert longest_distinct_substring(s) == expected
