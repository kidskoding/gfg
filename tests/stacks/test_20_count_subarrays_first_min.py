import pytest
from helpers import load

count_first_min_subarrays = load(
    "stacks.20_count_subarrays_first_min"
).count_first_min_subarrays


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([1, 2, 1], 5),
        ([1, 3, 5, 2], 8),
        ([4, 1, 3, 2], 6),
        ([2, 2, 2], 6),
        ([1, 2, 3], 6),
        ([3, 2, 1], 3),
        ([7], 1),
        ([], 0),
    ],
)
def test_count_first_min_subarrays(arr, expected):
    assert count_first_min_subarrays(arr) == expected
