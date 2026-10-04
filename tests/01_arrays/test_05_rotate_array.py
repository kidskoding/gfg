import pytest
from helpers import load

rotate_left = load("01_arrays.05_rotate_array").rotate_left


@pytest.mark.parametrize(
    "arr, d, expected",
    [
        ([1, 2, 3, 4, 5, 6], 2, [3, 4, 5, 6, 1, 2]),
        ([1, 2, 3], 4, [2, 3, 1]),
        ([1, 2, 3, 4], 0, [1, 2, 3, 4]),
        ([1, 2, 3, 4], 4, [1, 2, 3, 4]),
        ([1, 2, 3, 4, 5], 7, [3, 4, 5, 1, 2]),
        ([9], 3, [9]),
        ([], 3, []),
    ],
)
def test_rotate_left(arr, d, expected):
    rotate_left(arr, d)
    assert arr == expected
