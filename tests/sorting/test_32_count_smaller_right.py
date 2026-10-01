import pytest
from helpers import load

count_smaller = load("sorting.32_count_smaller_right").count_smaller


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([12, 1, 2, 3, 0, 11, 4], [6, 1, 1, 1, 0, 1, 0]),
        ([5, 4, 3, 2, 1], [4, 3, 2, 1, 0]),
        ([5, 2, 6, 1], [2, 1, 1, 0]),
        ([1, 2, 3], [0, 0, 0]),
        ([2, 2, 2], [0, 0, 0]),  # strictly smaller only
        ([-1, -1], [0, 0]),
        ([], []),
    ],
)
def test_count_smaller(arr, expected):
    assert count_smaller(arr) == expected
