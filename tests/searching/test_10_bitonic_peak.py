import pytest
from helpers import load

bitonic_peak = load("searching.10_bitonic_peak").bitonic_peak


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([8, 10, 20, 80, 100, 200, 400, 500, 3, 2, 1], 500),
        ([1, 3, 50, 10, 9, 7, 6], 50),
        ([10, 20, 30, 40, 50], 50),  # increasing only
        ([120, 100, 80, 20, 0], 120),  # decreasing only
        ([-3, -1, -2], -1),
        ([1, 2], 2),
        ([5], 5),
    ],
)
def test_bitonic_peak(arr, expected):
    assert bitonic_peak(arr) == expected
