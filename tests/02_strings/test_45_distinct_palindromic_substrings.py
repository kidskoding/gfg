import pytest
from helpers import load

count_distinct_palindromes = load(
    "02_strings.45_distinct_palindromic_substrings"
).count_distinct_palindromes


@pytest.mark.parametrize(
    "s, expected",
    [
        ("abaaa", 5),  # a, b, aa, aba, aaa
        ("geek", 4),  # g, e, k, ee
        ("abba", 4),
        ("aaaa", 4),
        ("aba", 3),
        ("abc", 3),
        ("a", 1),
        ("", 0),
    ],
)
def test_count_distinct_palindromes(s, expected):
    assert count_distinct_palindromes(s) == expected
