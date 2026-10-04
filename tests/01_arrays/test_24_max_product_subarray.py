import pytest
from helpers import load

max_product_subarray = load("01_arrays.24_max_product_subarray").max_product_subarray


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([-2, 6, -3, -10, 0, 2], 180),
        ([-1, -3, -10, 0, 6], 30),
        ([2, 3, 4], 24),
        ([-2, 0, -1], 0),
        ([-5], -5),
        ([-2, -3, 0, -2, -40], 80),
        ([0, 0], 0),
    ],
)
def test_max_product_subarray(arr, expected):
    assert max_product_subarray(arr) == expected
