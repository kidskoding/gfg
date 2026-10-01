import pytest
from helpers import load

reverse_in_groups = load("arrays.04_reverse_in_groups").reverse_in_groups


@pytest.mark.parametrize(
    "arr, k, expected",
    [
        ([1, 2, 3, 4, 5], 3, [3, 2, 1, 5, 4]),
        ([5, 6, 8, 9], 5, [9, 8, 6, 5]),
        ([1, 2, 3, 4, 5, 6, 7, 8], 3, [3, 2, 1, 6, 5, 4, 8, 7]),
        ([1, 2, 3, 4], 2, [2, 1, 4, 3]),
        ([1, 2, 3], 1, [1, 2, 3]),
        ([1, 2, 3, 4], 4, [4, 3, 2, 1]),
        ([], 2, []),
    ],
)
def test_reverse_in_groups(arr, k, expected):
    reverse_in_groups(arr, k)
    assert arr == expected
