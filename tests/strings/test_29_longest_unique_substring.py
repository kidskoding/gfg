import pytest
from helpers import load

longest_unique_substring = load(
    "strings.29_longest_unique_substring"
).longest_unique_substring


@pytest.mark.parametrize(
    "s, expected",
    [
        ("geeksforgeeks", 7),
        ("abcdefabcbb", 6),
        ("abcabcbb", 3),
        ("pwwkew", 3),
        ("dvdf", 3),
        ("aaa", 1),
        ("a", 1),
        ("", 0),
    ],
)
def test_longest_unique_substring(s, expected):
    assert longest_unique_substring(s) == expected
