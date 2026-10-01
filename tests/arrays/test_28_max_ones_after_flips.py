import pytest
from helpers import load

max_ones_after_flips = load("arrays.28_max_ones_after_flips").max_ones_after_flips


@pytest.mark.parametrize(
    "arr, k, expected",
    [
        ([1, 0, 1], 1, 3),
        ([1, 0, 0, 1, 0, 1, 0, 1], 2, 5),
        ([1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1], 2, 8),
        ([1, 1, 0, 1, 1], 0, 2),
        ([0, 0, 0], 0, 0),
        ([0, 0, 0], 5, 3),
        ([1, 1, 1], 1, 3),
        ([], 1, 0),
    ],
)
def test_max_ones_after_flips(arr, k, expected):
    assert max_ones_after_flips(arr, k) == expected
