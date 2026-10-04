import pytest
from helpers import load

numbers_with_diff = load("11_recursion.43_n_digit_numbers_with_k_diff").numbers_with_diff


@pytest.mark.parametrize(
    "n, k, expected",
    [
        (2, 1, [10, 12, 21, 23, 32, 34, 43, 45, 54, 56, 65, 67, 76, 78, 87, 89, 98]),
        (3, 7, [181, 292, 707, 818, 929]),
        (2, 0, [11, 22, 33, 44, 55, 66, 77, 88, 99]),  # k == 0: no double counting
        (2, 9, [90]),  # no leading zero, so 09 is excluded
        (3, 9, [909]),
        (3, 0, [111, 222, 333, 444, 555, 666, 777, 888, 999]),
        (4, 8, [1919, 8080, 9191]),
        (3, 10, []),
    ],
)
def test_numbers_with_diff(n, k, expected):
    assert numbers_with_diff(n, k) == expected
