import pytest
from helpers import load

second_largest = load("10_searching.02_second_largest").second_largest


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([12, 35, 1, 10, 34, 1], 34),
        ([10, 5, 10], 5),  # duplicate max does not count
        ([10, 10, 10], -1),
        ([5, 4, 3, 2, 1], 4),
        ([1, 2], 1),
        ([0, 0, 3], 0),
        ([7], -1),
    ],
)
def test_second_largest(arr, expected):
    assert second_largest(arr) == expected
