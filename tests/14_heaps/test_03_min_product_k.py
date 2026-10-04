import pytest
from helpers import load

min_product_k = load("14_heaps.03_min_product_k").min_product_k


@pytest.mark.parametrize(
    "arr, k, expected",
    [
        ([198, 76, 544, 123, 154, 675], 2, 9348),
        ([5, 4, 1, 2, 3], 3, 6),
        ([2, 9, 4], 3, 72),
        ([3, 3, 3], 2, 9),
        ([1, 1, 1, 5], 2, 1),
        ([7], 1, 7),
    ],
)
def test_min_product_k(arr, k, expected):
    assert min_product_k(arr, k) == expected
