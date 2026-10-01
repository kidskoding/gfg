import pytest
from helpers import load

first_negative_in_windows = load(
    "deques.05_first_negative_in_window"
).first_negative_in_windows


@pytest.mark.parametrize(
    "arr, k, expected",
    [
        ([-8, 2, 3, -6, 10], 2, [-8, 0, -6, -6]),
        ([12, -1, -7, 8, -15, 30, 16, 28], 3, [-1, -1, -7, -15, -15, 0]),
        ([1, 2, 3], 2, [0, 0]),
        ([-1, -2, -3], 1, [-1, -2, -3]),
        ([-3, -1, 4], 3, [-3]),
        ([5], 1, [0]),
        ([-5], 1, [-5]),
        ([1, -1], 3, []),
    ],
)
def test_first_negative_in_windows(arr, k, expected):
    assert first_negative_in_windows(arr, k) == expected
