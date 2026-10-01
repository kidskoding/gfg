import pytest
from helpers import load

count_product_less_than_k = load(
    "arrays.26_subarrays_product_less_than_k"
).count_product_less_than_k


@pytest.mark.parametrize(
    "arr, k, expected",
    [
        ([1, 2, 3, 4], 10, 7),
        ([1, 9, 2, 8, 6, 4, 3], 100, 16),
        ([10, 5, 2, 6], 100, 8),
        ([1, 2, 3], 0, 0),
        ([1, 2, 3], 1, 0),
        ([1, 1, 1], 2, 6),
        ([5], 6, 1),
    ],
)
def test_count_product_less_than_k(arr, k, expected):
    assert count_product_less_than_k(arr, k) == expected
