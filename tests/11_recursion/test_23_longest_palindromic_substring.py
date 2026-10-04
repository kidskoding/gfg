import pytest
from helpers import load

longest_palindrome_length = load(
    "11_recursion.23_longest_palindromic_substring"
).longest_palindrome_length


@pytest.mark.parametrize(
    "s, expected",
    [
        ("aaaabbaa", 6),
        ("banana", 5),
        ("forgeeksskeegfor", 10),
        ("abc", 1),
        ("a", 1),
        ("", 0),
        ("cbbd", 2),
        ("aaaa", 4),
    ],
)
def test_longest_palindrome_length(s, expected):
    assert longest_palindrome_length(s) == expected
