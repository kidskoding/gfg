import pytest
from helpers import load

max_subarray_xor = load("bit_manipulation.36_max_subarray_xor").max_subarray_xor


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([1, 2, 3, 4], 7),
        ([8, 1, 2, 12, 7, 6], 15),
        ([4, 6], 6),
        ([5, 1], 5),
        ([2, 2, 2], 2),
        ([0, 0], 0),
        ([5], 5),
    ],
)
def test_max_subarray_xor(arr, expected):
    assert max_subarray_xor(arr) == expected
