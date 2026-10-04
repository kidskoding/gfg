import pytest
from helpers import load

closest_triplet_sum = load("09_sorting.09_triplet_closest_sum").closest_triplet_sum


@pytest.mark.parametrize(
    "arr, target, expected",
    [
        ([-1, 2, 1, -4], 1, 2),
        ([1, 2, 3, 4, -5], 10, 9),
        ([1, 10, 4, 5], 10, 10),
        ([0, 1, 2, 10], 7, 11),  # 3 and 11 are equally close: take the larger
        ([5, 5, 5], 0, 15),
        ([-3, -2, -1, 0], 5, -3),
    ],
)
def test_closest_triplet_sum(arr, target, expected):
    assert closest_triplet_sum(arr, target) == expected
