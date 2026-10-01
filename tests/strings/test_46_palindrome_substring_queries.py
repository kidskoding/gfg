import pytest
from helpers import load

palindrome_queries = load("strings.46_palindrome_substring_queries").palindrome_queries


@pytest.mark.parametrize(
    "s, queries, expected",
    [
        (
            "abaaabaaaba",
            [(0, 10), (5, 8), (2, 5), (5, 9)],
            [True, False, False, True],
        ),
        (
            "racecar",
            [(0, 6), (1, 5), (0, 0), (0, 1), (2, 3), (3, 3)],
            [True, True, True, False, False, True],
        ),
        ("aa", [(0, 1), (1, 1)], [True, True]),
        ("ab", [(0, 1)], [False]),
        ("abc", [], []),
    ],
)
def test_palindrome_queries(s, queries, expected):
    assert palindrome_queries(s, queries) == expected
