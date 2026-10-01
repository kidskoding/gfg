import pytest
from helpers import load

first_negatives = load("queues.10_first_negative_in_window").first_negatives


@pytest.mark.parametrize(
    "arr, k, expected",
    [
        ([-8, 2, 3, -6, 10], 2, [-8, 0, -6, -6]),
        ([12, -1, -7, 8, -15, 30, 16, 28], 3, [-1, -1, -7, -15, -15, 0]),
        ([1, 2, 3], 1, [0, 0, 0]),
        ([-5, 4, -3], 1, [-5, 0, -3]),
        ([-1, -2], 2, [-1]),
        ([3, -2, -2, 3], 4, [-2]),
        ([1, 2], 3, []),
        ([], 1, []),
    ],
)
def test_first_negatives(arr, k, expected):
    assert first_negatives(arr, k) == expected
