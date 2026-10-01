import pytest
from helpers import load

nearest_smaller_left = load("stacks.12_nearest_smaller_on_left").nearest_smaller_left


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([1, 6, 2], [-1, 1, 1]),
        ([1, 5, 0, 3, 4, 5], [-1, 1, -1, 0, 3, 4]),
        ([2, 1, 5, 6, 2, 3], [-1, -1, 1, 5, 1, 2]),
        ([-1, -3, 0], [-1, -1, -3]),
        ([5, 4, 3], [-1, -1, -1]),
        ([3, 3, 3], [-1, -1, -1]),
        ([], []),
    ],
)
def test_nearest_smaller_left(arr, expected):
    assert nearest_smaller_left(arr) == expected
