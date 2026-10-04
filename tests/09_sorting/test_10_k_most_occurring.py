import pytest
from helpers import load

top_k_frequent = load("09_sorting.10_k_most_occurring").top_k_frequent


@pytest.mark.parametrize(
    "arr, k, expected",
    [
        ([3, 1, 4, 4, 5, 2, 6, 1], 2, [4, 1]),
        ([7, 10, 11, 5, 2, 5, 5, 7, 11, 8, 9], 4, [5, 11, 7, 10]),
        ([2, 2, 2, 1, 1, 3], 1, [2]),
        ([1, 2, 3], 3, [3, 2, 1]),  # all tied: larger value first
        ([-1, -1, 4], 2, [-1, 4]),
        ([1], 1, [1]),
    ],
)
def test_top_k_frequent(arr, k, expected):
    assert top_k_frequent(arr, k) == expected
