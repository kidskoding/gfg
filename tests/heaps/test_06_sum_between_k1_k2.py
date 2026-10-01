import pytest
from helpers import load

sum_between_k1_k2 = load("heaps.06_sum_between_k1_k2").sum_between_k1_k2


@pytest.mark.parametrize(
    "arr, k1, k2, expected",
    [
        ([20, 8, 22, 4, 12, 10, 14], 3, 6, 26),
        ([10, 2, 50, 12, 48, 13], 2, 6, 73),
        ([5, 1, 4, 2, 3], 1, 5, 9),
        ([-1, -5, 3, 0], 1, 4, -1),
        ([4, 4, 4, 4], 1, 4, 8),
        ([1, 2, 3], 1, 2, 0),  # adjacent ranks: nothing in between
    ],
)
def test_sum_between_k1_k2(arr, k1, k2, expected):
    assert sum_between_k1_k2(arr, k1, k2) == expected
