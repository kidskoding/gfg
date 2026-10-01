import pytest
from helpers import load

min_deletions = load("strings.48_min_deletions_palindrome").min_deletions


@pytest.mark.parametrize(
    "s, expected",
    [
        ("aebcbda", 2),
        ("geeksforgeeks", 8),
        ("abcd", 3),
        ("ab", 1),
        ("abcba", 0),
        ("a", 0),
        ("", 0),
    ],
)
def test_min_deletions(s, expected):
    assert min_deletions(s) == expected
