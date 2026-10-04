import pytest
from helpers import load

stable_sort_position = load("09_sorting.24_stable_sort_position").stable_sort_position


@pytest.mark.parametrize(
    "arr, index, expected",
    [
        ([3, 4, 3, 5, 2, 3, 4, 3, 1, 5], 5, 4),
        ([3, 4, 3, 5, 2, 3, 4, 3, 1, 5], 0, 2),
        ([3, 4, 3, 5, 2, 3, 4, 3, 1, 5], 9, 9),
        ([5, 4, 3, 2, 1], 0, 4),
        ([2, 2, 2], 2, 2),
        ([-1, 7, -3], 1, 2),
        ([1], 0, 0),
    ],
)
def test_stable_sort_position(arr, index, expected):
    assert stable_sort_position(arr, index) == expected
