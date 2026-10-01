import pytest
from helpers import load

is_binary_palindrome = load(
    "bit_manipulation.25_binary_palindrome"
).is_binary_palindrome


@pytest.mark.parametrize(
    "n, expected",
    [
        (9, True),
        (21, True),
        (3, True),
        (2**31 - 1, True),
        (10, False),
        (6, False),
        (2**31, False),
        (1, True),
        (0, True),
    ],
)
def test_is_binary_palindrome(n, expected):
    assert is_binary_palindrome(n) is expected
