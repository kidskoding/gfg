import pytest
from helpers import load

next_palindrome = load("strings.25_next_palindrome_same_digits").next_palindrome


@pytest.mark.parametrize(
    "num, expected",
    [
        ("4697557964", "4756996574"),
        ("12321", "21312"),
        ("35453", "53435"),
        ("1221", "2112"),
        ("123321", "132231"),
        ("53435", None),  # already the largest arrangement
        ("11", None),
        ("1", None),
    ],
)
def test_next_palindrome(num, expected):
    assert next_palindrome(num) == expected
