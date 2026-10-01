import pytest
from helpers import load

min_swaps = load("graphs.28_min_swaps_to_sort").min_swaps


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([2, 8, 5, 4], 1),
        ([10, 19, 6, 3, 5], 2),
        ([2, 3, 4, 1], 3),  # one 4-cycle
        ([4, 3, 2, 1], 2),
        ([3, 2, 1], 1),
        ([-1, -5, 3], 1),
        ([1, 2, 3], 0),
        ([7], 0),
        ([], 0),
    ],
)
def test_min_swaps(arr, expected):
    before = arr[:]
    assert min_swaps(arr) == expected
    assert arr == before
