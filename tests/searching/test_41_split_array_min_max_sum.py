import pytest
from helpers import load

split_array = load("searching.41_split_array_min_max_sum").split_array


@pytest.mark.parametrize(
    "arr, k, expected",
    [
        ([1, 2, 3, 4], 3, 4),
        ([1, 1, 2], 2, 2),
        ([7, 2, 5, 10, 8], 2, 18),
        ([2, 3, 1, 2, 4, 3], 5, 4),
        ([1, 4, 4], 3, 4),  # every element alone
        ([1, 2, 3], 3, 3),
        ([10, 5, 3], 1, 18),  # one part: the total
        ([5], 1, 5),
    ],
)
def test_split_array(arr, k, expected):
    assert split_array(arr, k) == expected
