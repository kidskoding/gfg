import pytest
from helpers import load

remove_duplicates = load("01_arrays.13_remove_duplicates_sorted").remove_duplicates


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([2, 2, 2, 2, 2], [2]),
        ([1, 2, 4], [1, 2, 4]),
        ([1, 2, 2, 3, 4, 4, 4, 5, 5], [1, 2, 3, 4, 5]),
        ([-3, -3, 0, 0, 7], [-3, 0, 7]),
        ([5], [5]),
        ([], []),
    ],
)
def test_remove_duplicates(arr, expected):
    n = len(arr)
    k = remove_duplicates(arr)
    assert k == len(expected)
    assert arr[:k] == expected
    assert len(arr) == n
