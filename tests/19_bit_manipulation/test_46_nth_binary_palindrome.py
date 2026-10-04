import pytest
from helpers import load

nth_binary_palindrome = load(
    "19_bit_manipulation.46_nth_binary_palindrome"
).nth_binary_palindrome


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, 1),
        (2, 3),
        (4, 7),
        (5, 9),
        (6, 15),
        (9, 27),
        (15, 65),
        (20, 107),
    ],
)
def test_nth_binary_palindrome(n, expected):
    assert nth_binary_palindrome(n) == expected


def test_nth_binary_palindrome_large():
    # 2**((L - 1) // 2) palindromes of length L: lengths 1..20 hold 2046, the last being 2**20 - 1
    assert nth_binary_palindrome(2046) == 2**20 - 1
    assert nth_binary_palindrome(2047) == 2**20 + 1
