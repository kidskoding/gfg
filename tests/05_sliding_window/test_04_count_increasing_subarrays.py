import pytest
from helpers import load

count_increasing_subarrays = load(
    "05_sliding_window.04_count_increasing_subarrays"
).count_increasing_subarrays


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([1, 4, 3], 1),
        ([1, 2, 3, 4], 6),
        ([1, 2, 2, 4], 2),  # equal neighbours break the run
        ([1, 3, 2, 4, 5], 4),
        ([5, 4, 3], 0),
        ([7], 0),
        ([], 0),
    ],
)
def test_count_increasing_subarrays(arr, expected):
    assert count_increasing_subarrays(arr) == expected
