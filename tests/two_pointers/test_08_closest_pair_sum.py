import pytest
from helpers import load

closest_pair_sum = load("two_pointers.08_closest_pair_sum").closest_pair_sum


@pytest.mark.parametrize(
    "arr, target, expected",
    [
        ([10, 30, 20, 5], 25, [5, 20]),
        ([5, 2, 7, 1, 4], 10, [2, 7]),  # 9, 9 and 11 tie; [2, 7] has the widest gap
        ([1, 3, 4, 6], 7, [1, 6]),  # exact ties: widest gap wins
        ([-1, 2, 1, -4], 4, [1, 2]),
        ([1, 1], 5, [1, 1]),
        ([10], 10, []),
        ([], 0, []),
    ],
)
def test_closest_pair_sum(arr, target, expected):
    assert closest_pair_sum(arr, target) == expected
