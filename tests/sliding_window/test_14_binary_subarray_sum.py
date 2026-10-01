import pytest
from helpers import load

count_binary_subarrays = load(
    "sliding_window.14_binary_subarray_sum"
).count_binary_subarrays


@pytest.mark.parametrize(
    "arr, target, expected",
    [
        ([1, 0, 1, 0, 1], 2, 4),
        ([1, 0, 1, 1, 1, 0, 0], 2, 6),
        ([0, 1, 0], 1, 4),
        ([0, 0, 0, 0, 0], 0, 15),  # target 0
        ([1, 1, 1], 4, 0),
        ([1], 1, 1),
        ([], 0, 0),
    ],
)
def test_count_binary_subarrays(arr, target, expected):
    assert count_binary_subarrays(arr, target) == expected
