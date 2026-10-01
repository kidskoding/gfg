import pytest
from helpers import load

split_three_equal = load("arrays.27_split_three_equal_sums").split_three_equal


@pytest.mark.parametrize(
    "arr",
    [
        [1, 3, 4, 0, 4],
        [1, -1, 1, -1, 1, -1, 1, -1],
        [0, 0, 0],
        [3, 3, 3],
        [1, 2, 3, 0, 3],
        [-1, -1, -1],
        [2, 0, 0, 2, 0, 2],
    ],
)
def test_split_three_equal_valid(arr):
    i, j = split_three_equal(arr)
    assert 0 <= i < j < len(arr) - 1
    assert sum(arr[: i + 1]) == sum(arr[i + 1 : j + 1]) == sum(arr[j + 1 :])


@pytest.mark.parametrize(
    "arr",
    [
        [2, 3, 4],
        [1, 1],
        [3],
        [],
        [1, 5, 0],
        [1, 2, 3, 4, 5, 6],
    ],
)
def test_split_three_equal_impossible(arr):
    assert split_three_equal(arr) == [-1, -1]
