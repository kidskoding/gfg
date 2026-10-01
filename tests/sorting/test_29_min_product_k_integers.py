import pytest
from helpers import load

min_product_k = load("sorting.29_min_product_k_integers").min_product_k


@pytest.mark.parametrize(
    "arr, k, expected",
    [
        ([198, 76, 544, 123, 154, 675], 2, 9348),
        ([11, 8, 5, 7, 5, 100], 4, 1400),
        ([4, 3, 2, 1], 4, 24),
        ([10, 1, 1], 2, 1),
        ([2, 2, 2], 3, 8),
        ([3], 1, 3),
    ],
)
def test_min_product_k(arr, k, expected):
    assert min_product_k(arr, k) == expected
