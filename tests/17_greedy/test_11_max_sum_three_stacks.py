import pytest
from helpers import load

max_equal_sum = load("17_greedy.11_max_sum_three_stacks").max_equal_sum


@pytest.mark.parametrize(
    "s1, s2, s3, expected",
    [
        ([3, 2, 1, 1, 1], [4, 3, 2], [1, 1, 4, 1], 5),
        ([1, 1, 4, 1], [4, 3, 2], [3, 2, 1, 1, 1], 5),  # same stacks, reordered
        ([2, 2, 2], [3, 3], [6], 6),  # already equal, nothing popped
        ([1, 2, 3], [1, 2, 3], [1, 2, 3], 6),
        ([1, 4], [5], [2, 3], 5),
        ([1, 1, 1], [2], [3], 0),  # only equal when all empty
        ([10], [1, 2], [3], 0),
        ([], [1], [1], 0),
    ],
)
def test_max_equal_sum(s1, s2, s3, expected):
    assert max_equal_sum(s1, s2, s3) == expected
