import pytest
from helpers import load

zero_sum_triplets = load("10_searching.17_zero_sum_triplets").zero_sum_triplets


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([0, -1, 2, -3, 1], [[0, 1, 4], [2, 3, 4]]),
        ([1, -2, 1, 0, 5], [[0, 1, 2]]),
        ([2, 3, 1, 0, 5], []),
        (
            [-1, 0, 1, 2, -1, -4],
            [[0, 1, 2], [0, 3, 4], [1, 2, 4]],
        ),  # equal values, different indices
        ([0, 0, 0, 0], [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]]),
        ([1, 2], []),
        ([], []),
    ],
)
def test_zero_sum_triplets(arr, expected):
    assert sorted(list(t) for t in zero_sum_triplets(arr)) == expected
