import pytest
from helpers import load

next_palindrome = load("arrays.46_next_smallest_palindrome").next_palindrome


@pytest.mark.parametrize(
    "digits, expected",
    [
        ([9, 4, 1, 8, 7, 9, 7, 8, 3, 2, 2], [9, 4, 1, 8, 8, 0, 8, 8, 1, 4, 9]),
        ([2, 3, 5, 4, 5], [2, 3, 6, 3, 2]),
        ([9, 9, 9], [1, 0, 0, 1]),
        ([1, 2, 3], [1, 3, 1]),
        ([1, 2, 1], [1, 3, 1]),
        ([1, 9, 9, 1], [2, 0, 0, 2]),
        ([7], [8]),
        ([9], [1, 1]),
    ],
)
def test_next_palindrome(digits, expected):
    assert next_palindrome(digits) == expected
