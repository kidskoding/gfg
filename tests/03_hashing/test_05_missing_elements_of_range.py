import pytest
from helpers import load

missing_in_range = load("03_hashing.05_missing_elements_of_range").missing_in_range


@pytest.mark.parametrize(
    "arr, low, high, expected",
    [
        ([10, 12, 11, 15], 10, 15, [13, 14]),
        ([1, 14, 11, 51, 15], 50, 55, [50, 52, 53, 54, 55]),
        ([1, 2, 3], 1, 3, []),
        ([], 4, 6, [4, 5, 6]),
        ([5, 5, 5], 5, 5, []),
        ([100, -1], 0, 2, [0, 1, 2]),  # out-of-range values ignored
        ([-2, 0], -3, 1, [-3, -1, 1]),
    ],
)
def test_missing_in_range(arr, low, high, expected):
    assert missing_in_range(arr, low, high) == expected
