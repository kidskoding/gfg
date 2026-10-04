import pytest
from helpers import load

min_partition_diff = load("18_dynamic_programming.04_minimum_partition").min_partition_diff


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([1, 6, 11, 5], 1),
        ([1, 4], 3),
        ([1, 5, 11, 5], 0),
        ([36, 7, 46, 40], 23),
        ([3, 1, 4, 2, 2, 1], 1),
        ([7], 7),
        ([0, 0], 0),
        ([], 0),
    ],
)
def test_min_partition_diff(arr, expected):
    assert min_partition_diff(arr) == expected
