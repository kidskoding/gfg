import pytest
from helpers import load

zero_sum_subarrays = load("03_hashing.10_all_zero_sum_subarrays").zero_sum_subarrays


@pytest.mark.parametrize(
    "arr, expected",
    [
        (
            [6, 3, -1, -3, 4, -2, 2, 4, 6, -12, -7],
            [(0, 10), (2, 4), (2, 6), (5, 6), (6, 9)],
        ),
        ([1, 2, -3, 3, -1, -1], [(0, 2), (1, 5), (2, 3)]),
        ([1, 2, 3], []),
        ([0], [(0, 0)]),
        ([0, 0], [(0, 0), (0, 1), (1, 1)]),
        ([], []),
        ([5, -5, 5, -5], [(0, 1), (0, 3), (1, 2), (2, 3)]),
    ],
)
def test_zero_sum_subarrays(arr, expected):
    assert zero_sum_subarrays(arr) == expected
