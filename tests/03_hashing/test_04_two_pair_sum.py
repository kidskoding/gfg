import pytest
from helpers import load

find_two_pairs = load("03_hashing.04_two_pair_sum").find_two_pairs


@pytest.mark.parametrize(
    "arr",
    [
        [3, 4, 7, 1, 2, 9, 8],
        [1, 2, 3, 4],  # 1 + 4 == 2 + 3
        [0, 0, 0, 0],
        [-1, 5, 2, 2],  # -1 + 5 == 2 + 2
        [10, 1, 20, 3, 5, 6],  # only 1 + 10 == 5 + 6
    ],
)
def test_find_two_pairs_found(arr):
    result = find_two_pairs(arr)
    assert result is not None
    i, j, k, l = result
    assert len({i, j, k, l}) == 4
    assert all(0 <= x < len(arr) for x in result)
    assert arr[i] + arr[j] == arr[k] + arr[l]


@pytest.mark.parametrize(
    "arr",
    [
        [65, 30, 7, 90, 1, 9, 8],  # GFG: all 21 pair sums differ
        [1, 2, 4, 8, 16],  # powers of two: all pair sums differ
        [1, 2, 3],
        [5],
        [],
    ],
)
def test_find_two_pairs_none(arr):
    assert find_two_pairs(arr) is None
