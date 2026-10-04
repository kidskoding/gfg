import pytest
from helpers import load

max_ones_k_flips = load("05_sliding_window.09_max_ones_k_flips").max_ones_k_flips


@pytest.mark.parametrize(
    "arr, k, expected",
    [
        ([1, 0, 1], 1, 3),
        ([1, 0, 0, 1, 0, 1, 0, 1], 2, 5),
        ([1, 0, 1, 1, 0, 1, 1, 1], 0, 3),  # no flips allowed
        ([1, 1, 1], 0, 3),
        ([0, 0, 0], 0, 0),
        ([0, 0, 0], 5, 3),  # k larger than zero count
        ([], 1, 0),
    ],
)
def test_max_ones_k_flips(arr, k, expected):
    assert max_ones_k_flips(arr, k) == expected
