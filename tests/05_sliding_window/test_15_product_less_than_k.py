import pytest
from helpers import load

count_product_less_than_k = load(
    "05_sliding_window.15_product_less_than_k"
).count_product_less_than_k


@pytest.mark.parametrize(
    "arr, k, expected",
    [
        ([10, 5, 2, 6], 100, 8),
        ([1, 2, 3, 4], 10, 7),
        ([1, 9, 2, 8, 6, 4, 3], 100, 16),
        ([1, 1, 1], 2, 6),
        ([5], 5, 0),  # strictly less
        ([1, 2, 3], 0, 0),
        ([], 10, 0),
    ],
)
def test_count_product_less_than_k(arr, k, expected):
    assert count_product_less_than_k(arr, k) == expected
