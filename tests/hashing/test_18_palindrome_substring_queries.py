import pytest
from helpers import load

palindrome_queries = load("hashing.18_palindrome_substring_queries").palindrome_queries


@pytest.mark.parametrize(
    "s, queries, expected",
    [
        ("abaaabaaaba", [(0, 10), (5, 8), (2, 5), (5, 9)], [True, False, False, True]),
        ("abcba", [(0, 4), (1, 3), (0, 1), (2, 2)], [True, True, False, True]),
        ("aaaa", [(0, 3), (1, 2), (0, 0)], [True, True, True]),
        ("abab", [(0, 3), (0, 2), (1, 3)], [False, True, True]),
        ("racecar", [(0, 6), (0, 5), (1, 5)], [True, False, True]),
        ("ab", [(0, 1)], [False]),
        ("x", [], []),
    ],
)
def test_palindrome_queries(s, queries, expected):
    assert palindrome_queries(s, queries) == expected
