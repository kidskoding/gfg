import pytest
from helpers import load

top_k_frequent = load("14_heaps.08_top_k_frequent").top_k_frequent


@pytest.mark.parametrize(
    "arr, k, expected",
    [
        ([3, 1, 4, 4, 5, 2, 6, 1], 2, [4, 1]),
        ([7, 10, 11, 5, 2, 5, 5, 7, 11, 8, 9], 4, [5, 11, 7, 10]),
        ([4, 4, 4, 1, 1, 2], 3, [4, 1, 2]),
        ([1, 1, 2, 2, 3, 3], 2, [3, 2]),  # all tie: larger value first
        ([-1, -1, 2], 2, [-1, 2]),
        ([1], 1, [1]),
    ],
)
def test_top_k_frequent(arr, k, expected):
    assert top_k_frequent(arr, k) == expected
