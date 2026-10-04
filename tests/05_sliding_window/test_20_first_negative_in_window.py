import pytest
from helpers import load

first_negatives = load("05_sliding_window.20_first_negative_in_window").first_negatives


@pytest.mark.parametrize(
    "arr, k, expected",
    [
        ([-8, 2, 3, -6, 10], 2, [-8, 0, -6, -6]),
        ([12, -1, -7, 8, -15, 30, 16, 28], 3, [-1, -1, -7, -15, -15, 0]),
        ([12, 1, 3, 5], 3, [0, 0]),
        ([1, -2, -3], 3, [-2]),
        ([-5, -4, -3], 1, [-5, -4, -3]),
        ([-1], 1, [-1]),
    ],
)
def test_first_negatives(arr, k, expected):
    assert first_negatives(arr, k) == expected
