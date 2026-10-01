import pytest
from helpers import load

four_sum_quadruplets = load(
    "two_pointers.25_four_sum_distinct_quadruplets"
).four_sum_quadruplets


@pytest.mark.parametrize(
    "arr, target, expected",
    [
        ([10, 2, 3, 4, 5, 7, 8], 23, [[2, 3, 8, 10], [2, 4, 7, 10], [3, 5, 7, 8]]),
        ([1, 0, -1, 0, -2, 2], 0, [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]),
        ([2, 2, 2, 2, 2], 8, [[2, 2, 2, 2]]),  # duplicates collapse to one quadruplet
        ([0, 0, 0, 0], 1, []),
        ([1, 2, 3], 6, []),
        ([], 0, []),
    ],
)
def test_four_sum_quadruplets(arr, target, expected):
    assert four_sum_quadruplets(arr, target) == expected
