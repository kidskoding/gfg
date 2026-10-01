import pytest
from helpers import load

min_insertions = load("strings.49_min_insertions_palindrome").min_insertions


@pytest.mark.parametrize(
    "s, expected",
    [
        ("abcd", 3),
        ("geeks", 3),
        ("abcda", 2),
        ("abcde", 4),
        ("ab", 1),
        ("aba", 0),
        ("aa", 0),
        ("", 0),
    ],
)
def test_min_insertions(s, expected):
    assert min_insertions(s) == expected
