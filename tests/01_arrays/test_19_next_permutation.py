import pytest
from helpers import load

next_permutation = load("01_arrays.19_next_permutation").next_permutation


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([2, 4, 1, 7, 5, 0], [2, 4, 5, 0, 1, 7]),
        ([3, 2, 1], [1, 2, 3]),
        ([3, 4, 2, 5, 1], [3, 4, 5, 1, 2]),
        ([1, 2, 3], [1, 3, 2]),
        ([1, 1, 5], [1, 5, 1]),
        ([1, 5, 1], [5, 1, 1]),
        ([7], [7]),
        ([2, 2], [2, 2]),
    ],
)
def test_next_permutation(arr, expected):
    next_permutation(arr)
    assert arr == expected
