import pytest
from helpers import load

max_of_subarrays = load("deques.06_max_of_subarrays_size_k").max_of_subarrays


@pytest.mark.parametrize(
    "arr, k, expected",
    [
        ([1, 2, 3, 1, 4, 5, 2, 3, 6], 3, [3, 3, 4, 5, 5, 5, 6]),
        ([8, 5, 10, 7, 9, 4, 15, 12, 90, 13], 4, [10, 10, 10, 15, 15, 90, 90]),
        ([5, 4, 3, 2, 1], 2, [5, 4, 3, 2]),
        ([-1, -3, -2], 1, [-1, -3, -2]),
        ([2, 2, 2], 2, [2, 2]),
        ([4, 1, 7], 3, [7]),
        ([1, 2], 3, []),
    ],
)
def test_max_of_subarrays(arr, k, expected):
    assert max_of_subarrays(arr, k) == expected
