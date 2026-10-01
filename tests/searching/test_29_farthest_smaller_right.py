import pytest
from helpers import load

farthest_smaller_right = load(
    "searching.29_farthest_smaller_right"
).farthest_smaller_right


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([2, 5, 1, 3, 2], [2, 4, -1, 4, -1]),
        ([2, 3, 5, 4, 1], [4, 4, 4, 4, -1]),
        ([5, 1, 4, 2, 6], [3, -1, 3, -1, -1]),  # farthest, not nearest or smallest
        ([3, 2, 1], [2, 2, -1]),
        ([1, 2, 3], [-1, -1, -1]),
        ([3, 3, 3], [-1, -1, -1]),  # equal is not smaller
        ([1], [-1]),
        ([], []),
    ],
)
def test_farthest_smaller_right(arr, expected):
    assert farthest_smaller_right(arr) == expected
