import pytest
from helpers import load

count_equivalent_subarrays = load(
    "sliding_window.23_equivalent_subarrays"
).count_equivalent_subarrays


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([2, 1, 3, 2, 3], 5),
        ([2, 4, 4, 2, 4], 9),
        ([1, 2, 1, 2], 6),
        ([1, 2, 3], 1),
        ([1, 1, 1], 6),  # one distinct value: every subarray
        ([5], 1),
        ([], 0),
    ],
)
def test_count_equivalent_subarrays(arr, expected):
    assert count_equivalent_subarrays(arr) == expected
