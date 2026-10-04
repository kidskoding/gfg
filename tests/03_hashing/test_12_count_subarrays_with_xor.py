import pytest
from helpers import load

count_subarrays_xor = load("03_hashing.12_count_subarrays_with_xor").count_subarrays_xor


@pytest.mark.parametrize(
    "arr, k, expected",
    [
        ([4, 2, 2, 6, 4], 6, 4),
        ([5, 6, 7, 8, 9], 5, 2),
        ([1, 1, 1], 0, 2),
        ([1, 2, 3], 7, 0),
        ([0, 0, 0], 0, 6),  # every subarray
        ([3], 3, 1),
        ([], 0, 0),
    ],
)
def test_count_subarrays_xor(arr, k, expected):
    assert count_subarrays_xor(arr, k) == expected
