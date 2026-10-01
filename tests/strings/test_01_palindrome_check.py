import pytest
from helpers import load

is_palindrome = load("strings.01_palindrome_check").is_palindrome


@pytest.mark.parametrize(
    "s, expected",
    [
        ("racecar", True),
        ("abba", True),
        ("abc", False),
        ("abca", False),
        ("Aba", False),  # case-sensitive
        ("a", True),
        ("", True),
    ],
)
def test_is_palindrome(s, expected):
    assert is_palindrome(s) is expected
