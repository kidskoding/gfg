import pytest
from helpers import load

longest_subarray_within_x = load(
    "deques.09_longest_subarray_within_x"
).longest_subarray_within_x


@pytest.mark.parametrize(
    "arr, x, expected",
    [
        ([8, 4, 2, 6, 7], 4, [4, 2, 6]),
        ([15, 10, 1, 2, 4, 7, 2], 5, [2, 4, 7, 2]),
        ([1, 5, 2, 6], 3, [5, 2]),
        ([-3, -1, -6, 0], 3, [-3, -1]),
        ([1, 3, 5], 0, [1]),  # leftmost of equal-length answers
        ([1, 1, 1], 0, [1, 1, 1]),
        ([5, 1, 9], 10, [5, 1, 9]),
        ([], 4, []),
    ],
)
def test_longest_subarray_within_x(arr, x, expected):
    assert longest_subarray_within_x(arr, x) == expected
