import pytest
from helpers import load

max_circular_sum = load("arrays.39_max_circular_subarray_sum").max_circular_sum


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([8, -8, 9, -9, 10, -11, 12], 22),
        ([10, -3, -4, 7, 6, 5, -4, -1], 23),
        ([5, -2, 3, 4], 12),
        ([-1, -40, -3], -1),
        ([7], 7),
        ([1, -2, 3, -2], 3),
        ([5, -3, 5], 10),
    ],
)
def test_max_circular_sum(arr, expected):
    assert max_circular_sum(arr) == expected
