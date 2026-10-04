import pytest
from helpers import load

k_max_sum_combinations = load("14_heaps.31_k_max_sum_combinations").k_max_sum_combinations


@pytest.mark.parametrize(
    "a, b, k, expected",
    [
        ([3, 2], [1, 4], 2, [7, 6]),
        ([4, 2, 5, 1], [8, 0, 5, 3], 3, [13, 12, 10]),
        ([1, 2, 3], [1, 2, 3], 9, [6, 5, 5, 4, 4, 4, 3, 3, 2]),
        ([1, 1], [1, 1], 4, [2, 2, 2, 2]),  # equal sums from distinct index pairs
        ([-1, -2], [-3, 0], 3, [-1, -2, -4]),
        ([1], [1], 1, [2]),
    ],
)
def test_k_max_sum_combinations(a, b, k, expected):
    assert k_max_sum_combinations(a, b, k) == expected
