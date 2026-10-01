from collections import Counter

import pytest
from helpers import load

tug_of_war = load("backtracking.06_tug_of_war").tug_of_war


@pytest.mark.parametrize(
    "arr, min_diff",
    [
        ([3, 4, 5, -3, 100, 1, 89, 54, 23, 20], 0),
        ([23, 45, -34, 12, 0, 98, -99, 4, 189, -1, 4], 1),
        ([1, 2, 3, 4], 0),
        ([1, 1, 1, 1, 100, 100], 0),
        ([-1, -2, -3, 10], 10),  # 10 must share a side with exactly one negative
        ([5, 5, 5], 5),
        ([1], 1),
    ],
)
def test_tug_of_war(arr, min_diff):
    a, b = tug_of_war(list(arr))
    assert Counter(a) + Counter(b) == Counter(arr)
    assert sorted([len(a), len(b)]) == [len(arr) // 2, len(arr) - len(arr) // 2]
    assert abs(sum(a) - sum(b)) == min_diff
