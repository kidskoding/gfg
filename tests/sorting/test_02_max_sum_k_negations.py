import pytest
from helpers import load

max_sum_after_k_negations = load(
    "sorting.02_max_sum_k_negations"
).max_sum_after_k_negations


@pytest.mark.parametrize(
    "arr, k, expected",
    [
        ([-2, 0, 5, -1, 2], 4, 10),
        ([9, 8, 8, 5], 3, 20),
        ([-5, -3, -1], 2, 7),
        ([-5, -3, -1], 5, 9),  # flip all, spend the extra 2 on one element
        ([-5, -3, -1], 4, 7),  # one leftover flip must hit the smallest |x|
        ([1, 2, 3], 1, 4),
        ([0, -3], 3, 3),  # leftovers absorbed by 0
        ([4], 0, 4),
    ],
)
def test_max_sum_after_k_negations(arr, k, expected):
    assert max_sum_after_k_negations(arr, k) == expected
