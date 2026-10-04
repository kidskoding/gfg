import pytest
from helpers import load

max_consecutive_same = load("01_arrays.07_max_consecutive_ones").max_consecutive_same


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([0, 1, 0, 1, 1, 1, 1], 4),
        ([0, 0, 1, 0, 1, 0], 2),
        ([0, 0, 0, 0], 4),
        ([1, 0, 1, 0], 1),
        ([1], 1),
        ([], 0),
        ([1, 1, 0, 0, 0, 1], 3),
    ],
)
def test_max_consecutive_same(arr, expected):
    assert max_consecutive_same(arr) == expected
