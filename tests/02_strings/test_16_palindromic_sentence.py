import pytest
from helpers import load

is_sentence_palindrome = load("02_strings.16_palindromic_sentence").is_sentence_palindrome


@pytest.mark.parametrize(
    "s, expected",
    [
        ("Too hot to hoot.", True),
        ("Abc 012..## 10cba", True),
        ("A man, a plan, a canal: Panama", True),
        ("ABC $. def01ASDF", False),
        ("race a car", False),
        ("0P", False),  # digits count
        ("...", True),
        ("", True),
    ],
)
def test_is_sentence_palindrome(s, expected):
    assert is_sentence_palindrome(s) is expected
