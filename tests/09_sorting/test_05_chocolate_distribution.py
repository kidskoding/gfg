import pytest
from helpers import load

find_min_diff = load("09_sorting.05_chocolate_distribution").find_min_diff


@pytest.mark.parametrize(
    "arr, m, expected",
    [
        ([7, 3, 2, 4, 9, 12, 56], 3, 2),
        ([3, 4, 1, 9, 56, 7, 9, 12], 5, 6),
        ([7, 3, 2, 4, 9, 12, 56], 5, 7),
        ([4, 4, 4, 9], 3, 0),
        ([5, 8], 1, 0),
        ([1, 2], 0, 0),
        ([1, 2], 3, -1),
    ],
)
def test_find_min_diff(arr, m, expected):
    assert find_min_diff(arr, m) == expected
