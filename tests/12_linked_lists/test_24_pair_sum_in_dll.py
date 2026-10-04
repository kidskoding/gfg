import pytest
from helpers import load
from helpers.linked_lists import build_dlist

pair_sum = load("12_linked_lists.24_pair_sum_in_dll").pair_sum


@pytest.mark.parametrize(
    "values, target, expected",
    [
        ([1, 2, 4, 5, 6, 8, 9], 7, [(1, 6), (2, 5)]),
        ([1, 5, 6], 6, [(1, 5)]),
        ([1, 3, 5, 7, 9], 10, [(1, 9), (3, 7)]),  # 5 cannot pair with itself
        ([-3, -1, 0, 2, 4], 1, [(-3, 4), (-1, 2)]),
        ([1, 2, 3], 10, []),
        ([5], 10, []),
        ([], 0, []),
    ],
)
def test_pair_sum(values, target, expected):
    assert pair_sum(build_dlist(values), target) == expected
