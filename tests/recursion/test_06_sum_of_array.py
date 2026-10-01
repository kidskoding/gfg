import pytest
from helpers import load

sum_array = load("recursion.06_sum_of_array").sum_array


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([1, 2, 3, 4, 5], 15),
        ([15, 12, 13, 10], 50),
        ([9], 9),
        ([], 0),
        ([-1, -2, -3], -6),
        ([5, -5, 3, -3], 0),
        ([2, 2, 2, 2], 8),
    ],
)
def test_sum_array(arr, expected):
    assert sum_array(arr) == expected
