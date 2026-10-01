import pytest
from helpers import load

is_sentence_palindrome = load(
    "two_pointers.12_sentence_palindrome"
).is_sentence_palindrome


@pytest.mark.parametrize(
    "s, expected",
    [
        ("Too hot to hoot.", True),
        ("Abc 012..##  10cba", True),
        ("ABC $. def01ASDF", False),
        ("No 'x' in Nixon", True),
        ("ab", False),
        ("a", True),
        (".", True),
        ("", True),
    ],
)
def test_is_sentence_palindrome(s, expected):
    assert is_sentence_palindrome(s) is expected
