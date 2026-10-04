import pytest
from helpers import load

min_pair_product_sum = load("09_sorting.23_min_product_sum_pairs").min_pair_product_sum


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([9, 2, 8, 4, 5, 7, 6, 0], 74),
        ([1, 2, 3, 4], 10),
        ([-5, -4, 1, 2], -14),
        ([3, 3, 3, 3], 18),
        ([-2, -1], 2),
        ([1, 2], 2),
        ([], 0),
    ],
)
def test_min_pair_product_sum(arr, expected):
    assert min_pair_product_sum(arr) == expected
