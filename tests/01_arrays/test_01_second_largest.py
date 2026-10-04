import pytest
from helpers import load

second_largest = load("01_arrays.01_second_largest").second_largest


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([12, 35, 1, 10, 34, 1], 34),
        ([10, 5, 10], 5),
        ([10, 10, 10], -1),
        ([7], -1),
        ([-3, -1, -2], -2),
        ([1, 2], 1),
        ([5, 5, 4, 4], 4),
    ],
)
def test_second_largest(arr, expected):
    assert second_largest(arr) == expected
