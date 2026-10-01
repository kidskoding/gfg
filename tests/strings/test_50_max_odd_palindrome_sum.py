import pytest
from helpers import load

max_odd_palindrome_sum = load(
    "strings.50_max_odd_palindrome_sum"
).max_odd_palindrome_sum


@pytest.mark.parametrize(
    "s, expected",
    [
        ("xyabacbcz", 6),  # aba + cbc
        ("gfgforgeeks", 4),  # gfg + any single char
        ("abacaba", 6),  # whole string can't be used twice
        ("aaaa", 4),  # aaa + a
        ("abcde", 2),
        ("aa", 2),
        ("ab", 2),
    ],
)
def test_max_odd_palindrome_sum(s, expected):
    assert max_odd_palindrome_sum(s) == expected
