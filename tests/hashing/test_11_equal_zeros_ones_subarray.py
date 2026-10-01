import pytest
from helpers import load

max_len_equal_01 = load("hashing.11_equal_zeros_ones_subarray").max_len_equal_01


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([1, 0, 1, 1, 1, 0, 0], 6),
        ([1, 1, 1, 1], 0),
        ([0, 0, 1, 1, 0], 4),
        ([0, 1], 2),
        ([0], 0),
        ([], 0),
        ([1, 0, 0, 1, 0, 1, 1], 6),
        ([0, 0, 0, 1, 0, 0], 2),
    ],
)
def test_max_len_equal_01(arr, expected):
    assert max_len_equal_01(arr) == expected
