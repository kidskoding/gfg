import pytest
from helpers import load

can_partition = load("dynamic_programming.13_partition_problem").can_partition


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([1, 5, 11, 5], True),
        ([1, 5, 3], False),
        ([1, 3, 5], False),
        ([3, 1, 1, 2, 2, 1], True),
        ([2, 2], True),
        ([1], False),
        ([0], True),
        ([], True),
    ],
)
def test_can_partition(arr, expected):
    assert can_partition(arr) == expected
