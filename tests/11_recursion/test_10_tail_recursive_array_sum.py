import pytest
from helpers import load

tail_sum = load("11_recursion.10_tail_recursive_array_sum").tail_sum


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([1, 8, 9], 18),
        ([2, 55, 1, 7], 65),
        ([4], 4),
        ([], 0),
        ([-3, 3, -7], -7),
        ([1, 1, 1, 1, 1], 5),
    ],
)
def test_tail_sum_whole_array(arr, expected):
    assert tail_sum(arr, len(arr)) == expected


@pytest.mark.parametrize(
    "arr, n, acc, expected",
    [
        ([1, 2, 3, 4, 5], 3, 0, 6),  # only the first n elements count
        ([1, 2, 3], 0, 0, 0),
        ([1, 2, 3], 3, 10, 16),  # acc is the running total carried in
        ([5, 5], 1, -5, 0),
    ],
)
def test_tail_sum_prefix_and_acc(arr, n, acc, expected):
    assert tail_sum(arr, n, acc) == expected
