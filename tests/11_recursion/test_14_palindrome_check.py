import pytest
from helpers import load

is_palindrome = load("11_recursion.14_palindrome_check").is_palindrome


@pytest.mark.parametrize(
    "s, expected",
    [
        ("malayalam", True),
        ("geeks", False),
        ("abba", True),
        ("abca", False),
        ("a", True),
        ("", True),
        ("Aa", False),  # case-sensitive
        ("ab", False),
    ],
)
def test_is_palindrome(s, expected):
    assert is_palindrome(s) is expected
