import pytest
from helpers import load

min_palindrome_cuts = load(
    "dynamic_programming.26_palindrome_partitioning"
).min_palindrome_cuts


@pytest.mark.parametrize(
    "s, expected",
    [
        ("geek", 2),
        ("aaaa", 0),
        ("ababbbabbababa", 3),
        ("aab", 1),
        ("abcde", 4),
        ("a", 0),
        ("", 0),
    ],
)
def test_min_palindrome_cuts(s, expected):
    assert min_palindrome_cuts(s) == expected
