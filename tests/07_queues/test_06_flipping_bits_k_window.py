import pytest
from helpers import load

min_k_flips = load("07_queues.06_flipping_bits_k_window").min_k_flips


@pytest.mark.parametrize(
    "arr, k, expected",
    [
        ([1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1], 2, 4),
        ([0, 0, 1, 1, 1, 0, 0], 3, -1),
        ([0, 0, 0, 1, 0, 1, 1, 0], 3, 3),
        ([0, 1, 0], 1, 2),
        ([1, 1, 0], 2, -1),
        ([1, 1, 1], 2, 0),
        ([0, 0, 0, 0], 4, 1),
        ([0], 2, -1),  # window longer than array
    ],
)
def test_min_k_flips(arr, k, expected):
    original = list(arr)
    assert min_k_flips(arr, k) == expected
    assert arr == original
