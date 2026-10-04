import pytest
from helpers import load

missing_ranges = load("01_arrays.17_missing_ranges").missing_ranges


@pytest.mark.parametrize(
    "arr, lower, upper, expected",
    [
        (
            [14, 15, 20, 30, 31, 45],
            10,
            50,
            [[10, 13], [16, 19], [21, 29], [32, 44], [46, 50]],
        ),
        (
            [-48, -10, -6, -4, 0, 4, 17],
            -54,
            17,
            [[-54, -49], [-47, -11], [-9, -7], [-5, -5], [-3, -1], [1, 3], [5, 16]],
        ),
        ([1, 2, 3], 1, 3, []),
        ([], 1, 5, [[1, 5]]),
        ([2], 1, 3, [[1, 1], [3, 3]]),
        ([0, 2, 4], 0, 4, [[1, 1], [3, 3]]),
    ],
)
def test_missing_ranges(arr, lower, upper, expected):
    assert missing_ranges(arr, lower, upper) == expected
