import pytest
from helpers import load

product_except_self = load("01_arrays.25_product_except_self").product_except_self


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([10, 3, 5, 6, 2], [180, 600, 360, 300, 900]),
        ([12, 0], [0, 12]),
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        ([0, 0, 3], [0, 0, 0]),
        ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
        ([5], [1]),
    ],
)
def test_product_except_self(arr, expected):
    assert product_except_self(arr) == expected
