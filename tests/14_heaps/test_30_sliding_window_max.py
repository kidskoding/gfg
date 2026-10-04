import pytest
from helpers import load

sliding_window_max = load("14_heaps.30_sliding_window_max").sliding_window_max


@pytest.mark.parametrize(
    "arr, k, expected",
    [
        ([1, 2, 3, 1, 4, 5, 2, 3, 6], 3, [3, 3, 4, 5, 5, 5, 6]),
        ([8, 5, 10, 7, 9, 4, 15, 12, 90, 13], 4, [10, 10, 10, 15, 15, 90, 90]),
        ([-1, -3, -2], 2, [-1, -2]),
        ([4, 4, 4], 2, [4, 4]),
        ([3, 2, 1], 3, [3]),
        ([1, 2, 3], 1, [1, 2, 3]),
        ([5], 1, [5]),
    ],
)
def test_sliding_window_max(arr, k, expected):
    assert sliding_window_max(arr, k) == expected
