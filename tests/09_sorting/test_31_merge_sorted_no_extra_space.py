import pytest
from helpers import load

merge_in_place = load("09_sorting.31_merge_sorted_no_extra_space").merge_in_place


@pytest.mark.parametrize(
    "a, b, expected_a, expected_b",
    [
        ([2, 4, 7, 10], [2, 3], [2, 2, 3, 4], [7, 10]),
        ([1, 5, 9, 10, 15, 20], [2, 3, 8, 13], [1, 2, 3, 5, 8, 9], [10, 13, 15, 20]),
        ([-3, 4], [-5, 0, 9], [-5, -3], [0, 4, 9]),
        ([5, 6], [1, 2], [1, 2], [5, 6]),
        ([0, 1], [2, 3], [0, 1], [2, 3]),
        ([1, 1, 1], [1], [1, 1, 1], [1]),
        ([], [1, 2], [], [1, 2]),
        ([3], [], [3], []),
    ],
)
def test_merge_in_place(a, b, expected_a, expected_b):
    assert merge_in_place(a, b) is None
    assert a == expected_a
    assert b == expected_b
