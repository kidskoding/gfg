import pytest
from helpers import load

pair_in_sorted_rotated = load(
    "04_two_pointers.07_pair_sum_sorted_rotated"
).pair_in_sorted_rotated


@pytest.mark.parametrize(
    "arr, target, expected",
    [
        ([11, 15, 6, 8, 9, 10], 16, True),
        ([11, 15, 26, 38, 9, 10], 35, True),
        ([11, 15, 26, 38, 9, 10], 45, False),
        ([1, 2, 3, 4, 5], 9, True),  # not rotated
        ([4, 5, 1, 2, 3], 10, False),
        ([4, 5, 1, 2, 3], 3, True),
        ([2, 1], 3, True),
        ([5], 10, False),
    ],
)
def test_pair_in_sorted_rotated(arr, target, expected):
    assert pair_in_sorted_rotated(arr, target) is expected
