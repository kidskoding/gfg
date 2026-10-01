import pytest
from helpers import load

remove_duplicates = load("two_pointers.03_unique_in_sorted_array").remove_duplicates


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([2, 2, 2, 2, 2], [2]),
        ([1, 2, 4], [1, 2, 4]),
        ([1, 1, 2, 3, 3, 3, 4], [1, 2, 3, 4]),
        ([-3, -3, -1, 0, 0, 2], [-3, -1, 0, 2]),
        ([5], [5]),
        ([], []),
    ],
)
def test_remove_duplicates(arr, expected):
    k = remove_duplicates(arr)
    assert k == len(expected)
    assert arr[:k] == expected
