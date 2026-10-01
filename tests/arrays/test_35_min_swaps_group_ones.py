import pytest
from helpers import load

min_swaps_group_ones = load("arrays.35_min_swaps_group_ones").min_swaps_group_ones


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([1, 0, 1, 0, 1], 1),
        ([1, 0, 1, 0, 1, 1], 1),
        ([0, 0, 0], -1),
        ([1, 1, 1], 0),
        ([1, 0, 0, 1, 0, 1, 0, 1], 2),
        ([0, 1, 0], 0),
        ([1, 0, 0, 0, 1], 1),
    ],
)
def test_min_swaps_group_ones(arr, expected):
    assert min_swaps_group_ones(arr) == expected
